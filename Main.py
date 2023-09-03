import random
import os
from tkinter import Tk

print("The Ultimate Rock Paper Scissors Game")
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

#Write your code below this line 👇
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def gamestart():
  user_score = 0
  computer_score = 0
  while True:
    bet = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    clear_console()
    if bet >=3:
      print("you entered the wrong input. Try again")
    else:
      options = [rock, paper, scissors]
      user_input = options[bet]
      print("You Chose: \n" + user_input)

      random_computer_input = random.randint(0, len(options) - 1)
      computer_input = options[random_computer_input]
      print("Computer chose" + computer_input)
      if (user_input == rock) and (computer_input == paper):
        print("You lose!")
        computer_score += 1
      elif (user_input == rock) and (computer_input == scissors):
        print("You Win!")
        user_score += 1
      elif (user_input == rock) and (computer_input == rock):
        print("A draw!")

      if (user_input == paper) and (computer_input == scissors):
        print("You lose!")
        computer_score += 1
      elif (user_input == paper) and (computer_input == rock):
        print("You Win!")
        user_score += 1
      elif (user_input == paper) and (computer_input == paper):
        print("A draw!")

      if (user_input == scissors) and (computer_input == rock):
        print("You lose!")
        computer_score += 1
      elif (user_input == scissors) and (computer_input == paper):
        print("You Win!")
        user_score += 1
      elif (user_input == scissors) and (computer_input == scissors):
        print("A draw!")

      print(f"Your Score: {user_score} \nComputer Score:  {computer_score}")
clear_console()
gamestart()




