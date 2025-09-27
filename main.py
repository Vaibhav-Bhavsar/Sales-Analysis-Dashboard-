import pandas as pd
import matplotlib.pyplot as plt

# Date
# Region
# Salesperson
# Units_Sold
# Unit_Price
# Total_Revenue
sale=pd.read_csv('sales_data_2025.csv')
sale['Date']=pd.to_datetime(sale['Date'],dayfirst=True)
sale['Month']=sale['Date'].dt.to_period('M')

# Total_Revenue Month
month_revenue=sale.groupby('Month')['Total_Revenue'].sum()
# print(month_revenue)
month_revenue.plot(kind='bar',color='skyblue')
plt.title("Monthly Revenue")
plt.ylabel('revenue')
plt.xlabel('month')
plt.xticks(rotation=45)
plt.show()
input("Press Enter to see next chart...")

# product_performance=Product,Units_Sold','Total_Revenue
product_performance=sale.groupby('Product')[['Units_Sold','Total_Revenue']].sum()
print(product_performance)
product_performance.plot(kind='bar')
plt.title("Product Performance (Units & Revenue)")
plt.ylabel("Values") # as python automatically add the profuct name
plt.xticks(rotation=45)
plt.show()
input("Press Enter to see next chart...")

#Region_revenue=Region,Total_Revenue
Region_revenue=sale.groupby('Region')['Total_Revenue'].sum()
print(Region_revenue)
Region_revenue.plot(kind='pie')
plt.title("Product Performance (Units & Revenue)")
plt.ylabel(" ")
plt.xticks(rotation=45)
plt.show()
input("Press Enter to see next chart...")

# saleperson_performance=Salesperson,Units_Sold','Total_Revenue
saleperson_performance=sale.groupby('Salesperson')[['Units_Sold','Total_Revenue']].sum()
print(saleperson_performance)

saleperson_performance.plot(kind='bar')
plt.title("Salesperson Performance")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.show()

print('all the data is showed')