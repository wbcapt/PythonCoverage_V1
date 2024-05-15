import unittest
import MultiplyFunctions as mf

class testMultiplyFunctions(unittest.TestCase):
    def test_multiply_by_two(self):
        self.assertEqual(mf.multiply_by_two(4),8)  # add assertion here


if __name__ == '__main__':
    unittest.main()
