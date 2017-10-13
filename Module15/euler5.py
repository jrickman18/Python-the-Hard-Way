def check_if_divisible(numerator):          # Defines a function that will check if the numerator is devisible by every number in the given range
    for denominator in range (11,21):       # Will loop from 11 to 20 (we already know there are 2520 from 1 to 10)
        if numerator % denominator == 0:    # Checks to see if numerator is devisible by denominator without a remainder
            continue                        # If it is evenly divisible then continue to next higher denominator in the range
        else:
            return False                    # If it's not evenly divisible, then return False; this will result in x being increased by 1
    return True                             # If it looped through all the denominators in the range and never hit a False, then it will return True and the run is complete

x = 2520                                    # Start the program with x set to 2520 since we already know that's the total for 1 to 10

while not check_if_divisible(x):            # While the check_if_divisible function is False, keep looping until it returns True
    x += 2520                               # CheckIfDivisible(x) is False so increment x by 1 and then go run the function again with the next number

print(x)                                    # Prints out the final answer after the function returned True
