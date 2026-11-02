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
                ".git", "dist", "evals", "__pycache__"))
            for relative in ("README.md", "docs/INSTALL.md", "provenance/workflow-audit.md"):
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


if __name__ == "__main__":
    unittest.main()
