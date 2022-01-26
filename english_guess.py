import sys
import math
import random
import time

password = ""
password = sys.argv[1]
lengthp = len(password)

alpha = {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0
}

freq = {
    'e' : 0,
    't' : 0,
    'a' : 0,
    'o' : 0,
    'i' : 0,
    'n' : 0,
    's' : 0,
    'h' : 0,
    'r' : 0,
    'd' : 0,
    'l' : 0,
    'c' : 0,
    'u' : 0,
    'm' : 0,
    'w' : 0,
    'f' : 0,
    'g' : 0,
    'y' : 0,
    'p' : 0,
    'b' : 0,
    'v' : 0,
    'k' : 0,
    'x' : 0,
    'j' : 0,
    'q' : 0,
    'z' : 0
}
print("here is the password: ")
print (password)
print("=======================")

def check(attempt, real):
    return (attempt == real)

def sys_guess_lower(x, goal, attempt):
    if (len(attempt) == x):
        if(check(attempt, goal)):
           print(attempt)
           return True
        else:
            return False
    else:
        res = False
        for i in alpha:
            if(res):
                return res
            else:
                res = sys_guess_lower(x, goal, attempt + i)
        return False

def sys_guess_lower_order(x, goal, attempt):
    if (len(attempt) == x):
        if(check(attempt, goal)):
            print(attempt)
            return True
        else:
            return False
    else:
        res = False
        for i in freq:
            if(res):
                return res
            else:
                res = sys_guess_lower_order(x, goal, attempt + i)
        return False


print("Standard systematic check:")
ts1 = time.time()
print(sys_guess_lower(lengthp, password, ""))
ts2 = time.time()
print("it took ",(ts2-ts1)," seconds to run")
print("===========================")
print("Ordered by frequency check:")
ts1 = time.time()
print(sys_guess_lower_order(lengthp, password, ""))
ts2 = time.time()
print("it took ", (ts2-ts1)," seconds to run")
