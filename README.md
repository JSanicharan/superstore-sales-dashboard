# Superstore Sales Dashboard

An interactive data analytics dashboard built with **Python**, **Pandas**, and **Streamlit** to analyze sales performance, profitability, and trends within a Superstore dataset. This project demonstrates a complete analytics workflow, from data cleaning and feature engineering to aggregation and interactive visualization.

---

## Project Overview

This dashboard allows users to explore Superstore sales data across multiple years and business dimensions. Users can dynamically analyze monthly trends, category performance, and top-performing sub-categories while switching between key metrics such as **Sales, Quantity, Discount, and Profit Margin**.

The goal of this project is to showcase practical data analytics skills and the ability to communicate insights through interactive visualizations.

---

## Features

- **Year Filter**
  - Analyze performance for any year in the dataset

- **Monthly Sales & Profit Trends**
  - Line chart displaying monthly Sales and Profit for the selected year

- **Category-Level Analysis**
  - Bar chart showing total Sales by Category (Technology, Furniture, Office Supplies)

- **Top Sub-Category Analysis**
  - Top 10 Sub-Categories dynamically ranked by:
    - Sales
    - Quantity
    - Discount
    - Profit Margin
  - Metric selection controlled via the sidebar

- **Profitability Analysis**
  - Profit Margin calculated at the transaction level and aggregated by sub-category

- **Clean & Modular Code**
  - Separate data cleaning and dashboard logic
  - Cached data loading for improved performance

---

## Key Insights (Example)

- Technology consistently generates the highest total sales across most years.
- Some high-revenue sub-categories exhibit low profit margins, highlighting pricing and discount inefficiencies.
- Certain lower-volume sub-categories maintain strong profit margins, indicating optimization opportunities.
- Discount-heavy sub-categories often show reduced profitability.

*(Insights vary depending on the selected year and metric.)*

---

## Tech Stack

**Stack:** Python for data analysis and processing | Pandas and NumPy for data cleaning, aggregation, and feature engineering | Streamlit for interactive dashboard development and visualization | CSV-based dataset | Virtual environment and dependency management via `venv` and `requirements.txt`

---

## Project Structure

SuperstoreDashboard/
│
├── data/
│ └── Sample - Superstore.csv
│
├── data_cleaning.py # Data loading, cleaning, and feature engineering
├── dashboard.py # Streamlit dashboard application
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md

---

## Installation & Setup

1. Clone the repository:
git clone https://github.com/yourusername/SuperstoreDashboard.git
cd SuperstoreDashboard

**Create a virtual environment:**
    python -m venv venv

**Activate the virtual environment:**
Mac/Linux:
    source venv/bin/activate

Windows (PowerShell):
    .\venv\Scripts\Activate.ps1

**Install dependencies:**
    pip install -r requirements.txt

**Running the Dashboard**

**Run the Streamlit application:**
    streamlit run dashboard.py
**The dashboard will open in your browser at:**
    http://localhost:8501

## Skills Demonstrated

- Data Cleaning & Preparation  
- Feature Engineering (time-based features, profit margin calculation)  
- Data Aggregation & Grouping  
- Exploratory Data Analysis (EDA)  
- Interactive Dashboard Development (Streamlit)  
- Data Visualization & Business Insight Communication  
- Python Project Structuring  
- Git & GitHub Best Practices  

---

## Dataset

The project uses the **Superstore Sales Dataset** in CSV format.

### Dataset Includes:
- Sales  
- Profit  
- Quantity  
- Discount  
- Category and Sub-Category  
- Order Date and Ship Date  

---

## Future Enhancements

Planned improvements to expand analytical depth and usability:

- Profit margin trends by category and sub-category  
- Discount vs. profit impact analysis  
- Ability to export filtered data as CSV  
- Deployment to Streamlit Community Cloud  

---

## License

This project is **open-source** and intended for **educational and portfolio use**.
