
import pandas as pd
import matplotlib.pyplot as plt

# Coffee Exploration Assignment
# Exploratory Data Analysis (EDA)

# =====================================
# PART 1: LOAD THE DATA
# =====================================

export_df = pd.read_csv("Coffee_export-1.csv")
import_df = pd.read_csv("Coffee_import-1.csv")
production_df = pd.read_csv("Coffee_production-1.csv")

print("===== COFFEE EXPORT =====")
print(export_df.head())

print("\n===== COFFEE IMPORT =====")
print(import_df.head())

print("\n===== COFFEE PRODUCTION =====")
print(production_df.head())


# =====================================
# PART 2: EXPLORE THE DATA
# =====================================

datasets = {
    "Coffee Export": export_df,
    "Coffee Import": import_df,
    "Coffee Production": production_df
}

for name, df in datasets.items():

    print(f"\n===== {name} =====")

    # Number of rows and columns
    print("\nRows and Columns:")
    print(df.shape)

    # Column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Dataset information
    print("\nDataset Information:")
    df.info()

    # Unique values
    print("\nUnique Values:")
    for col in df.columns:
        print(col, df[col].nunique())

    # Years and countries
    print("\nYears and Countries:")
    for col in df.columns:
        if "year" in str(col).lower():
            print("Year column:", col)
            print(df[col].dropna().unique())

        if "country" in str(col).lower():
            print("Country column:", col)
            print(df[col].dropna().unique())

    # Check if years are stored as column names
    year_columns = [
        str(col) for col in df.columns
        if str(col).strip().isdigit()
        and len(str(col).strip()) == 4
    ]

    if year_columns:
        print("Years in column names:")
        print(min(year_columns), "to", max(year_columns))


# =====================================
# PART 3: DESCRIPTIVE STATISTICS
# =====================================

for name, df in datasets.items():

    print(f"\n===== {name} STATISTICS =====")

    print("\nDescriptive Statistics:")
    print(df.describe())

    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:

        print("\nMaximum Values:")
        print(numeric_df.max())

        print("\nMinimum Values:")
        print(numeric_df.min())

        print("\nAverage Values:")
        print(numeric_df.mean())

    else:
        print("No numeric columns found.")


# =====================================
# PART 4: DATA QUALITY ASSESSMENT
# =====================================

for name, df in datasets.items():

    print(f"\n===== {name} DATA QUALITY =====")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Total missing values
    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    # Duplicate rows
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    # Check column formatting
    print("\nColumns With Extra Spaces:")
    for col in df.columns:
        if col != col.strip():
            print(col)

    # Check missing percentages
    print("\nMissing Value Percentage:")
    print((df.isnull().sum() / len(df) * 100).round(2))


# =====================================
# PART 5: INITIAL INSIGHTS
# =====================================

print("\n===== INITIAL INSIGHTS =====")

print("""
These datasets can help a global coffee
company understand international coffee
production, imports, and exports.

The company can use this information to
identify major coffee-producing countries,
compare international coffee trade, and
study changes over time.

The results can support decisions about
purchasing, supply chains, and global markets.

After reviewing the data quality results,
the company should address missing values,
duplicate records, and inconsistent formats
before conducting more advanced analysis.
""")

print("\nCoffee Exploration Analysis Complete!")
