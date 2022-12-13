import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_names = len(names)
random_number = random.randint(0, number_of_names - 1)
person_pays = names[random_number]

# or use line 11 instead of lines 6, 7 and 8
#person_pays = random.choice(names)

print(person_pays + " is going to buy meal today!")
