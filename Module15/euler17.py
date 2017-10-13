import time
start = time.time()

def character_count_under_ten (n):
    if n == 1 or n == 2 or n == 6:
        return 3
    elif n == 4 or n == 5 or n == 9:
        return 4
    elif n == 3 or n == 7 or n == 8:
        return 5
    else:
        return 0


def character_count (number):
    if number < 10:
        if number == 1 or number == 2 or number == 6:
            return 3
        elif number == 4 or number == 5 or number == 9:
            return 4
        elif number == 3 or number == 7 or number == 8:
            return 5
        else:
            return 0

    elif 10 <= number < 20:
            if number == 10:
                return 3
            elif number == 11 or number == 12:
                return 6
            elif number == 15 or number == 16:
                return 7
            elif number == 13 or number == 14 or number == 18 or number == 19:
                return 8
            elif number == 17:
                return 9

    elif 20 <= number <100:
        if 20 <= number < 30:
            return 6 +  character_count_under_ten (number-20)
        elif 30 <= number < 40:
            return 6 +  character_count_under_ten (number-30)
        elif 40 <= number < 50:
            return 5 +  character_count_under_ten (number-40)
        elif 50 <= number < 60:
            return 5 +  character_count_under_ten (number-50)
        elif 60 <= number < 70:
            return 5 +  character_count_under_ten (number-60)
        elif 70 <= number < 80:
            return 7 +  character_count_under_ten (number-70)
        elif 80 <= number < 90:
            return 6 +  character_count_under_ten (number-80)
        elif 90 <= number < 100:
            return 6 +  character_count_under_ten (number-90)

number = 0
character_sum = 0
x =0
#z = 0

for x in range (1,1001):
    if x < 100:
        character_sum += character_count (x)
        print (x,character_count (x),character_sum)
    elif x == 100:
        character_sum += 10
    elif 100 < x < 200:
        character_sum += 13 + character_count (x-100)
        print (x,character_count (x-100),character_sum)
    elif x == 200:
        character_sum += 10
    elif 200 < x < 300:
        character_sum += 13 + character_count (x-200)
        print (x,character_count (x-200),character_sum)
    elif x == 300:
        character_sum += 12
    elif 300 < x < 400:
        character_sum += 15 + character_count (x-300)
        print (x,character_count (x-300),character_sum)
    elif x == 400:
        character_sum += 11
    elif 400 < x < 500:
        character_sum += 14 + character_count (x-400)
        print (x,character_count (x-400),character_sum)
    elif x == 500:
        character_sum += 11
    elif 500 < x < 600:
        character_sum += 14 + character_count (x-500)
        print (x,character_count (x-500),character_sum)
    elif x == 600:
        character_sum += 10
    elif 600 < x < 700:
        character_sum += 13 + character_count (x-600)
        print (x, character_count (x-600),character_sum)
    elif x == 700:
        character_sum += 12
    elif 700 < x < 800:
        character_sum += 15 + character_count (x-700)
        print (x,character_count (x-700),character_sum)
    elif x == 800:
        character_sum += 12
    elif 800 < x < 900:
        character_sum += 15 + character_count (x-800)
        print (x,character_count (x-800),character_sum)
    elif x == 900:
        character_sum += 11
    elif 900 < x < 1000:
        character_sum += 14 + character_count (x-900)
        print (x,character_count (x-900),character_sum)
    elif x == 1000:
        character_sum += 11



print (character_sum)
elapsed = time.time() - start
print "found in %s seconds" % (elapsed)
