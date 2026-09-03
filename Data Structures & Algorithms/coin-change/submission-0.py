class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # example: [1,5,10] amount = 12, output = 3

        # recursion, to find least amount of coins needed, we need to search every single possibility
        
        memo = {}
        def minChange(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float("inf")
            
            if remaining in memo:
                return memo[remaining]

            best = float("inf")

            for coin in coins:
                minimum = 1 + minChange(remaining - coin)
                best = min(best, minimum)

            memo[remaining] = best
            return best

        result = minChange(amount)
        return -1 if result == float('inf') else result