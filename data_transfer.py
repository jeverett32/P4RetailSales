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
    
    