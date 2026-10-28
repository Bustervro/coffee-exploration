import pandas as pd

# Part 1: Load the datasets
export_df = pd.read_csv("Coffee_export.csv")
import_df = pd.read_csv("Coffee_import.csv")
production_df = pd.read_csv("Coffee_production.csv")

datasets = {
    "Coffee Export": export_df,
    "Coffee Import": import_df,
    "Coffee Production": production_df
}

# Part 1: Display first five rows
for name, df in datasets.items():
    print(f"\n===== {name} =====")
    print(df.head())

# Part 2: Explore the data
for name, df in datasets.items():
    print(f"\n===== {name} =====")

    print("Rows and Columns:", df.shape)
    print("Column Names:", df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDataset Information:")
    df.info()

    print("\nYear and Country Information:")
    for col in df.columns:
        if "year" in str(col).lower():
            print(col, df[col].dropna().unique())
        if "country" in str(col).lower():
            print(col, df[col].dropna().unique())

# Part 3: Descriptive Statistics
for name, df in datasets.items():
    print(f"\n===== {name} =====")

    print(df.describe())

    numeric_df = df.select_dtypes(include="number")

    print("\nMaximum:")
    print(numeric_df.max())

    print("\nMinimum:")
    print(numeric_df.min())

    print("\nAverage:")
    print(numeric_df.mean())

# Part 4: Data Quality
for name, df in datasets.items():
    print(f"\n===== {name} =====")

    print("Missing Values:")
    print(df.isnull().sum())

    print("Duplicate Rows:", df.duplicated().sum())

    print("Data Types:")
    print(df.dtypes)
