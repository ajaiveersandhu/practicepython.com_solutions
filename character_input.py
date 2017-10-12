# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("# Enter your name, user : \n> ")
age = int(input("# How old are you, {name} :\t(Hint: current year 2017) \n> ".format(name = name)))
message1 = "Hello, {name_of_user}. Welcome :)\
           \nLet's hope you complete your century on {year}.".format(name_of_user = name, year = (2017-age)+100)

print(message1)

# optional
number_of_copies = int(input("\n# How many copies you want for the above message : \n> "))
print("\n" + "*"*10 + "  copies  " + "*"*10 + "\n")
print((message1 + "\n") * number_of_copies)

