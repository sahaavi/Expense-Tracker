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
            print(p)

        elif user_input == "2":
            print("nothing")
                    
        elif user_input == "3":
            while True:
                print("1. Search a specific day's transactions")
                print("2. Search transactions from a range of days")
                print("3. Search a month's transactions")
                print("4. Search a year's transactions")
                print("5. Search category")
                print("6. Search category from a range of days")
                print("7. Search amount")
                print("8. Search amount from a range of days")
                print("0. Back to main")
                user_input_s = input("Choose an option: ")
                if user_input_s == "1":
                    date = input("Enter the date (dd/mm/yyyy): ")
                    print(p.search_date(date))
                elif user_input_s == "2":
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_range(start_date, end_date))
                elif user_input_s == "3":
                    month = input("Enter month's number (8 -> Aug): ")
                    print(p.search_month(month))
                elif user_input_s == "4":
                    year = input("Enter year (yyyy): ")
                    print(p.search_year(year))
                elif user_input_s == "5":
                    cname = input("Enter the category name: ")
                    print(p.search_category(cname))
                elif user_input_s == "6":
                    cname = input("Enter the category name: ")
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_category_range(cname, start_date, end_date))
                elif user_input_s == "7":
                    amount = float(input("Enter the amount: "))
                    print(p.search_amount(amount))
                elif user_input_s == "8":
                    amount = float(input("Enter the amount: "))
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_category_range(amount, start_date, end_date))
                elif user_input_s == "0":
                    break
                else:
                    print("Input a valid choice (0-8)")

        elif user_input == "4":
            start_date = input("Enter start date (dd/mm/yyyy): ")
            end_date = input("Enter end date (dd/mm/yyyy): ")
            j = a(statement, start_date, end_date)
            while True:
                print("1. Total Expense")
                print("2. Income Expense Ratio from a range of days")
                print("3. Category Percentage")
                print("4. Category Average")
                print("0. Back to main")
                user_input_s = input("Choose an option: ")
                if user_input_s == "1":
                    print(j.total_expense(statement))
                if user_input_s == "2":
                    income = float(input("Enter the income: "))
                    print(j.income_expense_ratio_range(income))
                elif user_input_s == "3":
                    print(j.category_average())
                elif user_input_s == "4":
                    print(j.category_average())
                elif user_input_s == "0":
                    break
                else:
                    print("Input a valid choice (0-4)")

        elif user_input == "exit":
            break

if __name__ == '__main__':
    main()
