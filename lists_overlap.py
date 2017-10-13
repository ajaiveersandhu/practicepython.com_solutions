# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

from random import randint
# # getting list_1 from user
# list1_range = int(input("Enter the number of elements you want in list_1 : \n> "))
# list_1 = []
# print("Let's give some input to the list :")
# for x in range(list1_range):
#     list_1.append(int(input("> ")))

# # giving random input to the list :
list_1 = []
list1_range = randint(1,20)
for x in range(list1_range):
    list_1.append(randint(1,10))


# # getting list_2 from user
# list2_range = int(input("Enter the number of elements you want in list_2 : \n> "))
# list_2 = []
# print("Let's give some input to the list :")
# for x in range(list2_range):
#     list_2.append(int(input("> ")))

# # giving random input to the list :
list_2 = []
list2_range = randint(1,20)
for x in range(list2_range):
    list_2.append(randint(1,20))


common_elements_list = []

print("list1_range : {0}\nlist2_range : {1}\nlist_1 : {2}\nlist_2 : {3}\
      ".format(list1_range, list2_range, list_1, list_2))
print("Common and non-duplicate elements are : ")
for x in list_1:
    if x in list_2 and x not in common_elements_list:
        common_elements_list.append(x)
        print("{}\t".format(x), end = '')
print("\n")