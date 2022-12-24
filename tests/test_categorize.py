import sys
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis")
sys.path.append("e:\\Study\\UBC\\Block 3\\DATA 533 Collaborative Software Development\\Project\\Expense-Tracker-and-Analysis\\expta")
sys.path.append('/home/travis/build/sahaavi/Expense-Tracker-and-Analysis/')
sys.path.append('/home/travis/build/sahaavi/Expense-Tracker-and-Analysis/expta')

import unittest
import expta.data.store_data as sd
import expta.data.categorize_data as cd

class TestCategorize(unittest.TestCase):
    
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
        cls.df_e2 = sd.add_expenses("11/01/2022", "otherstuff", 543.22, 5)

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
    def test_update_category(self):
        cd.update_category(self.df_e2, 5, "other")
        self.assertIn("other", cd.catlist.values())
        self.assertNotIn("misc", cd.catlist.values())
        self.assertIn("other", [i for i in self.df_e2['category']])
        self.assertNotIn("misc", [i for i in self.df_e2['category']])
        #self.assertIn("other", cd.dict_cat_shop.values()) 
        #[this doesn't work b/c my add_expense doesn't add to dict_catshop, only add_csv does]

    def test_add_category(self):
        cd.add_category("more food")
        self.assertEqual(len(cd.catlist), 6) # checking length
        self.assertIn("more food", cd.catlist.values()) # checking the new name is in the catlist
        cd.add_category(self.df_e2)
        self.assertEqual(len(cd.catlist), 6) #assert that adding a dataframe instead of string will not add it
        self.assertNotIn("more food",[i for i in self.df_e2['category']]) #assert the new category is not yet used in dataframe
        cd.add_category("groceries")
        self.assertEqual(len(cd.catlist), 6) # assert that can't add a category that already exists

unittest.main(argv=[''], verbosity=2, exit=False)

