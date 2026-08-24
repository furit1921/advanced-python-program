
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

price = 9.99
quantity = 10

print("is the price under 10?",price < 10 )
print("is the quantity over 6?", quantity > 6)
print("is the price exactly 9.99?", price == 9.99)

snack_item = "lays barbecue chips"
shop_name = "YUMMY" + " " + "DETERMINATION"

print(snack_item)
print(shop_name)

print("length of shop name:", len(shop_name))
print("length of snack item:", len(snack_item))
print("first letter of shop name:"+ shop_name[0])
print("last letter of shop name:" + shop_name[-1])
print("first letter of snack item:" + snack_item[0])
print("last letter of snack item:" + snack_item[-1])



price_a = 9.99
price_b = 7.99

temp = price_a
price_a = price_b
price_b = temp

print("after swap", price_a , "and", price_b)