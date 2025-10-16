
#!/usr/bin/env python3
#coding: utf-8
# Investment Analysis Script
import pandas as pd
import numpy as np

# Import data (McKinney, 2022)
df = pd.read_excel("Data Set.xlsx")

# Identify duplicates
duplicates = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicates)

# Group by state with descriptive statistics (VanderPlas, 2016)
df_stats = df.groupby("Business State").agg(["mean", "median", "min", "max"])
print("\nDescriptive Statistics by State:")
print(df_stats)

# Filter negative debt-to-equity ratios (McKinney, 2022)
df_negative_de = df[df["Debt to Equity"] < 0]
print("\nBusinesses with Negative Debt-to-Equity Ratios:")
print(df_negative_de)

# Create debt-to-income ratio dataframe (VanderPlas, 2016)
# Handle division by zero (Harris et al., 2020)
df_dti = pd.DataFrame()
df_dti["Debt to Income"] = np.where(df["Total Revenue"] == 0, 
                                   np.nan, 
                                   df["Total Long-term Debt"] / df["Total Revenue"])

# Concatenate dataframes (McKinney, 2022)
df_final = pd.concat([df, df_dti], axis=1)
print("\nFinal DataFrame:")
print(df_final)

# References:
# Harris, C. R., Millman, K. J., Van Der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. nature, 585(7825), 357-362. https://www.nature.com/articles/s41586-020-2649-2
# McKinney, W. (2022). Python for data analysis (3rd ed.). O'Reilly Media.
# VanderPlas, J. (2016). Python data science handbook: Essential tools for working with data. " O'Reilly Media, Inc.".
