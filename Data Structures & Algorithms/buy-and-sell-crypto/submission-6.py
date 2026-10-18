class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        left, right = 0, 1

        while right < len(prices):
            profit = prices[right] - prices[left]

            if prices[right] < prices[left]:    # if next day prices are lower than left, 
                # make right day the new left
                left = right
            else:   # if prices[right] is bigger than left, then there is profit to make
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
        return maxProfit
