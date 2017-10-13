# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
original_list_range = int(input("Enter the number of elements you want for the list : \n> "))
original_list = []
print("Let's give input to the list : ")
for x in range(original_list_range):
    original_list.append(int(input("> ")))

user_choice = int(input("Enter the limit number :\n> "))
print("Elements less than {}".format(user_choice))
for x in original_list:
    if x < user_choice:
        print("{} \t".format(x), end = '')
print("\n")

# new list containing all the elements less than user_choice number 
new_list = [x for x in original_list if x < user_choice]
print("Newly created list : {}".format(new_list))