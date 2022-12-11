import pandas as pd
import numpy as np
from datetime import datetime

#df = pd.read_csv("accountactivity.csv", header=None, usecols=[0, 1, 2])
#print(df)

class Expenses:
    colnames = ["date", "shop_name", "amount", "category"]
    newdf = pd.DataFrame(columns=colnames)

    def __init__(self, maindf = newdf, colnames = colnames):
        self.maindf = maindf
        self.colnames = colnames

    def add_expenses(self):
        try:
            user_date = input("Enter the date (MM/DD/YYYY): ")
            date_format = "%m/%d/%Y"
            user_date = datetime.strptime(user_date, date_format)
            user_shopname = input("Enter the transaction name: ")
            user_amount = float(input("Enter the amount: "))
            ## print current list of categories so user can choose from
            user_category = input("Enter a category: ")
            print(f'Confirm input (y/n): Date: {user_date}, Transaction name: {user_shopname}, Amount: {user_amount}, Category: {user_category}')
            newrow = [user_date, user_shopname, user_amount, user_category]
            confirm = input("Confirm input (y/n): ")
            if confirm == "y":
                self.maindf.loc[len(self.maindf)] = newrow
                #print(self.maindf)
            else:
                print("input cancelled")
        except ValueError:
            print("input called; Please input a numeric value for amount")
        except Exception as e:
            print(e)
        

    def add_csv(self):
        try: 
            filename = input("Enter csv file name to add: ")
            print("File to add is: " + filename)
            userdf = pd.read_csv(filename, header=None, usecols=[0, 1, 2])
            userdf['category'] = ''
            userdf.columns = self.colnames
            userdf = userdf.dropna()
            userdf["date"] = pd.to_datetime(userdf["date"])
            self.maindf = self.maindf.append(userdf)
            #print(self.maindf)
        except Exception as e:
            print(e) 

    def show_expenses(self):
        if len(self.maindf) != 0:
            print(self.maindf)
            #print(self.maindf.info())
        else:
            print("No data yet")

    def export_expenses(self):
        filename = input("Name the exported file: ")
        export_data = self.maindf.to_csv(filename)

    def delete_expenses(self):
        self.show_expenses()
        try:
            whichrow = int(input("Which row number you would like to delete: "))
            confirm = input(f'Confirm delete row {whichrow} (y/n): ')
            if confirm == "y":
                self.maindf = self.maindf.drop(whichrow)
            else:
                print("deletion cancelled")
        except Exception as e:
            print(e)

