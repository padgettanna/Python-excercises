print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_persentage = float(input("What persentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_bill_with_tip = total_bill * (1 + tip_persentage / 100)
each_person_payment_amount = total_bill_with_tip  / number_of_people
round_each_person_payment_amount = round(each_person_payment_amount, 2)
round_each_person_payment_amount = "{:.2f}".format(each_person_payment_amount)

print(f"Each person should pay: {round_each_person_payment_amount}")
