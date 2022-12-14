# Subpackage: `data`

## Overview

`data` sub-package handles all the data related task like importing the csv file, exporting the file, categorize expenses, add new expenses.

## Description

This sub-package contains 2 modules
- `store_data`
- `categorize_data`

`store_data` module is dealing with storing data, adding new data in dataframe, exporting the data as csv, deleting the whole dataframe with functions like `add_expenses()`, `add_csv()`, `delete_expenses`.

`categorize_data` modoule is dealing with categorizing the expenses. User can specifically categorize an expense or all the expenses together, update the category with funcitons like  `categorize_all()`, `categorize_item()`, `update_category()`.

To use the subpackage, you import the desired submodule and call its functions directly. For example:  
```
from store_data import add_csv

filename = "statement.csv"
add_csv(filename)
```
Check `driver.py` for more use cases.