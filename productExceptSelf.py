# Link to problem: https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Solution1
        # n = len(nums)
        # l_mult, r_mult = 1, 1
        # left_factor = [0] * n
        # right_factor = [0] * n 
        # # Calculate the left and right factor of the product
        # for i in range(n): 
        #     # Calculate 2 array at the same time
        #     # i starts at the first elemment
        #     j = -i - 1 # j starts at the last elememt
        #     left_factor[i] = l_mult
        #     right_factor[j] = r_mult
        #     # update the multipliers
        #     l_mult *= nums[i]
        #     r_mult *= nums[j]

        # # return the result
        # return [l*r for l,r in zip(left_factor, right_factor)] 
        # Time Complexity : O(n)
        # Space Complexity: O(n)

        # Solution 2
        # It's pretty similar to solution 1
        # Instead of using 2 array, we only use one array which is result
        # array to calculate everything
        n = len(nums)
        result = [0] * n
        l_mult, r_mult = 1, 1
        # Calcuate the the left factor an update values in result array
        for i in range(n):
            result[i] = l_mult
            l_mult *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            #Result wil be the value of current result(left_fator) time to r_mult(right_factor)
            result[j]*= r_mult
            #Update r_mult on the go
            r_mult *= nums[j]
        return result
        # Time complexity: O(n)
        # Space complexity: O(1)





