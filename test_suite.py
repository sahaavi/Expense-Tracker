import unittest

from test_search import TestSearch 
from test_store_data import TestStoreData
from test_categorize import TestCategorize

def my_suite():
    suite = unittest.TestSuite() 
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSearch))  
    suite.addTest(unittest.makeSuite(TestStoreData))
    suite.addTest(unittest.makeSuite(TestCategorize))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    #print(result)

my_suite()