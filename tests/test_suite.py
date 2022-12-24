import sys
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis")
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis\\expta")

import unittest

from test_search import TestSearch 
from test_analysis import TestAnalysis 
from test_store_data import TestStoreData
from test_categorize import TestCategorize

def my_suite():
    suite = unittest.TestSuite() 
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestAnalysis))  
    suite.addTest(unittest.makeSuite(TestStoreData))
    suite.addTest(unittest.makeSuite(TestCategorize))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    #print(result)

my_suite()