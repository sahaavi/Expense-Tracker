from timerange import TimeRange as tr

class Search(object):

    def __init__(self, df):
        self.statement = df
        
    def search_category(self, cname):
        matched_cat = self.statement.loc[self.statement['category'] == cname]
        return matched_cat

    def search_cateegory(self, cname, start_date, end_date):
        filtered_statement = tr.getrange(slef.statement, start_date, end_date)
        matched_cat = filtered_statement.loc[filtered_statement["category"] == cname]
        return matched_cat

    def search_amount(self, amount):
        matched_amt = self.statement.loc[self.statement['amount'] == amount]
        return matched_amt
