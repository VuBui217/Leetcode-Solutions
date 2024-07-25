Link to problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Algorithm: Using 2 pointers to solve
        # One pointer is at the first element, another on start at the last element
        # Because the 'numbers' is sorted in ascending order
        # Use a while loop to calculate the sum of pair numbers in the array
        # If the current sum is greater than the target. That means we need to move the 
        # right pointer to the left
        # Similarly when the current sum is smaller than target
        # We move 2 pointers until the sum = target
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r + 1]

        # Time complexity: O(n)
        # Space Complexity: O(1)
        #1 2 3 4
        #l = 0 r = 3  1+4 > 3 r = 2
        #l = 0 r = 2  1+3 > 3 r = 1
        #l = 0 r = 1  1+2 = 3 r = 1  
