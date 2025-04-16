# John Everett, Meagan Brown, Aeysha Entrikin, Kiera Fisher, Zaniel Murdock, Will Francom

# Section 002

# Description: Transfer data into a postgres database and read data programmatically back from the database

# Import necessary libraries 
import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot

# Connect to database
username = 'postgres'
password = '' # ENTER PASSWORD TO TEST!! 
host = 'localhost'
port = '5432'
database = 'is303'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# read file 
df = pd.read_excel("Retail_Sales_Data.xlsx")

# PART 1
seguir = True 
while seguir:
    # ask user for input 
    iUserInput = int(input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))
    if iUserInput == 1 :
        # Split the name column into first and last name and delete old name column
        df[['first_name', 'last_name']] = df['name'].str.split('_', expand=True)
        df = df.drop(columns=['name'])

        # Product category map
        productCategoriesDict = {
            'Camera':'Technology',
            'Laptop':'Technology',
            'Gloves':'Apparel',
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
        df['category'] = df['product'].map(productCategoriesDict)

        # upload to database
        df.to_sql('sale', con=engine, if_exists='replace', index=False)

        # Inform user of success
        print("You've imported the excel file into your postgres database.")

    elif iUserInput == 2:
        # connect to new and updated table 
        df = pd.read_sql_table('sale', con=engine)

        # Print the statement
        print("The following are all the categories that have been sold: ")
            
        # The counter to go up, as well as the list of categories already printed
        category_counter = 0
        the_categories = []
            
        # Looping through each row, checking if the category has been printed, if not, then we print and update the counter
        for category in df["category"]:
            if category not in the_categories:
                category_counter += 1
                the_categories.append(category)
                print(f" {category_counter}: {category}")
        #Gets input on what number they want to see
        selected_category = input("\nEnter the category number to view the sales summary: ")
        #Makes sure it is converted to an interger. 
        selected_category = int(selected_category) 

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
        
        # step 5 - display bar chart 
        dfProductSales = df_filtered.groupby('product')['total_price'].sum()
        # make it a bar chart 
        dfProductSales.plot(kind='bar') 
        # add labels 
        plot.title(f"Total Sales in {category_name}")
        plot.xlabel('Product')
        plot.ylabel('Total Sales')
        # show the dang plot 
        plot.show()
    else: 
        print("Closing the program.")
        seguir = False
        # ^^ stops the loop 