import unittest
import pandas as pd
# module to check pandas dataframe
from pandas.testing import assert_frame_equal

import data.store_data as sd
from analysis.search import Search as s

class TestSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Test class starts")
        filename = "statement.csv"
        # creting a object
        cls.base_df = sd.Expenses()
        # add the csv file
        cls.base_df.add_csv(filename)
        # show all expenses
        cls.df = cls.base_df.show_expenses()
        cname = "grocery"

    # setting up for test
    def setUp(self):
        print("Test Setup")
        self.p = s(self.df)
        self.cdf = pd.DataFrame({'date': ['11/02/2022'], 'shop_name': ['SAVE ON FOODS #2229'], 'amount': [11.08], 'category': ""})
        self.cdf['date'] = pd.to_datetime(self.cdf['date'])

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("Test class finishes")

    # test casae
    def test_search_date(self): 
        actual = self.p.search_date("11/02/2022")
        # reset the index of dataframe
        actual = actual.reset_index(drop=True)
        assert_frame_equal(actual, self.cdf, check_dtype=False)
        # other way of checking dataframe equality
        #assert actual.equals(self.cdf)
        # no transaction in this date
        self.assertEqual(self.p.search_date("02/02/2022"), None)
        # string passed instead of date
        self.assertEqual(self.p.search_date("date"), None)
        # integer passed insted of date
        self.assertEqual(self.p.search_date(1234), None)

    # test case
    def test_search_amount(self):
        actual = self.p.search_amount(float("11.08"))
        # reset the index of dataframe
        actual = actual.reset_index(drop=True)
        assert_frame_equal(actual, self.cdf, check_dtype=False)
        # string passed instead of amount
        self.assertEqual(self.p.search_amount("11.08"), None)
        # amount not matched with statement records
        self.assertEqual(self.p.search_amount(float("11.18")), None)
        # integer passed instead of float
        self.assertEqual(self.p.search_amount(11), None)

unittest.main(argv=[''], verbosity=2, exit=False)

