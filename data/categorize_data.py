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
    try:
        name_or_row = input('Would you like to categorize a specific transaction name or a specific row (t/r): ')
        if name_or_row == 't':
            # update the category in the dataframe
            # update dict_cat_shop shop_name : new category
            user_shop_name = input('What transaction name would you like to categorize? ').upper()
            if df['shop_name'].str.contains(user_shop_name).any():
                print('We have a match')
                df_contains = df[df['shop_name'].str.contains(user_shop_name)]
                print(df_contains)
                confirm = input("Confirm selection for categorizing (y/n): ")
                if confirm == 'y':
                    print(catlist)
                    i = int(input("Enter the category: ", ))
                    print(f'Updating the category to {catlist.get(i)}')
                    for index, row in df_contains.iterrows():
                        df.loc[index, 'category'] = catlist.get(i) # index is same as main dataframe
                        dict_cat_shop[df.loc[index, 'shop_name']] = catlist.get(i) # in case that str.contains shows items with diff names
                else:
                    print("Categorizing cancelled")
            else:
                print('No match')
        elif name_or_row == 'r':
            # update the category in the dataframe
            # does not update the dictionary shop_name
            user_show = input("Would you like to see the dataframe (y/n): ")
            if user_show == 'y':
                print(df)
            user_row = int(input("Which row would you like to categorize (input number): "))
            print(df.loc[[user_row]])
            confirm = input("Confirm selection for categorizing (y/n): ")
            if confirm == 'y':
                print(catlist)
                i = int(input("Enter the category: ", ))
                print(f'Updating the category of line {user_row} to {catlist.get(i)}')
                df.loc[user_row, 'category'] = catlist.get(i)
            else:
                print("Categorizing cancelled")
        else:
            print('Please input t (transaction name) or r (row number). Edit cancelled.')
    except Exception as e:
                print(e)

def update_category(self):

    # if category was 'grocery', update to 'groceries' ; actually changing the dictionary ?
    # change in dictionary
    # update in dataframe
    print("update category")

def delete_category(self): 
    # delete from dictionary
    # update in dataframe: [if not in dictionary then set null somewhere earlier]
    # if categroy was 'grocery', make column cell null
    print("delete category")

