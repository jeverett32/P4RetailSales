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
<<<<<<< Updated upstream
    
    
=======
#Gets input on what number they want to see
    selected_category = input("\nEnter the category number to view the sales summary: ")
    #Makes sure it is converted to an interger. 
    selected_category = int(selected_category)  # Convert input to an integer

    # Ensure the category exists
    if selected_category > 0 and selected_category <= category_counter:
        # Get the name of the selected category
        category_name = the_categories[selected_category - 1]

        # Filter the DataFrame to show only the selected category's data
        df_filtered = df[df["category"] == category_name]

        # Calculate the sum of total sales (total_price), average sale amount (total_price), and total units sold (quantity_sold)
        total_sales = df_filtered["total_price"].sum()
        avg_sale_amount = df_filtered["total_price"].mean()
        total_units_sold = df_filtered["quantity_sold"].sum()

        # Display the results
        print(f"\nSales Summary for {category_name}:")
        print(f"Total Sales: ${total_sales:,.2f}")
        print(f"Average Sale Amount: ${avg_sale_amount:,.2f}")
        print(f"Total Units Sold: {total_units_sold}")

    else:
        print("Invalid category number. Exiting the summary section.")
    
    # step 5 - display bad chart 
    dfProductSales = df_filtered.groupby('product')['total_price'].sum()
    dfProductSales.plot(kind='bar') 
    plot.title(f"Total Sales in {selected_category}")
    plot.xlabel('Product')
    plot.ylabel('Total Sales')
    plot.show()
>>>>>>> Stashed changes
