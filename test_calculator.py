# https://github.com/Cstar354/lab10-CS-CS
# Partner 1: Camari
# Partner 2: William
# git clone https://github.com/Cstar354/lab10-CS-CS
# cd lab10-CS-CS
# git add calculator.py
# git commit -m "modified calculator p1"
# git push
import unittest
from calculator import *

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
    def test_mul(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(2, 1), 2)

    def test_div(self): # 3 assertions
        self.assertEqual(div(10, 2), 5.0)
        self.assertEqual(div(6, 36), 0.16666666666666666)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)  # Divide by zero should raise an error

    ######## Partner 2
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(2, 32), 5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

# Do not touch this
if __name__ == "__main__":
    unittest.main()
