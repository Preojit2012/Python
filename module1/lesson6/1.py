age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()

if age<5:
    price = 0
elif age<=18 or student == "yes":
    price = 15
else:
    price = 20

print(f"Your ticket price is: {price} dollars.")