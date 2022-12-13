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


def categorize_all(df, catlist, dict_cat_shop):
    print(catlist)
    for index, row in df.iterrows():
        if df.loc[index, 'category'] == '':
            if df.loc[index, 'shop_name'] in dict_cat_shop:
                df.loc[index, 'category'] = dict_cat_shop.get(df.loc[index, 'shop_name'])
            else:
                print(row['date'], row['shop_name'], row['amount'], row['category'])
                i = int(input("Enter the category: ", ))
                df.loc[index, 'category'] = catlist.get(i)
                dict_cat_shop[df.loc[index, 'shop_name']] = catlist.get(i)
    #print(dict_cat_shop)

def categorize_item(df, catlist, dict_cat_shop):
    name_or_row = input('Would you like to categorize a specific transaction name or a specific row (t/r): ')
    if name_or_row == 't':
        in_shop_name = input('What transaction name would you like to categorize? ')
        if df['shop_name'].str.contains(in_shop_name).any():
            print('We have a match')
        else:
            print('No match')
    elif name_or_row == 'r':
        print(name_or_row)
    else:
        print('Please input t or r. Edit cancelled.')
    # for a specific shop item name, change its category: in key(shop_name):value(category), easy enough
    # or for a specific row: change in dataframe only
    # if name / row is equal to user input, then change to category input
    print("categorize item")

def update_category(self):

    # if category was 'grocery', update to 'groceries' ; actually changing the dictionary ?
    print("update category")

def delete_category(self): 
    # if categroy was 'grocery', make column cell null
    print("delete category")

