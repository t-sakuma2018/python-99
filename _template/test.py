import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.do(), True)


if __name__ == "__main__":
    unittest.main()
