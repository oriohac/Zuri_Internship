our_fav_number = 10

#take user input
user_guess = input("Enter Your Guess: ")

print(type(user_guess))
user_guess = int(user_guess)
print (type(user_guess))
if user_guess == our_fav_number:
   print("success, you guessed the number! our favourite number is: "+ str(our_fav_number))
if user_guess < our_fav_number:
   print("your guess is too low, try higher ")
if user_guess > our_fav_number:
     print("your guess is too high try lower")

