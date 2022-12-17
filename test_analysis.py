import unittest
import pandas as pd
# module to check pandas dataframe
from pandas.testing import assert_frame_equal

import data.store_data as sd
from analysis.analysis import Analysis as a

class TestAnalysis(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Analysis test starts")
        filename = "statement.csv"
        # creting a object
        cls.base_df = sd.Expenses()
        # add the csv file
        cls.base_df.add_csv(filename)
        # show all expenses
        cls.df = cls.base_df.show_expenses()

    # setting up for test
    def setUp(self):
        print("Test Setup")
        self.p = a(self.df, "02/11/2022", "02/11/2022")
        self.p_2 = a(self.df, "02/11/2022", "26/11/2022")

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("Analysis test finishes")

    # test casae
    def test_income_expense_ratio_range(self): 
        self.assertEqual(self.p.income_expense_ratio_range(1000), 1.1079999999999999)
        self.assertNotEqual(self.p.income_expense_ratio_range(1000), 1.107)
        self.assertEqual(self.p.income_expense_ratio_range(0), None)
        self.assertEqual(self.p.income_expense_ratio_range(3452.23), 0.32095196438244267)

    # test case
    def test_category_percentage(self):
        actual = self.p.category_average()
        actual_2 = self.p_2.category_average()

        self.assertEqual(actual['average'][0], 11.08)
        self.assertNotEqual(actual['average'][0], None)
        self.assertEqual(actual_2['average'][0], 17.018571428571427)
        self.assertEqual(round(actual_2['average'][0], 2), round(17.018571428571427, 2))

unittest.main(argv=[''], verbosity=2, exit=False)

