#https://github.com/asherjallen-jpg/lab11-AA-MV.git
#Partner 1: Asher Allen
#Partner 2: Mariana Velasco
import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # def test_add(self): # 3 assertions
    #     fill in code
        a,b= 8,2
        self.assertTrue(add(a,b) == 10)

        m,n= -5,5
        self.assertEqual(add(m,n),0)

        x,y= 8,8
        self.assertFalse(add(x,y) == 6)

    def test_subtract(self): # def test_subtract(self): # 3 assertions
    #     fill in code
        a, b = 8, 2
        self.assertTrue(subtract(a, b) == 6)

        m, n = -5, 5
        self.assertEqual(subtract(m, n), -10)

        x, y = 8, 8
        self.assertFalse(subtract(x, y) == 3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 3), 3)
        a,b = -1,-3
        self.assertEqual(mul(a, 3), b)
        self.assertAlmostEqual(mul(1.5, 3), 4.5)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(1, 2), .5)
        self.assertAlmostEqual(div(-4, 2), -2)

    ######## Partner 2
    def test_divide_by_zero(self):# def test_divide_by_zero(self): # 1 assertion
        nums =(100,0)    # call division function inside, example:
        with self.assertRaises(ZeroDivisionError): # with self.assertRaises(<INSERT_ERROR_TYPE>):
            div(*nums)#     div(0, 5)


    def test_logarithm(self): # 3 assertions
        a,b=8,2
        self.assertEqual(logarithm(a,b),3)

        m,n=100,10
        self.assertTrue(logarithm(m,n)==2)

        x,y=1,5
        self.assertFalse(logarithm(x,y)==8)

    def test_log_invalid_base(self): # 1 assertion
        vals =(10,1)#     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(*vals)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(10, -1)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(9), 5.0)
        self.assertAlmostEqual(square_root(5), math.sqrt(5))

# Do not touch this
if __name__ == "__main__":
    unittest.main()