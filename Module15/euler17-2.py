import math
import time
start = time.time()

#upper_limit = 1000

#character_count_array = [1]*upper_limit

S = { 0 , 3 , 3 , 5 , 4 , 4 , 3 , 5 , 5 , 4 , 3 , 6 , 6 ,8 , 8 , 7 , 7 , 9 , 8 , 7 }
D = { 0, 3 , 6 , 6 , 5 , 5 , 5 , 7 , 7 , 6 }
H = 7
T = 8

total = 0
for i in range(1 , 1000):
    c = i % 10 #singles digit
    b = ((i % 100) - c) / 10 #tens digit
    a = (((i % 1000) - (b * 10) - c) / 100 #Hundreds







elapsed = time.time() - start
print "Found in %s seconds." % (elapsed)
