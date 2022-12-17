import pandas as pd
from datetime import datetime
import data.categorize_data as cd
from numpy import nan 

catlist = cd.catlist

colnames = ["date", "shop_name", "amount", "category"]
newdf = pd.DataFrame(columns=colnames)

"""def __init__(self, maindf = newdf, colnames = colnames):
    self.maindf = maindf
    self.colnames = colnames"""

"""def convert_to_df(self):
    return self.maindf"""

def add_csv(filename, df = newdf):
    #try: 
    #filename = input("Enter csv file name to add: ")
    print("File to add is: " + filename)
    userdf = pd.read_csv(filename, header=None, usecols=[0, 1, 2])
    userdf['category'] = ''
    userdf.columns = colnames
    userdf = userdf.dropna()
    userdf["date"] = pd.to_datetime(userdf["date"])
    #df = df.append(userdf)
    df = pd.concat([df, userdf], ignore_index=True)
    #except Exception as e:
        #print(e) 
    return df

def add_expenses(user_date, user_shopname, user_amount, user_category,  df = newdf, catlist=catlist):
    try:
        ### user_date = input("Enter the date (MM/DD/YYYY): ")
        ## user_date = "12/01/2022"
        date_format = "%m/%d/%Y"
        user_date = datetime.strptime(user_date, date_format)
        ### user_shopname = input("Enter the transaction name: ").upper()
        ## user_shopname = "rent".upper()
        ### user_amount = float(input("Enter the amount: "))
        ## user_amount = 700
        ## print(catlist)
        ### user_category = catlist.get(int(input("Enter a category: ")))
        ## user_category = catlist.get(5)
        #print(f'Confirm input (y/n): Date: {user_date}, Transaction name: {user_shopname}, Amount: {user_amount}, Category: {user_category}')
        newrow = [user_date, user_shopname, user_amount, user_category]
        #confirm = input("Confirm input (y/n): ")
        ## confirm = "y"
        #if confirm == "y":
        df.loc[len(df)] = newrow
            #print(self.maindf)
        #else:
            #print("input cancelled")
    #except ValueError:
        #print("input cancelled; Please input a numeric value for amount")
    except Exception as e:
        print(e)
    return df
        


"""def show_expenses(self, start = 0, end = None):
    if end == None:
        end = len(self.maindf)
    if len(self.maindf) != 0:
        return self.maindf.loc[start:end]
    #else:
        #print("No data yet")"""

def export_expenses(df, newfilename):
    #filename = input("Name the exported file: ")
    export_data = df.to_csv(newfilename)
    return export_data

def delete_expenses(df, whichrow):
    #try:
        #whichrow = int(input("Which row number you would like to delete: "))
        #confirm = input(f'Confirm delete row {whichrow} (y/n): ')
        #if confirm == "y":
    df = df.drop(whichrow)
    df = df.reset_index()
        #else:
            #print("deletion cancelled")#
    #except Exception as e:
        #print(e)
    return df







