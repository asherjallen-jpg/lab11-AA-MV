import unittest
from calculator import *

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
        self.assertTrue(sub(a, b) == 6)

        m, n = -5, 5
        self.assertEqual(sub(m, n), -10)

        x, y = 8, 8
        self.assertFalse(sub(x, y) == 3)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):# def test_divide_by_zero(self): # 1 assertion
        nums =(100,0)    # call division function inside, example:
        with self.assertRaises(ZeroDivisionError): # with self.assertRaises(<INSERT_ERROR_TYPE>):
            div(*nums)#     div(0, 5)


    def test_logarithm(self): # 3 assertions
        a,b=8,2
        self.assertEqual(log(a,b),3)

        m,n=100,10
        self.assertTrue(log(m,n)==2)

        x,y=1,5
        self.assertFalse(log(x,y)==8)

    def test_log_invalid_base(self): # 1 assertion
        vals =(10,1)#     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(*vals)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()