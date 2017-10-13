import time
import math

start = time.time()

upper_limit = 10**7                                 # Sets the value of the upper limit of the problem to 10**7

numerator_array = [0]*(upper_limit)                 # Creates an array that has 10**7 single elements

def number_of_divisors (numerator):                 # Defines a function that determines the number of integer divisors that a numerator has
    for divisor in range (1,upper_limit//2):        # Will loop from 1 to upper limit / 2 (with the extra decimals stripped off so it's an integer)
        if numerator % divisor == 0:                # Checks to see if numerator is divisible by denominator without a remainder
            numerator_array[numerator] += 1         # If it is an integer deviser then incrment that numerator's array element by 1
    return

for j in range (2,upper_limit):                     # Loops j from 2 to the upper limit
    number_of_divisors(j)                           # For each j it calls the function number_of_divisors


sum = 0                                             # Sets the initial value of sum to 0
for i in range (2,upper_limit):                     # Loops i from 2 to the upper limit
    if numerator_array[i] == numerator_array[i-1]:  # If the number of positive divisors for two adjacent n's is the same, then increment sum by 1
        sum += 1                                    # Increments sum by 1 if the above is true

print(sum)
elapsed = time.time() - start
print "Found in %s seconds" % (elapsed)                                     # Prints out the final sum of adjacent integers that have the same number of divisors
