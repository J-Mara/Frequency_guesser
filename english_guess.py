import sys
import math
import random

password = ""
password = sys.argv[1]
lengthp = len(password)

freq = {
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

print (password)

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
        for i in freq:
            if(res):
                return res
            else:
                res = sys_guess_lower(x, goal, attempt + i)
        return False
    
print(sys_guess_lower(lengthp, password, ""))
