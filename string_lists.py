# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
user_input = input("Get me some input, buddy :\n> ")
reversed_user_input = user_input[::-1]
if user_input == reversed_user_input:
    print("Your string '{}' is a palindrom.".format(user_input))
else:
    print("Your string '{}' is not a palindrom.".format(user_input))
