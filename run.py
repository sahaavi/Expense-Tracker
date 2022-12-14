import data.store_data as sd
import data.categorize_data as cd
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

        df = base_df.show_expenses()
        if user_input == "1":
            input1 = None
            while input1 != "6":
                print("1: add csv file")
                print("2: add individual expense")
                print("3: show expenses")
                print("4: delete expense")
                print("5: export expenses to csv")
                print("6: exit")
                input1 = input("Choose an option: ")
                if input1 == "1":
                    filename = input("Enter csv file name to add: ")
                    base_df.add_csv(filename)
                elif input1 == "2":
                    user_date = input("Enter the date (MM/DD/YYYY): ")
                    user_shopname = input("Enter the transaction name: ").upper()
                    user_amount = float(input("Enter the amount: "))
                    print(catlist)
                    user_category = catlist.get(int(input("Enter a category: ")))
                    base_df.add_expenses()
                elif input1 == "3":
                    print(base_df.show_expenses())
                elif input1 == "4":
                    print(base_df.show_expenses())
                    whichrow = int(input("Which row number you would like to delete: "))
                    base_df.delete_expenses(whichrow)
                elif input1 == "5":
                    newfilename = input("Name the exported file: ")
                    base_df.export_expenses(newfilename)
                elif input1 == "6":
                    break
                else:
                    print("Input a valid choice (1-6)")

        elif user_input == "2":
            input2 = None
            while input2 != "5":
                print("1: categorize all uncagetorized expenses")
                print("2: categorize specific expense")
                print("3: update a category name")
                print("4: add a category")
                print("5: exit")
                input2 = input("Choose an option: ")
                if input2 == "1":
                    cd.categorize_all(df, catlist, dict_cat_shop)
                elif input2 == "2":
                    cd.categorize_item(df, catlist, dict_cat_shop)
                elif input2 == "3":
                    cd.update_category(df, catlist, dict_cat_shop)
                elif input2 == "4":
                    cd.add_category(catlist)
                elif input2 == "5":
                    break
                else:
                    print("Input a valid choice (1-5)")
                    
        elif user_input == "3":
            while True:
                print("What you want to do?")
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

        elif user_input == "4":
            print("Under maintainance")

        elif user_input == "exit":
            break

if __name__ == '__main__':
    main()
