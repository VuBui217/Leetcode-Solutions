Link to the problem: https://leetcode.com/problems/valid-parentheses/editorial/
class Solution:
    def isValid(self, s: str) -> bool:
        # Algorithm: Using Stack to solve this
        # For every opening bracket we'll push it to stack
        # When we encounter the closing braket we'll pop the top of the stack
        # If they are diffrent, s is invalid
        # If s i valid, the stack should be empty after the for loop is done
        stack = []
        for c in s:
            if (c == '(' or c == '{' or c == '['):
                stack.append(c)
                continue
            if not stack:
                return False
            top = stack.pop()
            if ((top == '(' and c != ')') or 
                (top == '[' and c != ']') or 
                (top == '{' and c != '}')):
                return False
        return not stack
