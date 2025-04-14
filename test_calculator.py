# https://github.com/Cstar354/lab10-CS-
# Partner 1: Camari 
# Partner 2: William
import unittest
from calculator import *
git add calculator.py    
git commit -m "merged changes"
git push	
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqualadd(2,2),4)
        self.assertEqualadd(5,5),10)
        self.assertEqual(-2,-2,-4)

     def test_subtract(self): # 3 assertions
         self.assertEqualsubtract(5,2),3)
         self.assertEqualsubtract(2,5),-3)
         self.assertEqualsubtract(11,4),7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqualmultiply(3,4),12)
        self.assertEqualmultiply(5,3),15)
        self.assertEqualmultiply(2,1),2)
        
  
    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2,10),5.0)
        self.assertEqual(divide(6,36),6.0)
        with self.assertRaises(ZeroDivisionError):
            divide(0,5)
    

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
               div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(math.e,1)
        self.assertAlmostEqual(logarithm(1000,10),3)
        self.assertAlmostEqual(logarithm(8,2),3
    

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10,1)
    

     def test_log_invalid_argument(self):
         with self.assertRaises(<INSERT_ERROR_TYPE>):
               logarithm(0, 5)


    def test_hypotenuse(self):
        self.assertAlmostEqualhypotenuse(3,4),5.0)
        self.assertAlmostEqualhypotenuse(6,10),9.0)
        self.assertAlmostEqualhypotenuse(0,0),0.0)
     def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqualhypotenuse(square_root(16),4.0)
        self.assertAlmostEqualhypotenuse(square_root(2),math.sqrt(2))

# Do not touch this
if __name__ == "__main__":
    unittest.main()
