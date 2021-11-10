#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/ #

import os

def isBalanced(s):
    if len(s) % 2 != 0:
        # If the string is not even it's impossible for it to be balanced
        return "NO"
    
    stack = [  ]
    pairs = {
        "{":"}",
        "[":"]",
        "(":")",
    }
    
    for i in range(0, len(s)):
        if s[i] in pairs.keys():
            stack.append(pairs[s[i]])
        elif s[i] in pairs.values():
            if not stack:
                return "NO"
            elif s[i] == stack[-1]:
                stack.pop(-1)
            else:
                return "NO"
    
    if not stack:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()