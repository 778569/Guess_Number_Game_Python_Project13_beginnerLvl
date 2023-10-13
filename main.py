#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)





def Guess_N(R_Number,Max_Atm):
  Chance = 0
  Game_over = True
  while Game_over and Chance < Max_Atm:
    print(f"You have {Max_Atm - Chance} attempts remaining to guess the number")
    guess= int(input("Make a guess : "))
    if R_Number == guess:
       
       print(f"You got it! The answer was {R_Number}.")
       Game_over = False
    elif R_Number > guess:
      print("Too low.")
      Chance += 1
    else:
      print("Too high.")
      Chance += 1
  if Chance == Max_Atm:
    print("Game over.!!! You lost.!!!")




random_numbers = []

for number in range(100):
  random_numbers.append(number)

R_Number = random.choice(random_numbers)
 #or can usr randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {R_Number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': easy : ").lower()

if difficulty == "easy":
  Chance = 10
  Guess_N(R_Number, Chance)
  

else:
  Chance = 5
  Guess_N(R_Number, Chance)
  
