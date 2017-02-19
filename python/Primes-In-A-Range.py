#Find all prime numbers in a specified range.
#Note, this will take long for big numbers.

import math
start = int(input("Start?"))
end = int(input("End?"))

for num in range(start,end):
    root = round(math.sqrt(num))
    prime = True
    for looper in range(2, root+1):
        if num % looper == 0:
            prime = False;
            break;
        else:
            looper = looper + 1
    if prime == True:
        print(num)
input("Done running, press any key to exit!")
