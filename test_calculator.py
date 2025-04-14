# https://github.com/Cstar354/lab10-CS-
# Partner 1: Camari 
# Partner 2: William
import unittest
from calculator import *

# git add calculator.py    
# git commit -m "merged changes"
# git push	

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-2, -2), -4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(11, 4), 7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(2, 1), 2)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(36, 6), 6.0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(math.e, 1), 0)
        self.assertAlmostEqual(logarithm(1000, 10), 3)
        self.assertAlmostEqual(logarithm(8, 2), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(6, 10), 9.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

# Do not touch this
if __name__ == "__main__":
    unittest.main()
