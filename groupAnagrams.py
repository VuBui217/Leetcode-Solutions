Link to problem: https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Algo: Use a dictionary/hashmap to store the group of anagrams
        # Any 2 words are anagram when they have the same key
        # The key should be immutable, so it can be either a sorted string
        # or a tuple(a list of character frequencies)
        anagrams_dict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)- ord('a')]+=1
            anagrams_dict[tuple(count)].append(word)
        return list(anagrams_dict.values())
