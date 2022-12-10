class TimeRange(object):

    def __init__(self, df, start_date, end_date):
        self.statement = df 
        self.start_date = start_date
        self.end_date = end_date

    def getrange(self):
        # Select DataFrame Rows between two dates
        mask = (self.statement['date'] > start_date) & (self.statement['date'] <= end_date)
        filtered_statement = self.statement.loc[mask]
        return filtered_statement