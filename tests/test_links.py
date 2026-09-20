import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_links.py"


class LinkCheckTest(unittest.TestCase):
    def run_check(self, files: dict[str, str]):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, content in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), directory],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_existing_link_passes(self):
        result = self.run_check({"README.md": "[Guide](docs/guide.md)", "docs/guide.md": "# Guide"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_link_fails(self):
        result = self.run_check({"README.md": "[Missing](docs/missing.md)"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("unresolved", result.stdout)


if __name__ == "__main__":
    unittest.main()
