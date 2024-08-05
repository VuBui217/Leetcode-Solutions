Link to the prolem: https://leetcode.com/problems/koko-eating-bananas/editorial/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Algorithm: Brute Force Solution
        # Notice that the time taken to eat x bananas in a pile is
        # speed/x after rounding up to the closest integer
        # Start with speed = 1, calculate the total will take for that speed
        # Until we meet the condition
        # Time complexity: O(n*m) with n is the length of piles, and m is the upper bound of elements in piles 
        # speed = 1
        # while True:
        #     total_hour = 0
        #     for pile in piles:
        #         total_hour += math.ceil(pile / speed)
        #     if (total_hour <= h):
        #         return speed
        #     else:
        #         speed += 1

        # Algorithm 2: Optimal Solution - Using Binary Search
        # Notice that the speed will range from 1 to max num in piles
        # Apply binary search to find the minimum speed 
        l = 1
        r = max(piles)
        speed = r
        while l <= r:
            mid = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return speed
