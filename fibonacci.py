def fibonacci(number):
    if number < 2:
        return number
    else:
        n_minus1 = 1
        n_minus2 = 0
        for x in range(1, number):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
        return result

for x in range(10):
    print("{} \t > ".format(x), fibonacci(x))
    