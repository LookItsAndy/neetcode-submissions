class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # better to use two pointer 
        if (len(prices) < 2):
            return 0

        left, right = 0,1
        profit = prices[left] - prices[right]
        maxProfit = 0
        while right < len(prices):
            # want to see when price of right - left is biggest

            # two checks, see if right pointer is bigger or lower than left
            # if lower, move left up and move right up
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]   # if next day is bigger, calculate possible profit)
                maxProfit = max(maxProfit, profit)
            else:
                left = right    # if the right is lower than left, make it the new lowest

            right += 1 

        return maxProfit





