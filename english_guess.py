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

freqFirst = (
    's',
    'c',
    'p',
    'd',
    'b',
    'r',
    'a',
    'm',
    't',
    'f',
    'e',
    'i',
    'h',
    'g',
    'l',
    'u',
    'w',
    'o',
    'n',
    'v',
    'j',
    'k',
    'q',
    'y',
    'z',
    'x'
)

   # ('a',
   # 'b',
   # 'c',
   # 'd',
   # 'e',
   # 'f',
   # 'g',
   # 'h',
   # 'i',
   # 'j',
   # 'k',
   # 'l',
   # 'm',
   # 'n',
   # 'o',
   # 'p',
   # 'q',
   # 'r',
   # 's',
   # 't',
   # 'u',
   # 'v',
   # 'w',
   # 'x',
   # 'y',
   # 'z')

freqA = (
    't',
    'n',
    'r',
    'l',
    'c',
    's',
    'd',
    'i',
    'm',
    'p',
    'g',
    'b',
    'y',
    'u',
    'v',
    'k',
    'f',
    'w',
    'h',
    'z',
    'x',
    'q',
    'e',
    'o',
    'a',
    'j'
)

freqB = (
    'e',
    'a',
    'l',
    'i',
    'o',
    'r',
    'u',
    's',
    'y',
    'b',
    'm',
    'c',
    'j',
    't',
    'd',
    'n',
    'p',
    'w',
    'h',
    'v',
    'g',
    'k',
    'z',
    'f',
    'q',
    'x'
)

freqC = (
    'o',
    'e',
    'a',
    'h',
    't',
    'i',
    'k',
    'r',
    'l',
    'u',
    'c',
    's',
    'y',
    'd',
    'n',
    'q',
    'm',
    'p',
    'b',
    'f',
    'g',
    'v',
    'z',
    'j',
    'w',
    'x'
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
    #print("i: ", i)
    if(i == x):
        #return (goal == attempt)
        if(goal == attempt):
            #print(attempt)
            return True
        return False
    if(i == 0):
        for t in freqFirst:
            if(sys_guess_lower_order(x, goal, attempt + t, i+1)):
                return True
        return False
    elif(attempt[i-1] == 'a'):
        for t in freqA:
            if(sys_guess_lower_order(x, goal, attempt + t, i+1)):
                return True
        return False
    elif(attempt[i-1] == 'b'):
        for t in freqB:
            if(sys_guess_lower_order(x, goal, attempt + t, i+1)):
                return True
        return False
    elif(attempt[i-1] == 'c'):
        for t in freqC:
            if(sys_guess_lower_order(x, goal, attempt + t, i+1)):
                return True
        return False
    else:
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
trials = 500

for i in range(trials):
    password = random_password_limit(4)
    lengthp = len(password)
   # print("here is the password: ")
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
#print("differance: ", (timeStandard - timeOrdered), " seconds")
print("It took the simple frequency based algorythm ", (timeOrdered/timeStandard), "the time of the systematic guessing one.")

