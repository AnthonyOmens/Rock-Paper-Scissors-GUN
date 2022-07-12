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

gun = '''
    _______
---'   ____)______________
          ________________)
      (_________________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# 1 Rock
# 2 Paper
# 3 Scissors
# 4 GUN!!!

playerInput = int(input("Rock Paper or Scissors?\n1 for Rock, 2 for Paper and 3 for Scissors\n"))

computerInput = random.randint(1,4)

fistList = [rock, paper, scissors, gun]

if playerInput == 1: #Rock
  print("You chose Rock")
  print(fistList[playerInput-1])
  if computerInput == 1: #Rock
    print("Computer chose Rock!")
    print(fistList[computerInput-1])
    print("Tie!") #CHANGE
  elif computerInput == 2: #Paper
    print("Computer chose Paper!")
    print(fistList[computerInput-1])
    print("You Lose, computer wins :/") #CHANGE
  elif computerInput == 3: # Scissors
    print("Computer chose Scissors")
    print(fistList[computerInput-1])
    print("You win!") #CHANGE
  elif computerInput == 4: #Gun
    print("Computer chose GUN!!!")
    print(fistList[computerInput-1])
    print("you lose, you always lose")

if playerInput == 2: #Paper
  print("You chose Paper")
  print(fistList[playerInput-1])
  if computerInput == 1: #Rock
    print("Computer chose Rock!")
    print(fistList[computerInput-1])
    print("You win!") #CHANGE
  elif computerInput == 2: #Paper
    print("Computer chose Paper!")
    print(fistList[computerInput-1])
    print("Tie!") #CHANGE
  elif computerInput == 3: # Scissors
    print("Computer chose Scissors")
    print(fistList[computerInput-1])
    print("You Lose, computer wins :/") #CHANGE
  elif computerInput == 4: #Gun
    print("Computer chose GUN!!!")
    print(fistList[computerInput-1])
    print("you lose, you always lose")
    

if playerInput == 3: #Scissors
  print("You chose Scissors")
  print(fistList[playerInput-1])
  if computerInput == 1: #Rock
    print("Computer chose Rock!")
    print(fistList[computerInput-1])
    print("You Lose, computer wins :/") #CHANGE
  elif computerInput == 2: #Paper
    print("Computer chose Paper!")
    print(fistList[computerInput-1])
    print("You win!") #CHANGE
  elif computerInput == 3: # Scissors
    print("Computer chose Scissors")
    print(fistList[computerInput-1])
    print("Tie!") #CHANGE
  elif computerInput == 4: #Gun
    print("Computer chose GUN!!!")
    print(fistList[computerInput-1])
    print("you lose, you always lose")