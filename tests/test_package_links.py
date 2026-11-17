"""Public documentation links are checked without building an archive."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_package


class PackageLinks(unittest.TestCase):
    def test_public_documentation_links(self):
        with tempfile.TemporaryDirectory(prefix="sa-links-") as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
                ".git", "evals", "__pycache__"))
            for relative in ("README.md", "README.en.md", "skills/sa-workflow/references/state.md"):
                with self.subTest(document=relative):
                    path = root / relative
                    original = path.read_text(encoding="utf-8")
                    try:
                        path.write_text(original + "\n[Missing](missing-page.md)\n", encoding="utf-8")
                        result = validate_package.check(root, runtime_only=True)
                        self.assertFalse(result["valid"])
                        self.assertTrue(any(relative in error.replace("\\", "/") and "missing-page.md" in error
                                            for error in result["errors"]), result["errors"])
                    finally:
                        path.write_text(original, encoding="utf-8")
            self.assertTrue(validate_package.check(root, runtime_only=True)["valid"])

    def test_readmes_link_each_other(self):
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertIn("](README.en.md)", chinese)
        self.assertIn("](README.md)", english)


if __name__ == "__main__":
    unittest.main()
