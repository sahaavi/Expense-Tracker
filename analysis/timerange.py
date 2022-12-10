def getrange(df, start_date, end_date):
        # Select DataFrame Rows between two dates
        mask = (df['date'] > start_date) & (df['date'] <= end_date)
        filtered_statement = df.loc[mask]
        return filtered_statement