class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:
            # target is within this row if bounds are valid
            if row[0] <= target and row[len(row)-1] >= target:

                # should implemeent a binary search algorithm here
                left = 0
                right = len(row) - 1
                mid = (left + right) // 2
                
                while left <= right:

                    if row[mid] > target:   # if middle is greatter than target, then move right pointer to mid
                        right = mid - 1
                    elif row[mid] < target:
                        left = mid + 1
                    elif row[mid] == target:
                        return True

                    mid = (left + right) //2



        return False