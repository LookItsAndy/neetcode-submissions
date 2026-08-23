class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # acm solution
        result = []
        path = []

        def backtrack(start):
            # base case
            if len(path) == k:
                result.append(path[:])
            else:
                for i in range(start, n + 1):   # 1, 2, 3, 4
                    path.append(i)
                    backtrack(i + 1)
                    path.pop()
                # undo the choice

        backtrack(1)
        return result