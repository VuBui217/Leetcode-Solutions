class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Algorithm: convert nums to a set so we can easily check
        # if a number exists in the list
        # Find all the possible sequence in the set
        # Update the len of each sequence on the go 
        # to find the longest sequence

        # Convert the nums to a set
        nums_set = set(nums)
        # Declare the length of the longest consecutive sequence
        # Initialize to zero
        longest_len = 0

        # Iterate the set
        for num in nums_set:
            # Check if the current num is the beginning of a sequence
            if num-1 not in nums_set:
                curr_len = 1 #current of the sequence just found
                # Check if the squence has other elements on the list
                while (num + curr_len) in nums_set:
                    curr_len += 1 # update the length of the current sequence
                # update longest_len
                longest_len = max(longest_len, curr_len)
        return longest_len
        
# Time complexity: O(n)
# Space complexity: O(n)
