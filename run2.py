import pandas as pd
import data.store_data as sd
import data.categorize_data as cd
import analysis.search as s
import analysis.analysis as a
#test for auto push

def main():
    base_df = sd.Expenses()
    catlist = {1:"groceries", 2:"dining out", 3:"household", 4:"clothing", 5:"misc"}
    dict_cat_shop = {}
    modulelist = {1: "store expenses", 2: "categorize expenses", 3: "search expenses", 4:"analyse expenses"}
    
    while True:
        print("1. Import/Export the data or add expenses.")
        print("2. Categorize the data")
        print("3. Search")
        print("4. Analysis")
        print("Type exit to exit")
        user_input = input("Choose option: ")

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


        if user_input == "2":
            
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

        if user_input == "exit":
            break

if __name__ == '__main__':
    main()