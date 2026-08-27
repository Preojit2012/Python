item_price=float(input("Give the item price: "))
item_quantity=int(input("Give the quantity of the item: "))
total_bill= item_price * item_quantity
print(f"Total bill: {total_bill} BDT.")

apples = 67
people = 22

print("If apples = 67 and people = 22, then:")

apple_each = apples//people
print(f"Each people gets {apple_each} apples.")

left_over = apples%people
print(f"{left_over} apples are left.")