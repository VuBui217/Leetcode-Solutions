Link to problem: https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1: Use built in library 
        # Create an extra string to store only alphanumeric characters
        # new_str = ""
        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()
        # return new_str == new_str[::-1]

        # Solution 2: Using 2 pointers and make your own isalnum function
        # left pointer starts at the firt character of the string
        l = 0
        # right pointer starts at the last character of the string
        r = len(s) - 1
        while l <= r:
            # increase l until see the character or number
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            # decrease r until see the character or number
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            # Compare 2 characters, if they are not the same -> not valid palindrome
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def isAlphaNum(self, c: chr) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
