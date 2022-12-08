import pandas as pd

class Search(object):

    def __init__(self, df):
        self.statement = df

    def search_category(self, cname):
        return pd.head(self.df)


statement = pd.read_csv("statement.csv")
p = Search(statement)