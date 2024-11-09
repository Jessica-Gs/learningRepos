# Codedex Bonus Article: Python Bugs: Bug Catcher

# Bug:  print('I caught ' + butterflies + ' 🦋 butterflies!')
#       print('I caught ' + beetles + ' 🪲 beetles!')
#       print('I caught ' + ladybug + ' 🐞 ladybugs!)
# Fix: Before we can use an integer as a string, we need to convert it using str()

# Bug: print('I caught ' + str(ladybug) + ' 🐞 ladybugs!)
# Fix: Missing ' at end of string following ladybugs

# Bug print('I caught ' + str(ladybug) + ' 🐞 ladybugs!')
# Fix: ladybug is not a defined variable but ladybugs is

# Bug: print('I caught ' + str(total) + ' total bugs!'
# Fix: Missing ) at end of print()

# Bug print('I caught ' + str(total) + ' total bugs!')
# Fix The variable for total is being used before being defined

butterflies = 10
beetles = 12
ladybugs = 20

total = butterflies + beetles + ladybugs

print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

print('I caught ' + str(total) + ' total bugs!')