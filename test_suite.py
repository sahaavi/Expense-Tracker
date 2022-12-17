import unittest

from test_search import TestSearch
from test_analysis import TestAnalysis 

def my_suite():
    suite = unittest.TestSuite() 
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestAnalysis))  
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    #print(result)

my_suite()