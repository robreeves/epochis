import unittest
import sys
import io
from epochis.__main__ import main


def _capture_stdout(func):
    stdout = sys.stdout
    try:
        func_out = io.StringIO()
        sys.stdout = func_out

        func()
        return func_out.getvalue().rstrip()
    finally:
        sys.stdout = stdout


class TestMain(unittest.TestCase):
    def test_months(self):
        out = _capture_stdout(lambda: main(["foo", "604m"]))
        self.assertEqual("2020-05", out)

    def test_days(self):
        out = _capture_stdout(lambda: main(["foo", "18412d"]))
        self.assertEqual("2020-05-30", out)

    def test_seconds(self):
        out = _capture_stdout(lambda: main(["foo", "1590792100s"]))
        self.assertEqual("2020-05-29 22:41:40", out)

    def test_milliseconds(self):
        out = _capture_stdout(lambda: main(["foo", "1590792100123ms"]))
        self.assertEqual("2020-05-29 22:41:40.123000", out)


if __name__ == '__main__':
    unittest.main()
