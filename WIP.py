# this is what i have so far !! 


# import libraries 
import pandas as pd
from sqlalchemy import create_engine

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
    'Sunglasases':'Accessories',
    'Hat':'Apparel',
    'Headphones': 'Technology',
    'Charger':'Tehcnology'
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
    names = file["name"].str.split("_", expand = True)

# step 3 - update category 
    file['category'] = file["category"].map(productCategories, inplace = True)

# step 4 - save results as file in PGadmin 
    file.to_sql('sale',con=engine, if_exists='replace', index = False)

# step 5 - print completetion statement 
    print("You've imported the excel ile into your postres database.")

elif Choice ==2:
# step 1 print statement 
    print("The following are all the categories that have been sold:")
# step 2 print categories w number before it 
    categories = pd.read_sql_query("SELECT category FROM sale", engine)
    num = 1
    diffCats = []
    diffCats.append(categories['category'].unique())
    for cat in diffCats:
        print(f"{num}. {cat}")
        num += 1

# step 3 print which category to see 
    view = int(input("Please enter the number of the category you want to see summarized: "))
    realView = view-1

# step 4 calculate and display the sum of total sales, the average sale amount, and the total units sold
    pd.read_sql_query(f"SELECT {diffCats[realView]} FROM sale", engine)




    print("Please enter the number")



else: print("Closing program. Goodbye!")