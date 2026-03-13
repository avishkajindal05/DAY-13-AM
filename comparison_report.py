import pandas as pd


jan_data = {
    "order_id": [1,2,3,4,5,6,7,8],
    "product": ["Laptop","Phone","Headphones","Laptop","Mouse","Keyboard","Phone","Monitor"],
    "price": [60000,25000,2000,60000,700,1200,25000,15000],
    "quantity": [1,2,3,1,4,2,1,1]
}

feb_data = {
    "order_id": [9,10,11,12,13,14,15,16],
    "product": ["Laptop","Tablet","Phone","Headphones","Mouse","Keyboard","Monitor","Phone"],
    "price": [62000,18000,24000,2200,750,1300,15500,24000],
    "quantity": [1,1,2,3,5,2,1,2]
}

mar_data = {
    "order_id": [17,18,19,20,21,22,23,24],
    "product": ["Laptop","Phone","Tablet","Headphones","Mouse","Keyboard","Monitor","Laptop"],
    "price": [61000,24500,17500,2100,800,1400,16000,61000],
    "quantity": [1,2,1,2,3,2,1,1]
}

jan_df = pd.DataFrame(jan_data)
feb_df = pd.DataFrame(feb_data)
mar_df = pd.DataFrame(mar_data)

for df in [jan_df, feb_df, mar_df]:
    df["revenue"] = df["price"] * df["quantity"]


def analyze_month(df, month_name):

    total_revenue = df["revenue"].sum()

    avg_order_value = df["revenue"].mean()

    top_product = (
        df.groupby("product")["quantity"]
        .sum()
        .idxmax()
    )

    print(f"\n {month_name} REPORT ")
    print("Total Revenue:", total_revenue)
    print("Average Order Value:", round(avg_order_value,2))
    print("Top Selling Product:", top_product)

    return {
        "Total Revenue": total_revenue,
        "Avg Order Value": avg_order_value,
        "Top Product": top_product
    }


jan_metrics = analyze_month(jan_df, "January")
feb_metrics = analyze_month(feb_df, "February")
mar_metrics = analyze_month(mar_df, "March")


summary_df = pd.DataFrame(
    [jan_metrics, feb_metrics, mar_metrics],
    index=["January","February","March"]
)

print("\n SUMMARY COMPARISON ")
print(summary_df)


print("\n HIGH VALUE ORDERS (Revenue > 20000) ")

high_value_orders = jan_df.query("revenue > 20000")
print(high_value_orders)

print("\n TOP 3 HIGHEST REVENUE ORDERS ")
print(jan_df.nlargest(3, "revenue"))

print("\n 3 LOWEST REVENUE ORDERS ")
print(jan_df.nsmallest(3, "revenue"))

print("\nAnalysis Complete.")
