# John Everett, Meagan Brown, Aeysha Entrikin, Kiera Fisher, Zaniel Murdock, Will Francom

# Section 002

# Description: Transfer data into a postgres database and read data programmatically back from the database

# Import necessary libraries
import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

# Optional libraries
import openpyxl
from sqlalchemy.sql import text
import psycopg2

# Program will ask the user what they want to do
iUserInput = int(input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))

if iUserInput == 1 :
    dfRaw = pd.read_excel("Retail_Sales_Data.xlsx")


if iUserInput == 2:
    #Print
    print("The following are all the categories that have been sold:"
    # the counter to go up, as well as the list of categories already printed
    category_counter = 0
    the_categories = []
    #looping through each row, checking if the category has been printed, if not, then we print and update the counter
    for category in df["Category"]:
        if category not in the_categories:
            category_counter += 1
            the_categories.append(category)
            print(f" {category_counter}: {category}"
    
    
