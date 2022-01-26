import sys
import math
import random
import time
import urllib.request

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib.request.urlopen(word_site)
txt = response.read().decode()
WORDS = txt.splitlines()

alpha = (
    'a' ,
    'b' ,
    'c' ,
    'd' ,
    'e' ,
    'f' ,
    'g' ,
    'h' ,
    'i' ,
    'j' ,
    'k' ,
    'l' ,
    'm' ,
    'n' ,
    'o' ,
    'p' ,
    'q' ,
    'r' ,
    's' ,
    't' ,
    'u' ,
    'v' ,
    'w' ,
    'x' ,
    'y' ,
    'z' 
)

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

dicFreq = (
    'e',
    's',
    'i',
    'a',
    'r',
    'n',
    't',
    'o',
    'l',
    'c',
    'd',
    'u',
    'g',
    'p',
    'm',
    'k',
    'h',
    'b',
    'y',
    'f',
    'v',
    'w',
    'z',
    'x',
    'q',
    'j'
)


def check(attempt, real):
    return (attempt == real)


def sys_guess_lower(x, goal, attempt, i=0):
    if(i == x):
        #return (goal == attempt)
        if(goal == attempt):
            #print(attempt)
            return True
        return False
    for n in alpha:
        if(sys_guess_lower(x, goal, attempt + n, i+1)):
            return True
    return False

def sys_guess_lower_order(x, goal, attempt, i=0):
    if(i == x):
        #return (goal == attempt)
        if(goal == attempt):
            #print(attempt)
            return True
        return False
    for n in dicFreq:
        if(sys_guess_lower_order(x, goal, attempt + n, i+1)):
            return True
    return False


def random_password_limit(x):
    word = random.choice(WORDS)
    if (len(word) <= x):
        #print (word)
        return word
    else:
        res = ""
        for char in word:
            res += char
            if(len(res) == x):
                #print (res)
                return res
    return False

timeStandard = 0
timeOrdered = 0
trials = 50

for i in range(trials):
    password = random_password_limit(5)
    lengthp = len(password)
    #print("here is the password: ")
    print (password)
    #print("=======================")
   # print("Standard systematic check:")
    ts1 = time.time()
    sys_guess_lower(lengthp, password, "")
    ts2 = time.time()
    #print("it took ",(ts2-ts1)," seconds to run")
    timeStandard += (ts2-ts1)
    #print("===========================")
    #print("Ordered by frequency check:")
    ts1 = time.time()
    sys_guess_lower_order(lengthp, password, "")
    ts2 = time.time()
    #print("it took ", (ts2-ts1)," seconds to run")
    timeOrdered += (ts2-ts1)

print()
print("============")
print()
print("Total time standard: ", timeStandard, " seconds")
print("Total time ordered: ", timeOrdered, " seconds")
print("differance: ", (timeStandard - timeOrdered), " seconds")
print("average differance per password: ", (timeStandard-timeOrdered)/trials, " seconds")
