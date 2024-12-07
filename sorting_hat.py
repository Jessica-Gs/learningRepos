# Program to decide which Hogwarts "House" the user belongs to
# Asks a series of questions and assigns points to each house based on the user's answers

# Initializing House variables for default scores
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question 1
print("Q1) Do you like Dawn or Dusk? (Enter a number 1 or 2)")
answer = int(input("1) Dawn\n2) Dusk\n"))
# If answer is Dawn
if answer == 1:
    gryffindor += 1 # Increment by 1
    ravenclaw += 1 
# If answer is Dusk
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
# If user enters something else
else:
    print("Wrong input. You must enter a number 1 or 2.")

# Question 2
print("Q2) When I'm dead, I want people to remember me as: (Enter a number 1-4)")
answer = int(input("1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong input. You must enter a number 1-4.")

# Question 3
print("Q3) Which kind of instrument most pleases your ear? (Enter a number 1-4)")
answer = int(input("1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong input. You must enter a number 1-4.")

# Print the total for each house
print("Total Points")
print("Gryffindor: " + str(gryffindor))
print("Ravenclaw: " + str(ravenclaw))
print("Hufflepuff: " + str(hufflepuff))
print("Slytherin: " + str(slytherin))

# Storing the value of the max function into a variable for easy reference
house = max(gryffindor, hufflepuff, ravenclaw, slytherin) 

# Decide which house to place the user in 
# This is based off the return value of max() compared to the value of each house variable
if house == gryffindor:
    print("You belong to Gryffindor!")
elif house == hufflepuff:
    print("You belong to Hufflepuff!")
elif house == ravenclaw:
    print("You belong to Ravenclaw!")
elif house == slytherin:
    print("You belong to Slytherin!")

# NOTE: Possible edge case: If two houses are selected for the max values