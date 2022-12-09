print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

count_t = name1_lower_case.count('t') + name2_lower_case.count('t')
count_r = name1_lower_case.count('r') + name2_lower_case.count('r')
count_u = name1_lower_case.count('u') + name2_lower_case.count('u')
count_e = name1_lower_case.count('e') + name2_lower_case.count('e')
count_l = name1_lower_case.count('l') + name2_lower_case.count('l')
count_o = name1_lower_case.count('o') + name2_lower_case.count('o')
count_v = name1_lower_case.count('v') + name2_lower_case.count('v')
count_e = name1_lower_case.count('e') + name2_lower_case.count('e')

first_number = str(count_t + count_r + count_u + count_e)
second_number = str(count_l + count_o + count_v + count_e)
love_score = int(first_number + second_number)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
