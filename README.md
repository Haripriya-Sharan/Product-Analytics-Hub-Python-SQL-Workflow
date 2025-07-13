# Product-Analytics-Hub-Python-SQL-Workflow

A complete data analysis project for exploring and summarizing product pricing, discounts, and ratings using Python (pandas) and SQL (MySQL). This project combines data from multiple CSV files, performs cleaning and transformation in Python, and enables advanced querying and insights via SQL.


## Overview

This project demonstrates a typical data pipeline:
- Importing product data (Headphones, Cameras) from CSV files using pandas.
- Cleaning, merging, and transforming the data (handling missing values, formatting prices, binning ratings).
- Uploading the processed data to a MySQL database.
- Writing and executing SQL queries to extract business insights, such as price statistics, discount leaders, and top-rated products.

## Features

- **Data Cleaning & Transformation:** Handles missing values, removes duplicates, formats price fields, and bins ratings.
- **Flexible Data Import:** Easily combine multiple CSVs into a single DataFrame.
- **MySQL Integration:** Uploads the cleaned data to a MySQL table for further analysis.
- **SQL Analytics:** Includes a suite of SQL queries for descriptive statistics, top-N analysis, and category-based insights.
- **Reproducible Workflow:** All steps are scripted for repeatability and transparency.

## Project Structure

```
product-price-analysis/
│
├── python_sql_project.py   # Python script for data cleaning & upload
├── python_sql_project.sql  # SQL queries for analysis
├── Headphones.csv          # Raw data: Headphones
├── Cameras.csv             # Raw data: Cameras
├── combined.csv            # Cleaned, merged dataset
└── README.md               # Project documentation
```

## Data Preparation (Python)

Key steps performed in the Python script:

- **Read CSV files** for each product category.
- **Concatenate** datasets into a single DataFrame.
- **Clean columns:** Remove unwanted columns, rename for clarity.
- **Format prices:** Remove currency symbols and commas, convert to numeric.
- **Handle ratings:** Fill missing values, bin ratings into categories (Low, Medium, High).
- **Calculate discounts:** Add a column for discount percentage.
- **Remove duplicates** and invalid rows.
- **Export cleaned data** to a new CSV and upload to MySQL.

## Database & SQL Analysis

The cleaned data is uploaded to a MySQL database table (`df_project`). The included SQL script provides:

- Table structure and row counts.
- Price statistics (average, min, max) by category.
- Product counts by category.
- Top 10 most expensive products in each category.
- Products with the highest discounts.
- Top-rated products (with at least 100 reviews).
- Product counts by rating bin.
- Top 10 "High" rated products below average price, by category.

## How to Use

### 1. Prepare the Environment

- Install Python (3.7+ recommended)
- Install required Python packages:
  ```bash
  pip install pandas sqlalchemy pymysql mysql-connector-python
  ```

### 2. Place Data Files

- Add your `Headphones.csv` and `Cameras.csv` files to the project folder.

### 3. Run the Python Script

- Update file paths and MySQL credentials as needed in `python_sql_project.py`.
- Execute:
  ```bash
  python python_sql_project.py
  ```
- This will create a `combined.csv` and upload the data to your MySQL database.

### 4. Run SQL Queries

- Open your MySQL client.
- Execute the queries in `python_sql_project.sql` to analyze the data.

## Requirements

- Python 3.7+
- pandas, sqlalchemy, pymysql, mysql-connector-python
- MySQL Server (local or remote)

