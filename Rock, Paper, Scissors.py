import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Invalid number. You loose.")

computers_choise = random.choice([rock, paper, scissors])
print("Computer chose:\n" + computers_choise)

if choice == 0:
  if computers_choise == paper:
    print("You lose.")
  elif computers_choise == scissors:
    print("You win!")
  else:
    print("It's a draw.")

elif choice == 1:
  if computers_choise == scissors:
    print("You lose.")
  elif computers_choise == rock:
    print("You win!")
  else:
    print("It's a draw.")

else:
  if computers_choise == rock:
    print("You lose.")
  elif computers_choise == paper:
    print("You win!")
  else:
    print("It's a draw.")
