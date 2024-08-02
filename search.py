Link to the problem: https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Algorithm: Binary search
        l, r = 0, len(nums)-1

        while l <= r: 0 < 5 3<5 3 = 3
            m = (r + l) // 2 # Potential overflow if len(nums) is too large
            # Use this instead m = l + ((r-l)//2)
            if (nums[m] == target): 
                return m
            elif (nums[m] > target):
                r = m - 1 # 3
            elif (nums[m] < target):
                l = m + 1 # 3
        return -1
