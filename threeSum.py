Link to problem: https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 1: USing 2 pointers
        # Alogorithm: Similarly Two Sum II problem
        # We will sort the array, so all the duplicates will
        # be next to each other. So we can manage the duplicates in
        # nums array

        # Declare the result list 
        results = []
        nums.sort()

        # Iterate the the array to find valid triplets
        for i in range(len(nums)):
            # If current element is positive, break the loop
            # Don't need to check further, because the array is sorted
            # so the rest is all positive numbers.
            if nums[i] > 0:
                break
            # Skip the duplicates after the first element
            # Only call getTriplets fucntion for element with different values
            if (i == 0 or nums[i-1] != nums[i]):
                self.getTriplets(nums, i, results)
        return results
        # Using 2 pointers algorithm to finds the triplets
    def getTriplets(self, nums: List[int], i, results: List[List[int]]):
        l = i + 1
        r = len(nums)-1
        while l<r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else: 
                results.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while (l < r and nums[l] == nums[l-1]):
                    l +=1
            
