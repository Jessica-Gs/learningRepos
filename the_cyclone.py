# This program creates a entry system for a roller coaster
# To get on the roller coaster the person must be:
# At least 137cm tall and have 10 credits

# Ask the user to enter their height in centimeters and amount of credits they have
height = int(input("Enter your height in centimeters: "))
credits = int(input("Enter amount of credits you have: "))

# If user's height is at least 137cm and have at least 10 credits
if height >= 137 and credits >= 10:
    print("You may ride the roller coaster! Enjoy the ride!")
# If user's height is less than 137cm and have at least 10 credits
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
    print("You are " + str(height) + "cm and must be 137cm to ride.")
# If the user's height is at least 137 but they have less than 10 credits
elif height >= 137 and credits < 10:
    print("You don't have enough credits.")
    print("You have " + str(credits) + " credit(s) and must have 10 to ride.")
# Else if they don't meet either requirements
else:
    print("You are not tall enough and also do not have the required amount of credits to ride.")