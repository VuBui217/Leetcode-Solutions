Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Algorithm: Using 2 pointers
        maxProfit = 0 # max profit
        lowest = prices[0] # left pointer to maintain the lowest price
        for price in prices: # right pointer 
            if price < lowest: #if the current price < lowest, update lowest
                lowest = price
            maxProfit = max(maxProfit, price-lowest) #maxProfit will be max of curretn maxProfit and new profit
        return maxProfit
