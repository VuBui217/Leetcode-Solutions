Link to th problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Algorithm: Using Binary Search
        
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            m = (l+r) // 2
            res = min(res, nums[m])
            # 
            if (nums[m] > nums[r]):
                l = m + 1
            else: 
                r = m - 1
        return res
