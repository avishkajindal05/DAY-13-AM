## Q1 — Difference Between `.loc[]` and `.iloc[]`

### `.loc[]` (Label-Based Indexing)
- Uses **row/column labels**.
- The slice **end value is inclusive**.
- Works with named indexes (strings, dates, etc.).

Example:

import pandas as pd

df = pd.DataFrame({"A":[10,20,30,40,50]}, index=[0,1,2,3,4])

df.loc[0:3]
Output (inclusive):

index	A
0	10
1	20
2	30
3	40
.iloc[] (Position-Based Indexing)
Uses integer positions.

The slice end value is exclusive (Python slicing rule).

Example:


df.iloc[0:3]
Output (exclusive):

index	A
0	10
1	20
2	30
Case 1: Index = 0,1,2,3,4
Expression	Rows Returned
df.loc[0:3]	0,1,2,3
df.iloc[0:3]	0,1,2
Reason:

.loc includes the end label.

.iloc follows Python slicing excluding the end.

Case 2: Index = 'a','b','c','d','e'
Example:


df = pd.DataFrame({"A":[10,20,30,40,50]}, index=["a","b","c","d","e"])
Expression	Result
df.loc["a":"d"]	rows a,b,c,d
df.iloc[0:3]	rows a,b,c
Key difference:

.loc uses labels

.iloc uses positions

Q2 — Function: analyze_csv(filepath)

import pandas as pd

def analyze_csv(filepath):
    
    df = pd.read_csv(filepath)
    
    print("FIRST 5 MINUTES CHECKLIST")
    
    print("\\nHead")
    print(df.head())
    
    print("\\nShape")
    print(df.shape)
    
    print("\\nData Types")
    print(df.dtypes)
    
    print("\\nMissing Values")
    print(df.isnull().sum())
    
    print("\\nSummary Statistics")
    print(df.describe(include="all"))
    
    
    num_rows, num_cols = df.shape
    
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    
    categorical_cols = df.select_dtypes(include="object").columns.tolist()
    
    null_counts = df.isnull().sum().to_dict()
    
    memory_mb = df.memory_usage(deep=True).sum() / (1024**2)
    
    
    return {
        "num_rows": num_rows,
        "num_cols": num_cols,
        "numeric_cols": numeric_cols,
        "categorical_cols": categorical_cols,
        "null_counts": null_counts,
        "memory_mb": memory_mb
    }
Example usage:


report = analyze_csv("sales.csv")
print(report)
Returned dictionary example:


{
 'num_rows': 500,
 'num_cols': 8,
 'numeric_cols': ['price','quantity','revenue'],
 'categorical_cols': ['product','category'],
 'null_counts': {'price':0,'quantity':2},
 'memory_mb': 0.45
}
Q3 — Debugging Pandas Code
Original Code Issues

high_earners = df[df["age"] > 25 and df["salary"] > 55000]
df["age"][0] = 26
first_two = df.iloc[0:2]
Bug 1 — Incorrect Logical Operator
Problem:
and cannot be used for vectorized pandas comparisons.

Fix:
Use bitwise operator & with parentheses.


high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
Bug 2 — Chained Indexing Assignment
Problem:
df["age"][0] = 26 causes SettingWithCopyWarning.

Fix:
Use .loc.


df.loc[0, "age"] = 26
Bug 3 — Misunderstanding .iloc Slice Behavior
Problem:
.iloc[0:2] returns rows 0 and 1 only because slicing is exclusive.

Fix:


first_three = df.iloc[0:3]
print(f"Got {len(first_three)} rows, expected 3")
Corrected Full Code

import pandas as pd
 
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})
 
# Fixed Bug 1
high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
 
# Fixed Bug 2
df.loc[0, "age"] = 26
 
# Fixed Bug 3
first_three = df.iloc[0:3]
print(f"Got {len(first_three)} rows, expected 3")