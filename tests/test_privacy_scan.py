import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "privacy_scan.py"


class PrivacyScanTest(unittest.TestCase):
    def run_scan(self, text: str):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "sample.md").write_text(text, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), directory],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_clean_text_passes(self):
        result = self.run_scan("# Fictional example\n\nNo private information.\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_absolute_home_path_fails(self):
        private_path = "/" + "Users/example/secret.md"
        result = self.run_scan(f"Private file: {private_path}\n")
        self.assertEqual(result.returncode, 1)
        self.assertIn("absolute home path", result.stdout)

    def test_token_fails(self):
        token = "gh" + "p_abcdefghijklmnopqrstuvwxyz123456"
        result = self.run_scan(f"token = {token}\n")
        self.assertEqual(result.returncode, 1)
        self.assertIn("GitHub token", result.stdout)


if __name__ == "__main__":
    unittest.main()
