import pandas as pd

# Load Dataset
file_path = r"C:\Users\ADMIN\Documents\Transformed_Housing_Data2.csv"

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully")
print(df.head())
# ==========================
# Basic Information
# ==========================
print("\nDataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Remove Duplicate Rows
# ==========================
df = df.drop_duplicates()

# ==========================
# Fill Missing Values
# ==========================
for column in df.columns:

    if df[column].dtype == "object":
        df[column] = df[column].fillna(df[column].mode()[0])

    else:
        df[column] = df[column].fillna(df[column].median())

# ==========================
# Convert Date Column (if exists)
# ==========================
possible_dates = ["date", "Date", "SaleDate"]

for col in possible_dates:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col])

        df["Year"] = df[col].dt.year
        df["Month"] = df[col].dt.month_name()

# ==========================
# Create Price per Sq Ft
# ==========================
possible_area = ["Area", "GrLivArea", "LotArea", "SquareFeet"]

for area in possible_area:
    if area in df.columns:

        if "SalePrice" in df.columns:
            df["Price_per_SqFt"] = df["SalePrice"] / df[area]

        elif "Price" in df.columns:
            df["Price_per_SqFt"] = df["Price"] / df[area]

        break

# ==========================
# Save Cleaned Dataset
# ==========================
output_file = "Housing_Cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print(f"Cleaned file saved as: {output_file}")