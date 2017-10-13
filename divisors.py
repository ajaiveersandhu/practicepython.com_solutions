# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Enter any number you wish, I will tell you all it's divisors : \n> "))
divisors_list = []
for i in range(number, 0, -1):
    if number%i == 0:
        divisors_list.append(i)

print(sorted(divisors_list))
