import pandas as pd

import analysis.search as s
import analysis.analysis as a

def main():
    while True:
        user_input = input("Choose option: ")
        if user_input == "1":
            statement = pd.read_csv("statement.csv")
            statement['date'] = pd.to_datetime(statement['date'])
            p = s.Search(statement)
            c = p.search_year("2021")
            print(c)

        if user_input == "2":
            j = a.Analysis(statement, "02/11/2022", "26/11/2022")
            print(j.income_expense_ratio_range(1000))

        if user_input == "exit":
            break

if __name__ == '__main__':
    main()