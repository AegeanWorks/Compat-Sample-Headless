#!/usr/bin/env python3
"""Regression shield for the headless compat drive (stdlib only)."""
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


def run_script(name, *args, timeout=30.0):
    cmd = [sys.executable, str(ROOT / name), *args]
    done = subprocess.run(
        cmd,
        cwd=str(ROOT),
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    return done.returncode, (done.stdout + done.stderr).strip()


class CompatDriveTest(unittest.TestCase):
    def test_inventory_lines_are_kind_name_locator(self):
        code, out = run_script("inventory.py")
        self.assertEqual(code, 0, msg=out[-400:])
        lines = [line.strip() for line in out.splitlines() if line.strip()]
        self.assertGreaterEqual(len(lines), 1, msg="inventory printed no entries")
        for entry in lines:
            parts = entry.split("|")
            self.assertEqual(len(parts), 3, msg=f"bad inventory line: {entry[:120]}")
            self.assertTrue(all(part.strip() for part in parts))

    def test_scripted_drive_prints_world_delta(self):
        code, out = run_script("demo.py", "--scripted")
        self.assertEqual(code, 0, msg=out[-400:])
        self.assertIn("WORLD-DELTA:", out)
        self.assertIn("OK: scripted drive complete", out)

    def test_scripted_drive_requires_flag(self):
        code, _out = run_script("demo.py")
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
