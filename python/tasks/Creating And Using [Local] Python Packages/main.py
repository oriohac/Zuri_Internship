import random

#Make User understand the game
print("**************WELCOME TO ROCK, PAPER AND SCISSORS GAME**************")
print("********************************RULES*******************************")
print("There are Three Characters to choose, R for Rock, P for Paper and S for Scissors")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")
print("If two players choose the same character, it is a tie")
#create a list of three choices
c_choice = ['R','P','S']
while True:
#define function choose() so that player will enter his/her choice and the computer will choose randomly
 def choose():
       '''function to make choices, this is the main body of the game'''
       choose.player_choice = str(input("Enter R, P or S To choose A character: "))
       choose.player_choice = choose.player_choice.upper()
       computer = random.choice(c_choice)
      
      #if player choice is equal to user choice promt player to choose character again
       if choose.player_choice == computer:
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("tied")
         choose()
      #else if the player choice is rock and computer is scissors player wins
       elif choose.player_choice == 'R' and computer == 'S':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Player Win!")
       #else if the player choice is paper and computer is rock player wins
       elif choose.player_choice == 'P' and computer == 'R':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Player Win!")
      #else if the player choice is scissors and computer is paper player wins
       elif choose.player_choice == 'S' and computer == 'P':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Player Win!")

      #else if the player choice is scissors and computer is rock computer wins
       elif choose.player_choice == 'S' and computer == 'R':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Computer Win!")
      #else if the player choice is rock and computer is paper computer wins
       elif choose.player_choice == 'R' and computer == 'P':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Computer Win!")
      #else if the player choice is paper and computer is scissors computer wins
       elif choose.player_choice == 'P' and computer == 'S':
         print("Player""(",choose.player_choice,")"":""CPU""(",computer,")")
         print("Computer Win!")
      #else if the player and computer choice doesn't meet any of the critereas, then go back and choose a charater
       else:
              print("Enter The right Character: R, P or S ")
              choose()
              return
              
 choose()
 break
  