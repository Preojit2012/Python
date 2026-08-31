buying_price = int(input("Enter the buying price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > buying_price:
    profit = selling_price - buying_price
    print(f"You had a profit of ${profit}.")
else:
    loss = buying_price-selling_price
    print(f"You had a loss of ${loss}.")