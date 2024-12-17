link to problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Algo: Use a pointer to keep track unique number when
        # traversal the array and update the array on the go
        # Start the pointer at 1 cause we always guarantee that array has at
        # least one unique number
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # Update the array 
                nums[left] = nums[i]
                # update the pointer for next checking
                left+=1
        return left
