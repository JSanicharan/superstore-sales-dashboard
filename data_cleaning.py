import pandas as pd
def load_data():
    df = pd.read_csv("Data/Sample - Superstore.csv", encoding= "Latin 1")
    
    return df

def data_cleaning(df):
    #Clean sales and profit by dropping empty values#
    df=df.dropna(subset=['Sales', 'Profit'])
    #Ensuring Profit and sales are numbers#
    df['Profit'] = df['Profit'].astype(float)
    df['Sales'] = df['Sales'].astype(float)
    #Convert order date to datetime#
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    return df

def create_columns(df):
    #Create year month and quarter columns#
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Quarter'] = df['Order Date'].dt.quarter

    #Create profit margin Column#
    df['Profit Margin'] = df['Profit'] / df['Sales']

    return df


def aggregate_data(df):
    monthly_sales=df.groupby(["Year", "Month"])[["Sales", "Profit"]].sum().reset_index()
    return monthly_sales

def aggregate_by_data(df):
    sales_by_category = (df.groupby('Category')[["Sales", 'Profit']].sum().sort_values(by="Sales", ascending = False).reset_index())
    sales_by_subcategory =(df.groupby(["Category", "Sub-Category"])[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending = False).reset_index())

    return sales_by_category, sales_by_subcategory

def main():
    df = load_data()
    df = data_cleaning(df)
    df = create_columns(df)
    monthly_sales = aggregate_data(df)
    category_summary,subcategory_summary = aggregate_by_data(df)

    print(df.columns)
    print(" Data loaded and cleaned successfully!")
    print("\nMonthly Summary:\n", monthly_sales)
    print("\nCategory Summary:\n", category_summary)
    print("\nSub-Category Summary:\n", subcategory_summary.head())

if __name__ == "__main__":
    main()