age=int(input("Enter your age: "))
height=float(input("Enter your height in cm: "))
vip=input("Do you have a vip pass? (Yes/No): ").strip()=="True"

ticket_price = 0
allowed=True
if height< 100 and not vip:
    allowed=False
    print(("Sorry. You are not allowed in the park."))

if allowed:
    if age < 3:
        ticket_price = 0
    elif 3<=age<= 10:
        ticket_price=15
    elif 13 <= age <=18:
        ticket_price = 20
    else:
        ticket_price = 25
    if vip:
        ticket_price=ticket_price * 0.5
        print("VIP Pass Applied! You got a 50% discount.")

    print(f"Access Granted! Your final ticket price is ${ticket_price}")