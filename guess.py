# Initialize variables
guess = 0
tries = 0
number = 6  # Variable for the number to guess for

# While the user does not guess the correct number and tries is less than 5
while guess != number and tries < 5:
  guess = int(input("Guess the number: "))
  tries += 1 
  warn = 5 - tries # Creating a variable for warning the user how many tries they have left
  if guess != number: # Only warn them if they haven't guessed the correct number
    print("You have " + str(warn) + " tries left!")

if guess == number:
  print("You got it!")
else:
  print("You ran out of tries!")