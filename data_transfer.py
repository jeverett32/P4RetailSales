# John Everett, Meagan Brown, Aeysha Entrikin, Kiera Fisher, Zaniel Murdock, Will Francom

# Section 002

# Description: Transfer data into a postgres database and read data programmatically back from the database

# Import necessary libraries
import sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot

# Optional libraries
import openpyxl
from sqlalchemy.sql import text
import psycopg2

# PART 1
# Program will ask the user what they want to do
iUserInput = int(input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))

# Logic for if the user chooses 1
if iUserInput == 1 :
    # Import excel file
    df = pd.read_excel("Retail_Sales_Data.xlsx")

    # Split the name column into first and last name and delete old name column
    df[['first_name', 'last_name']] = df['name'].str.split('_', expand=True)
    df = df.drop(columns=['name'])

    # Product category map
    productCategoriesDict = {
        'Camera':'Technology',
        'Laptop':'Technology',
        'Gloves':'Clothing',
        'Smartphone':'Technology',
        'Watch':'Accessories',
        'Backpack':'Accessories',
        'Water Bottle': 'Household Items',
        'T-shirt': 'Apparel',
        'Notebook': 'Stationery',
        'Sneakers': 'Apparel',
        'Dress': 'Apparel',
        'Scarf': 'Apparel',
        'Pen': 'Stationery',
        'Jeans': 'Apparel',
        'Desk Lamp': 'Household Items',
        'Umbrella': 'Accessories',
        'Sunglasses': 'Accessories',
        'Hat': 'Apparel',
        'Headphones': 'Technology',
        'Charger': 'Technology'
    }

    # Replace categories with the map
    df['categories'] = df['categories'].map(productCategoriesDict)

    # Save the results to a table called 'sale' in your is303 postgres database !!! HAS NOT BEEN TESTED YET!!!
    username = 'postgres'
    password = ''
    host = 'local'
    port = '5432'
    database = 'is303'

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

    df.to_sql('sales', con=engine, if_exists='replace', index=True)

    # Inform user of success
    print("You've imported the excel file into your postgres database.")
    