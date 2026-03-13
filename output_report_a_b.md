# Data Analysis Report

## Part A — E-Commerce Product Analyzer

### FIRST 5 MINUTES CHECKLIST

#### 1️⃣ Head of DataFrame

     name     category  price  stock  rating  num_reviews
0 Laptop Electronics 65000 10 4.6 320
1 Smartphone Electronics 30000 25 4.4 500
2 Headphones Electronics 2500 40 4.2 150
3 Smartwatch Electronics 8000 15 4.1 210
4 Tablet Electronics 20000 12 4.3 180


#### 2️⃣ DataFrame Shape
(24, 6)


#### 3️⃣ Data Types
name str
category str
price int64
stock int64
rating float64
num_reviews int64
dtype: object


#### 4️⃣ Missing Values
name 0
category 0
price 0
stock 0
rating 0
num_reviews 0
dtype: int64




#### 5️⃣ Summary Statistics


          price       stock     rating  num_reviews
count 24.000000 24.000000 24.000000 24.000000
mean 9440.416667 52.250000 4.220833 149.791667
std 16108.466172 44.223985 0.226465 116.679412
min 120.000000 8.000000 3.800000 30.000000
25% 775.000000 18.750000 4.075000 73.750000
50% 2500.000000 42.500000 4.200000 115.000000
75% 9000.000000 71.250000 4.400000 180.000000
max 65000.000000 200.000000 4.700000 500.000000




#### 6️⃣ Category Counts
Electronics 9
Clothing 5
Books 5
Home 5



### LOC OPERATIONS


#### All Electronics Products
Laptop, Smartphone, Headphones, Smartwatch, Tablet, Gaming Console, Monitor, Keyboard, Mouse



#### Highly Rated Affordable Products
Products rated >4.0 with price <5000 including:
Headphones, Jacket, Sneakers, Novel, Cookbook, Dictionary, Comics, Blender, Lamp, Keyboard


#### Updated Stock
Laptop stock updated from 10 → 20



### ILOC OPERATIONS

- First 5 rows retrieved successfully
- Last 5 rows retrieved successfully
- Every other row selected using step slicing
- Rows 10–15 with columns 0–3 extracted

### FILTERED DATAFRAMES

**Budget Products (price <1000)**  
T-shirt, Cap, Novel, Cookbook, Notebook, Dictionary, Comics, Lamp, Mouse

**Premium Products (price >10000)**  
Laptop, Smartphone, Tablet, Vacuum Cleaner, Gaming Console, Monitor

**Popular Products (reviews >100 and rating >4.0)**  
Laptop, Smartphone, Headphones, Smartwatch, Tablet, Sneakers, Novel, Cookbook, Vacuum Cleaner, Gaming Console, Monitor, Keyboard

### Export Results
budget_products.csv
premium_products.csv
popular_products.csv


All files exported successfully.

---


# Part B — Multi-DataFrame Sales Comparison

## January REPORT
Total Revenue: 221200
Average Order Value: 27650.0
Top Selling Product: Mouse



## February REPORT
Total Revenue: 204450
Average Order Value: 25556.25
Top Selling Product: Mouse



## March REPORT
Total Revenue: 213900
Average Order Value: 26737.5
Top Selling Product: Mouse



## SUMMARY COMPARISON
      Total Revenue  Avg Order Value Top Product
January 221200 27650.00 Mouse
February 204450 25556.25 Mouse
March 213900 26737.50 Mouse


## HIGH VALUE ORDERS (Revenue > 20000)
order_id product price quantity revenue
1 Laptop 60000 1 60000
2 Phone 25000 2 50000
4 Laptop 60000 1 60000
7 Phone 25000 1 25000




## TOP 3 HIGHEST REVENUE ORDERS
Laptop 60000
Laptop 60000
Phone 50000



## 3 LOWEST REVENUE ORDERS
Keyboard 2400
Mouse 2800
Headphones 6000


---

## Conclusion

This report demonstrates:

- Exploratory Data Analysis with pandas  
- Data filtering using `.loc`, `.iloc`, and `.query()`  
- Multi-DataFrame comparison across monthly datasets  
- Revenue analytics and product performance insights  
- Outlier detection using `.nlargest()` and `.nsmallest()`  
"""
output_file = "output_report_a_b.md"
