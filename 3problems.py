# algorithms

# # Problem No.1

# You are given an input string that controls the movement of a robot, each character instructing it to move one step north, south, east or west. E.g. "NW" moves the robot one step north and then one step west, or "SE" moves the robot one step south and one step east. Write a function that counts the number of locations that the robot visits more than once, including possibly its starting point. YOu should ignore any character that are not capital N, S, E or W
# For example:
#   - "NS" returns 1
#   - "WEWNES" returns 2
#   - "SxWxNxN" returns 0
#   - [input] string directions: The string describing the robots movements
#   - [output] integer: The number of locations visited more than once
### PROBLEMA NR 1 
def solution(directions):
    
    mylist = ["W", "E", "N", "S"]
    listoflists = [[0,0]]
    cnt = 0
    mydict = {}
    
    for ch in directions:
        if ch not in mylist:
            continue
        auxlist = listoflists[-1].copy()
        if ch == "W":
            auxlist[0] -= 1
        elif ch == "E":
            auxlist[0] += 1
        elif ch == "N":
            auxlist[1] += 1
        elif ch == "S":
            auxlist[1] -= 1
        listoflists.append(auxlist)
    for i in range(len(listoflists)):
        if listoflists[i] in listoflists[i+1:]:
            mydict.update({f"{listoflists[i][0]}{listoflists[i][1]}":1})
            print(mydict)
    if len(mydict.keys()) == 0:
        return 0
  
    return len(mydict.keys())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# # Problem No.2

# Write a function that displays the longest strict palindrome in a string. A strict palindrome reads exactly the same backwards as it does forwards, and respects all characters and letter case. E.g. "racecar" is a strict palindrome but "Racecar" and "race car" are not. If there is more than one palindrome with the longest length, then your code should display the first of those palindromes.
# For example:
#   - "bob has a racecar" returns "racecar"
#   - "bob has a racecar and a bike" returns "a racecar a"
#   - "anna arrived at noon" returns "anna"
#   - [input] string input: The input string
#   - [output] string: The longest strict palindrome from the input string

# ### PROBLEMA NR 2 
def palindrome(mystr):
    mycopy = mystr[::-1]
    if mystr == mycopy:
        return True
    return False

def solution(input):
    nrmin = 0
    mylist = []
    simplestring = ""
    for idx in range(len(input)):
        for jdx in range(idx, len(input)):
            if palindrome(input[idx:jdx+1]) == True:
                mylist.append(input[idx:jdx+1])
    for elem in mylist:
        if len(elem) > nrmin:
            nrmin = len(elem)
            simplestring = elem
    return simplestring

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# # Problem No.3

# Write a function that takes in two strings and returns the number of words that appear in both strings. For the purpose of this exercise, a word is defined as any consecutive string of letters (a-z, upper or lower case), hyphens or apostrophes - hence spaces and other characters act as word separators. Two words are considered the same if every character in them matches exactly, including the case of each of the letters.
# For example:
#   - "Yes, we all really like pizza." and "Where can we buy pizza around here?" returns 2
#   - "There were four people at dinner." and "There were seven people at dinner." returns 5
#   - [input] string first
#   - [input] string second
#   - [output] integer: The number of words present in both inputs

### PROBLEMA NR 3 
import re

def solution(first, second):
    
    first = re.sub('[^a-zA-Z]+', ' ', first)
    second = re.sub('[^a-zA-Z]+', ' ', second)
    
    firstcopy = []
    secondcopy = []
    
    
    firstcopy = first.split()
    secondcopy = second.split()
    
    cnt = 0
    for word in firstcopy:
        if word in secondcopy:
            cnt += 1
    return cnt