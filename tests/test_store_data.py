import sys
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis")
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis\\expta")
sys.path.append('/home/travis/build/sahaavi/Expense-Tracker-and-Analysis/')
sys.path.append('/home/travis/build/sahaavi/Expense-Tracker-and-Analysis/expta')

import unittest
import expta.data.store_data as sd

class TestStoreData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Test class starts")
        cls.filename = "statement.csv"
        cls.df_c = sd.add_csv(cls.filename)
        cls.user_date = "12/01/2022"
        cls.user_shopname = "rent"
        cls.user_amount = 700
        cls.user_category = 5
        cls.df_e = sd.add_expenses(cls.user_date, cls.user_shopname, cls.user_amount, cls.user_category)

    # setting up for test
    def setUp(self):
        print("Test Setup")
        

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("Test class finishes")

    # test case
    def test_add_csv(self):
        self.assertEqual(len(sd.add_csv(self.filename)), 7) # add csv to empty
        self.assertEqual(len(sd.add_csv(self.filename, self.df_e)), 8) # add csv to dataframe from one add_expense
        self.assertEqual(len(sd.add_csv(self.filename, self.df_c)), 14) # add csv to dataframe from add_csv
        self.assertEqual(sd.add_csv(self.filename, "fake_df"), None) # try to add csv to not a dataframe
        
    def test_add_expenses(self):
        self.assertEqual(len(sd.add_expenses("03/12/2022", "rent", 700, 5, self.df_c)), 8)
        self.assertEqual(len(sd.add_expenses("03/12/2022", "rent", 700, 5)), 1)
        self.assertEqual(sd.add_expenses("99/12/2022", "rent", 700, 5), None)
        self.assertEqual(sd.add_expenses("03/12/2022", "rent", "sevenhundred", 5), None)

        

unittest.main(argv=[''], verbosity=2, exit=False)

