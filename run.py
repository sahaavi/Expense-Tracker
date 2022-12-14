import pandas as pd

from analysis.search import Search as s
from analysis.analysis import Analysis as a

def main():
    while True:
        print("1. Import/Export the data or add expenses.")
        print("2. Categorize the data")
        print("3. Search")
        print("4. Analysis")
        print("Type exit to exit")
        user_input = input("Choose an option: ")

        if user_input == "1":
            statement = pd.read_csv("statement.csv")
            statement['date'] = pd.to_datetime(statement['date'])
            p = s(statement)

        elif user_input == "2":
            j = a(statement, "02/11/2022", "26/11/2022")
            print(j.income_expense_ratio_range(1000))

        elif user_input == "3":
            print("What you want to do?")
            print("1. Search a specific day's transactions")
            print("2. Search transactions from a range of days")
            print("3. Search a month's transactions")
            print("4. Search a year's transactions")
            print("5. Search category")
            print("6. Search category from a range of days")
            print("7. Search amount")
            print("8. Search amount from a range of days")
            user_input_s = input("Choose an option: ")
            if user_input_s == "1":
                 date = input("Enter the date (dd/mm/yyyy): ")
                 print(p.search_date(date))
            elif user_input == "2":
                print(2)

        elif user_input == "3":
            print("Under maintainance")

        elif user_input == "exit":
            break

if __name__ == '__main__':
    main()