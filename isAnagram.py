link to problem: https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Alg: use 2 hashmaps to store the occurences of every character 
        # in each string
        # Then compare 2 hashmaps, it return True which means t is an anagram
        # of s, otherwise return false
        if len(s) != len(t):
            return False
        s_hashmap = {}
        t_hashmap = {}
        for i in range(len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i],0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i],0)
        return s_hashmap == t_hashmap
