Link to problem: https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Algorithm: Use 2 pointers to calculate the container with most water
        # As we know: area of rectangle = height * width
        # For this problem: area = min(height[i], height[j]) * (j-i)
        # we maximmize our width by using the left and right pointer
        # And maximize the heights on the go and update the max_area at the same time
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            max_area = max(max_area, min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return max_area
