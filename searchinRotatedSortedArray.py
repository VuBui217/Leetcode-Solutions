Link to the problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Algorithm: Using Binary Search
        l, r = 0, len(nums) -1 
        while l <= r:
            mid = l + (r-l)//2
            # case 1: Target found
            if target == nums[mid]:
                return mid
            # L     M      R       Target
            # Case 2: subarray on mid's left sorted
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
