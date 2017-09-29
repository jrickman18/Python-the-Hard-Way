# If the number is divisible by 11-20, it is also divisible by 1-10
def isdevisible1to20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

n = 1
while True:
    if isdevisible1to20(n):
        break
    n += 1

print n
