"""Regression scenarios for state, ledger and package operations; no model calls."""
import json, subprocess, sys, tempfile, shutil, unittest, os
from pathlib import Path

SA = Path(__file__).resolve().parents[1]
S = SA / "scripts"
sys.path.insert(0, str(S))
import validate_artifacts as va, project_state as ps, validate_package as vp

def run(*args, cwd=None):
    r = subprocess.run([sys.executable, "-B", *map(str, args)], capture_output=True, text=True, encoding="utf-8", cwd=cwd, timeout=60, env={**os.environ, "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1"})
    return r.returncode, (r.stdout + r.stderr).strip()

class RegressionScenarios(unittest.TestCase):
    def test_previous_regressions(self):
        def check(name, condition, detail=""):
            with self.subTest(scenario=name):
                self.assertTrue(condition, str(detail))

        with tempfile.TemporaryDirectory(prefix="sa-regression-") as directory:
            tmp = Path(directory)
            # H1
            ex = json.loads((SA / "skills/sa-workflow/references/state.example.json").read_text())
            res, rep = ps.resume(ex, tmp, {})
            check("H1 pending+unknown stays pending", {k: v["status"] for k, v in res["stages"].items()} == {"analysis": "pending", "writing": "pending"}, res)
            check("H1 note reported", "analysis" in rep["status_preserved_notes"] and rep["next_candidates"] == ["analysis"], rep)
            # H1: complete stage with changed output still stale; dependents handled
            (tmp / "o.md").write_text("v1"); (tmp / "in.csv").write_text("x")
            h_in = "sha256:" + va.file_hash(tmp / "in.csv")
            st = {"schema_version": 1, "goal": "g", "run_id": "r", "stages": {
                "a": {"status": "complete", "inputs": {"in.csv": h_in}, "depends_on": [], "outputs": ["o.md"],
                      "output_versions": {"o.md": "sha256:" + "0" * 64}},
                "b": {"status": "complete", "inputs": {}, "depends_on": ["a"], "outputs": ["o.md"], "output_versions": {"o.md": "sha256:" + va.file_hash(tmp / "o.md")}},
                "n": {"status": "not_applicable", "reason": "theory", "inputs": {}, "depends_on": ["a"], "outputs": []},
                "d": {"status": "needs_decision", "decision": "pick", "inputs": {}, "depends_on": ["a"], "outputs": []}}}
            res, rep = ps.resume(st, tmp, {})
            got = {k: v["status"] for k, v in res["stages"].items()}
            check("H1 complete changed->stale, dependents semantic", got == {"a": "stale", "b": "stale", "n": "not_applicable", "d": "needs_decision"}, got)
            check("H1 preserved notes for n,d", set(rep["status_preserved_notes"]) == {"n", "d"}, rep)
            # H2
            st2 = json.loads(json.dumps(st)); st2["stages"]["a"]["inputs"] = {"x": "v1"}; st2["stages"]["p"] = {"status": "pending", "inputs": {"x": "v1"}, "depends_on": [], "outputs": []}
            got = {k: v["status"] for k, v in va.mark_stale(st2, {"x": "v2"})["stages"].items()}
            check("H2 mark_stale preserves statuses", got == {"a": "stale", "b": "stale", "n": "not_applicable", "d": "needs_decision", "p": "pending"}, got)
            # H3 docs
            issues = (SA / "shared/ISSUES.md").read_text(encoding="utf-8")
            statemd = (SA / "skills/sa-workflow/references/state.md").read_text(encoding="utf-8")
            check("H3 doc commands resolve the package path", "python scripts/" not in issues and "SA/scripts/validate_artifacts.py" in issues and "SA/scripts/validate_artifacts.py" in statemd)
            # H4
            p = tmp / "h.json"; p.write_bytes(b"\xef\xbb\xbf" + (SA / "shared/handoff.example.json").read_bytes())
            rc, out = run(S / "validate_artifacts.py", "handoff", p)
            check("H4 BOM accepted", rc == 0, out)
            # H5
            rc, out = run(S / "validate_package.py")
            check("H5 default mode passes w/o evals", rc == 0 and '"not_present_in_checkout"' in out, out[:300])
            rc, out = run(S / "validate_package.py", "--runtime-only")
            check("H5 runtime-only passes", rc == 0, out[:300])
            # M1
            (tmp / "st.json").write_text(json.dumps({"schema_version": 1, "goal": "g", "run_id": "r", "stages": {}}))
            rc, out = run(S / "project_state.py", "save", "state", "st.json", "--root", ".", "--output", "canon.json", cwd=tmp)
            h = json.loads(out)["sha256"]
            rc, out = run(S / "project_state.py", "save", "state", "st.json", "--root", ".", "--output", "canon.json", "--expect-sha256", "SHA256:" + h.upper(), cwd=tmp)
            check("M1 uppercase expect accepted", rc == 0, out)
            # M2
            rc, out = run(S / "project_state.py", "snapshot", "o.md", "--root", ".", "--expect-sha256", "abc", cwd=tmp)
            check("M2 snapshot rejects --expect-sha256", rc == 2, out)
            rc, out = run(S / "project_state.py", "record-outputs", "st.json", "--root", ".", "--sources", "x.json", cwd=tmp)
            check("M2 record-outputs rejects --sources", rc == 2, out)
            # M3
            s3 = {"schema_version": 1, "goal": "g", "run_id": "r", "stages": {"a": {"status": "complete", "inputs": {}, "depends_on": [], "outputs": ["o.md"], "output_versions": {"o.md": "sha256:" + "0" * 64}}}}
            (tmp / "s3.json").write_text(json.dumps(s3))
            rc, out = run(S / "project_state.py", "record-outputs", "s3.json", "--root", ".", cwd=tmp)
            check("M3 refuses changed recorded output", rc == 1 and "--rerecord" in out, out)
            rc, out = run(S / "project_state.py", "record-outputs", "s3.json", "--root", ".", "--rerecord", cwd=tmp)
            check("M3 --rerecord reports change", rc == 0 and "rerecorded_changed_outputs" in out, out[:300])
            s4 = json.loads(json.dumps(s3)); del s4["stages"]["a"]["output_versions"]; (tmp / "s4.json").write_text(json.dumps(s4))
            check("M3 first recording works", run(S / "project_state.py", "record-outputs", "s4.json", "--root", ".", cwd=tmp)[0] == 0)
            # M4
            led = {"issues": [{"id": "R1", "summary": "s", "severity": "major", "status": "open", "anchor": None,
                               "close_criterion": "c", "history": [{"at": "2026-01-01", "status": "open", "reason": "new"}]}]}
            l3 = ps.transition(ps.transition(led, "R1", "deferred", "later", None, tmp, {}), "R1", "open", "back", None, tmp, {})
            check("M4 reopen drops stale reason", "reason" not in l3["issues"][0] and l3["issues"][0]["history"][1]["reason"] == "later")
            # M5
            try:
                ps.transition(led, "R1", "resolved", "done", None, tmp, {}); check("M5", False)
            except ValueError as e:
                check("M5 message names resolved", "resolved status needs" in str(e) and "verified finding" not in str(e), e)
            # M6
            new = json.loads(json.dumps(led)); new["issues"][0]["history"][0]["reason"] = "edited"; new["issues"][0]["close_criterion"] = "weaker"
            errs = va.validate_ledger_update(led, new)
            check("M6 both violations reported", len(errs) == 2, errs)
            # M7
            bad = json.loads(json.dumps(led)); del bad["issues"][0]["history"][0]["at"]
            errs = va.validate_ledger(bad)
            check("M7 single error for missing at", len(errs) == 1, errs)
            # M8
            fake = tmp / "pkg"; shutil.copytree(SA, fake, ignore=shutil.ignore_patterns(".git", "dist", "evals", "__pycache__"))
            (fake / "skills/sa-code-audit/agents/openai.yaml").write_text("")
            r = vp.check(fake, runtime_only=True)
            check("M8 empty yaml -> error not crash", not r["valid"] and any("interface mapping" in e for e in r["errors"]), r["errors"])
            # M10
            lr = {"issues": [
                {"id": "R1", "summary": "s", "severity": "major", "status": "withdrawn", "reason": "criterion changed", "anchor": None, "close_criterion": "c", "replaced_by": "R2",
                 "history": [{"at": "2026-01-01", "status": "withdrawn", "reason": "criterion changed"}]},
                {"id": "R2", "summary": "s", "severity": "major", "status": "open", "anchor": None, "close_criterion": "c2", "replaces": "R1",
                 "history": [{"at": "2026-01-01", "status": "open", "reason": "replacement"}]}]}
            check("M10 valid link accepted", va.validate_ledger(lr) == [], va.validate_ledger(lr))
            lr["issues"][1]["replaces"] = "R9"; lr["issues"][0]["status"] = "open"; lr["issues"][0]["history"][0]["status"] = "open"
            errs = va.validate_ledger(lr)
            check("M10 dangling link + non-withdrawn replaced rejected", len(errs) == 2, errs)
            # CLI arg hygiene
            check("CLI changes only for stale", run(S / "validate_artifacts.py", "state", "a.json", "b.json", cwd=tmp)[0] == 2)
            check("CLI stale rejects --root", run(S / "validate_artifacts.py", "stale", "a.json", "b.json", "--root", ".", cwd=tmp)[0] == 2)
            # build: frontmatter break rejected; normal build ok
            (fake / "skills/sa-code-audit/agents/openai.yaml").write_bytes((SA / "skills/sa-code-audit/agents/openai.yaml").read_bytes())
            sk = fake / "skills/sa-code-audit/SKILL.md"; sk.write_text(sk.read_text(encoding="utf-8").replace("name: sa-code-audit", "name: wrong"), encoding="utf-8")
            rc, out = run(fake / "scripts/build_release.py", "--output", tmp / "b1")
            check("build rejects broken frontmatter", rc == 1 and "structure check failed" in out, out)
            rc, out = run(S / "build_release.py", "--output", tmp / "b2")
            check("build succeeds on real package", rc == 0, out)


if __name__ == "__main__":
    unittest.main()
