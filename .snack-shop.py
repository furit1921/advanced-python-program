
snack_item = "lays barbecue chips"
price = 9.99
quantity = 10
is_available = True


print("snack item:", snack_item)
print("type of snack item:", type(snack_item))
print("price:", price)
print("type of price:", type(price))
print("quantity:", quantity)
print("type of quantity:", type(quantity))
print("is available:", is_available)
print("type of is available:", type(is_available))

total_cost = price * quantity
print("total cost:", total_cost)
sales_price = price - 0.25
print("sales price:", sales_price)
double_stock = quantity * 2
print("double stock:", double_stock)