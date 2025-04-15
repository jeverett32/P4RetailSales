# OKAY THIS WORKS!! 
# this is just my work - feel free to pull anything but watch variable names 

# import libraries 
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plot

# choice input 
Choice = int(input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))

# dictionary 
productCategories = {
    'Camera': 'Technology',
    'Laptop': 'Technology',
    'Gloves': 'Apparel',
    'Smartphone':'Technology',
    'Watch':'Accessories',
    'Backpack':'Accessories',
    'Water Bottle': 'Household Items',
    'T-shirt': 'Apparel',
    'Notebook': 'Stationary',
    'Sneakers': 'Apparel',
    'Dress': 'Apparel',
    'Scarf':'Apparel',
    'Pen': 'Stationary',
    'Jeans': 'Apparel',
    'Desk Lamp': 'Household Items',
    'Umbrella':'Accessories',
    'Sunglasses':'Accessories',
    'Hat':'Apparel',
    'Headphones': 'Technology',
    'Charger':'Technology'
}

username = 'postgres'
password = 'Smurf0823'
host = 'localhost'
port = 5432
database = 'is303'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

if Choice ==1:
    # step 1 - read file via pandas
    file = pd.read_excel("Retail_Sales_Data.xlsx")

    #step 2- update name column to separate first and last names 
    name_col_idx = file.columns.get_loc('name')
    file[["first_name", "last_name"]] = file["name"].str.split("_", expand=True)
    file.drop(columns=['name'], inplace=True)
    file.insert(name_col_idx, 'first_name', file.pop('first_name'))
    file.insert(name_col_idx + 1, 'last_name', file.pop('last_name'))

    # step 3 - update category 
    file['category'] = file["product"].map(productCategories)

    # step 4 - save results as file in PGadmin 
    file.to_sql('sale',con=engine, if_exists='replace', index = False)

    # step 5 - print completetion statement 
    print("You've imported the excel file into your postres database.")

elif Choice ==2:
# step 1 print statement 
    print("The following are all the categories that have been sold:")
# step 2 print categories w number before it 
    dfImported = pd.read_sql_query("SELECT * FROM sale", engine)
    catVals = dfImported["category"].unique()
    num = 1
    for each in catVals:
        print(f"{num}. {each}")
        num += 1

# step 3 print which category to see 
    ToView = int(input("Please enter the number of the category you want to see summarized: "))
    CatDict = {1:"Technology", 
            2: "Apparel", 
            4: "Household Items",
            3: "Accessories",
            5: "Stationary",
        }
    categoryChoice = CatDict[ToView]
    dfFiltered = dfImported[dfImported['category'] == categoryChoice]
     

# step 4 calculate and display the sum of total sales, the average sale amount, and the total units sold
    sumOfSales = dfFiltered['total_price'].sum()
    avgSale = dfFiltered['total_price'].mean()
    totalUnits = dfFiltered['quantity_sold'].sum()

    print(f"Total sales for {categoryChoice}: {(sumOfSales):.2f}")
    print(f"Average sale amount for {categoryChoice}: {(avgSale):.2f}")
    print(f"Total units sold for {categoryChoice}: {(totalUnits)}")

# step 5 - display bad chart 
    dfProductSales = dfFiltered.groupby('product')['total_price'].sum()
    dfProductSales.plot(kind='bar') 
    plot.title(f"Total Sales in {categoryChoice}")
    plot.xlabel('Product')
    plot.ylabel('Total Sales')
    plot.show()

else: print("Closing program. Goodbye!")