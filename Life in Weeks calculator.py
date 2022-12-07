age = input("What is your current age? ")
time_left_in_years = 90 - int(age)
time_left_in_months = time_left_in_years * 12
time_left_in_weeks = time_left_in_years * 52
time_left_in_days = time_left_in_years * 365
print(f"You have {time_left_in_days} days, {time_left_in_weeks} weeks, and {time_left_in_months} months left.")
