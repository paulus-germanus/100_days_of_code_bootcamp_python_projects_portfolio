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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if player_choice == 0:
    print(f"You chose:\n{rock}")
elif player_choice == 1:
    print(f"You chose:\n{paper}")
elif player_choice == 2:
    print(f"You chose:\n{scissors}")

if computer_choice == 0:
    print(f"Computer chose:\n{rock}")
elif computer_choice == 1:
    print(f"Computer chose:\n{paper}")
elif computer_choice == 2:
    print(f"Computer chose:\n{scissors}")

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. Try again.")
elif player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 2 and computer_choice == 0:
    print("You loose!")
elif computer_choice == 2 and player_choice == 0:
    print("You win!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice > player_choice:
    print("You loose!")