Investment Fund Data Analysis
Overview
Analysis program for equity fund performance data covering 150 U.S. companies to support portfolio rebalancing decisions.
Requirements

Python 3.8+
pandas
numpy
openpyxl

Installation
bashpip install pandas numpy openpyxl
Usage
bashpython investment_analysis.py
Input File
Place Data Set.xlsx in the same directory as the script.
Output
The program displays:

Duplicate rows identified
Descriptive statistics grouped by state (mean, median, min, max)
Businesses with negative debt-to-equity ratios
Final dataset with calculated debt-to-income ratios

Program Tasks

Imports company financial data from Excel file
Identifies and displays any duplicate entries
Groups data by business state and calculates descriptive statistics
Filters companies with negative debt-to-equity ratios
Calculates debt-to-income ratio (long-term debt ÷ revenue) with zero-division handling
Concatenates results into final comprehensive dataset

Date
October 7, 2025