from datetime import datetime as dtime

class Search(object):

    def __init__(self, df):
        self.statement = df
        
    def search_date(self, date):
        matched_date = self.statement.loc[self.statement['date'] == date]
        return matched_date       

    def search_range(self, start_date, end_date):
        if(dtime.strptime(start_date, "%d/%m/%Y") < dtime.strptime(end_date, "%d/%m/%Y")):
            matched_date = self.statement.loc[self.statement['date'].between(start_date, end_date)]
            return matched_date
        else:
            return f"Starting date is bigger than ending date!"

    #def search_month(self, month):

    def search_category(self, cname):
        matched_cat = self.statement.loc[self.statement['category'] == cname]
        return matched_cat

    def search_category(self, cname, start_date, end_date):
        filtered_statement = self.statement.loc[self.statement['date'].between(start_date, end_date)]
        matched_cat = filtered_statement.loc[filtered_statement["category"] == cname]
        return matched_cat

    def search_amount(self, amount):
        matched_amt = self.statement.loc[self.statement['amount'] == amount]
        return matched_amt

    def search_amount(self, amount, start_date, end_date):
        filtered_statement = self.statement.loc[self.statement['date'].between(start_date, end_date)]
        matched_amt = filtered_statement.loc[filtered_statement['amount'] == amount]
        return matched_amt
