import pandas as pd

class Search(object):

    def __init__(self, df):
        self.statement = df

    def search_category(self, cname):
        #print(self.statement.head())
        matched_cat = self.statement.loc[self.statement['category'] == cname]
        return matched_cat


statement = pd.read_csv("analysis/statement.csv")
cname_u = input("Enter the category name: ")
p = Search(statement)
p.search_category("grocery")