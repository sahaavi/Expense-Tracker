import unittest

from test_search import TestSearch 

def my_suite():
    suite = unittest.TestSuite() 
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSearch))  
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    #print(result)

my_suite()