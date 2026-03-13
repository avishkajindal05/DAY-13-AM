import pandas as pd

data = {
    "name": [
        "Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet",
        "T-shirt", "Jeans", "Jacket", "Sneakers", "Cap",
        "Novel", "Cookbook", "Notebook", "Dictionary", "Comics",
        "Blender", "Microwave", "Vacuum Cleaner", "Coffee Maker", "Lamp",
        "Gaming Console", "Monitor", "Keyboard", "Mouse"
    ],
    "category": [
        "Electronics","Electronics","Electronics","Electronics","Electronics",
        "Clothing","Clothing","Clothing","Clothing","Clothing",
        "Books","Books","Books","Books","Books",
        "Home","Home","Home","Home","Home",
        "Electronics","Electronics","Electronics","Electronics"
    ],
    "price": [
        65000, 30000, 2500, 8000, 20000,
        500, 1500, 3500, 4000, 300,
        400, 700, 120, 900, 250,
        2500, 8000, 12000, 3500, 900,
        45000, 15000, 1200, 800
    ],
    "stock": [
        10, 25, 40, 15, 12,
        100, 60, 30, 45, 80,
        120, 50, 200, 70, 90,
        35, 20, 15, 25, 60,
        8, 14, 55, 75
    ],
    "rating": [
        4.6, 4.4, 4.2, 4.1, 4.3,
        4.0, 3.8, 4.2, 4.1, 3.9,
        4.5, 4.3, 4.0, 4.2, 4.4,
        4.1, 4.3, 4.5, 4.0, 4.2,
        4.7, 4.4, 4.1, 4.0
    ],
    "num_reviews": [
        320, 500, 150, 210, 180,
        95, 70, 60, 110, 50,
        140, 120, 30, 65, 85,
        75, 90, 130, 105, 40,
        420, 210, 160, 180
    ]
}

df = pd.DataFrame(data)

print("\nFIRST 5 MINUTES CHECKLIST ")

print("\n1️⃣ Head of DataFrame")
print(df.head())

print("\n2️⃣ DataFrame Shape")
print(df.shape)

print("\n3️⃣ Data Types")
print(df.dtypes)

print("\n4️⃣ Missing Values")
print(df.isnull().sum())

print("\n5️⃣ Summary Statistics")
print(df.describe())

print("\n6️⃣ Category Counts")
print(df["category"].value_counts())


print("\n LOC OPERATIONS")

electronics = df.loc[df["category"] == "Electronics"]
print("\nAll Electronics Products:")
print(electronics)

high_rating_affordable = df.loc[(df["rating"] > 4.0) & (df["price"] < 5000)]
print("\nHighly Rated Affordable Products:")
print(high_rating_affordable)

df.loc[df["name"] == "Laptop", "stock"] = 20
print("\nUpdated Stock for Laptop:")
print(df.loc[df["name"] == "Laptop"])


print("\n ILOC OPERATIONS")

print("\nFirst 5 Products:")
print(df.iloc[:5])
print("\nLast 5 Products:")
print(df.iloc[-5:])
print("\nEvery Other Row:")
print(df.iloc[::2])

print("\nRows 10–15, Columns 0–3:")
print(df.iloc[10:16, 0:4])


print("\n FILTERED DATAFRAMES ")

budget_products = df[df["price"] < 1000]
premium_products = df[df["price"] > 10000]
popular_products = df[(df["num_reviews"] > 100) & (df["rating"] > 4.0)]

print("\nBudget Products:")
print(budget_products)

print("\nPremium Products:")
print(premium_products)

print("\nPopular Products:")
print(popular_products)


print("\n EXPORTING CSV FILES ")

export_data = {
    "budget_products.csv": budget_products,
    "premium_products.csv": premium_products,
    "popular_products.csv": popular_products
}

for filename, dataframe in export_data.items():
    dataframe.to_csv(filename, index=False)
    print(f"{filename} exported successfully!")

print("\nAnalysis Complete.")
