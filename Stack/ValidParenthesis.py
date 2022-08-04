# https://leetcode.com/problems/valid-parentheses/


def isValid(s):

    d = {"(": ")", "{": "}", "[": "]"}

    stack = []

    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False

    return len(stack) == 0


s = "()[]"
print(isValid(s))
