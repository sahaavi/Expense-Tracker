import store_data as sd
import pandas as pd
# catlist = {1:"groceries", 2:"dining out", 3:"household", 4:"clothing", 5:"misc"}
# dictionary with shop_name and category
# key: shop_name, value: category
### key: category, values: list of shop_name
# list of defined shop_names
# if shop_name is in the list of defined shop_names
# then set category of shop_name as key

# algorithm: search through lines without a category
# if the shop_name is in the list of defined, then set the category as the value from key
# else (if shop_name not in list of defined), then prompt user for category, 
# and add shop_name in defined and in dictionary with new key and value as category

def categorize_all(df, catlist):
    print(catlist) 
    for index, row in df.iterrows():
        if df.loc[index, 'category'] == '':
            print(row['date'], row['shop_name'], row['amount'], row['category'])
            i = int(input("Enter the category: ", ))
            df.loc[index, 'category'] = catlist.get(i)

def categorize_item(self):
    print("categorize item")

def update_category(self):
    print("update category")

def delete_category(self): 
    print("delete category")

#OR

"""#from store_data import Expenses
import store_data as sd

class Categorize(sd.Expenses):

    catlist = ["groceries", "dining out","household", "clothing",]

    def print_df(self):
        sd.Expenses.show_expenses()  

    def categorize_all(self):
        sd.Expenses.show_expenses()
        print("categorize all")

    def categorize_item(self):
        print("categorize item")

    def update_category(self):
        print("update category")

    def delete_category(self): 
        print("delete category")"""