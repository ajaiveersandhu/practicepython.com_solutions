# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter a number : \n> "))
if number%2 == 0:
    print("You have entered an even number.")
# optional 
elif number%4 == 0:
    print("You entered a factor of number 4.")
else:
    print("You have entered an odd number.")

num = int(input("Enter a numerator(num) : \n> "))
check = int(input("Enter a denominator(check) : \n> "))
if check//num == 0:
    print("{0} divides {1} evenly.".format(check, num))
else:
    print("{0} divides {1} oddly.".format(check, num))