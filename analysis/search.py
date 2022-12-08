import pandas as pd

class Search(object):

    def __init__(self, df):
        self.statement = df

    def search_category(self, cname):
        print(self.statement.head())
        return self.statement.head()


statement = pd.read_csv("analysis/statement.csv")
p = Search(statement)
p.search_category("sd")