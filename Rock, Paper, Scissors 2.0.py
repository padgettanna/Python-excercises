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

images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >=3 or choice < 0:
  print("You've chosen invalid number, you loose!")
else:
  print(f"You chose \n {images[choice]}")

  computers_choice = random.randint(0,2)
  print(f"Computer chose:\n {images[computers_choice]}")

  if choice == 0 and computers_choice == 2:
    print("You win!")
  elif choice == 2 and computers_choice == 0:
    print("You loose!")
  elif choice > computers_choice:
    print("You win!")
  elif choice < computers_choice:
    print("You loose!")
  elif choice == computers_choice:
    print("It's a draw!")
