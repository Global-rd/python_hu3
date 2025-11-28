import pandas as pd

df = pd.read_csv("lessons/lesson_14/datasets/supermarket_sales.csv")
print(df)

print(df.dtypes)
print(len(df))
print(df.info())

print(df.head(10))
print(df.tail(10))

product_price_df = df[['Product line', 'Unit price']]
print(product_price_df)
print(type(product_price_df['Product line']))

#loc 
print("------------")
print(product_price_df.loc[1, "Product line"])
print(df.loc[1:3, ['Product line', 'Unit price']])

#iloc
print("------------")
print(df.iloc[1, 1])
print(df.iloc[1:3, [1,2]])


#aggregation and grouping
print("----------------")
#total sales per city and product line
total_sales_df = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()
print(total_sales_df)

# average rating by customer type and payment
avg_rating_df = df.groupby(['Customer type', 'Payment'])['Rating'].mean().reset_index()
print(avg_rating_df)


#filtering
print("-------")
yangon_df = df[df['City'] == 'Yangon']
print(yangon_df)
print(len(yangon_df))

#method chaining:

result_df = (df[df["City"] == 'Yangon']
             .groupby('Gender')
             .agg({'Unit price': 'mean'})
             .sort_values('Unit price', ascending=False)
             .reset_index()
             )


print("-----------------------")


df_stock_base = pd.read_csv("lessons/lesson_14/datasets/stock_base.csv")
df_stock_extension = pd.read_csv("lessons/lesson_14/datasets/stock_extension.csv")

print(df_stock_base)
print(df_stock_extension)

merged_df = pd.merge(left=df_stock_base,
                     right=df_stock_extension,
                     on="id",
                     how="left")

print(merged_df)

#apply

def categorize_stock(row):
    if row["price"] > 1000:
        return 'Premium'
    else:
        return 'Standard'
    
merged_df['category'] = merged_df.apply(categorize_stock, axis=1)
print(merged_df)

# lambda functions!

