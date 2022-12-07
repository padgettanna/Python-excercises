print("Welcome to Padgett Pizza Deliveries!")
size = input("What size pizza would you like? S, M, or L ")
add_pepperoni = input("Would you like some pepperoni? Y or N ")
extra_cheese = input("Any extra cheese? Y or N ")

bill = 0

if size == "S":
    bill =+ 15
elif size == "M":
    bill += 20
elif size == "L": 
    bill = +25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
