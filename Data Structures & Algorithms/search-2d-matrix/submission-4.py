class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:
            # target is within this row if bounds are valid
            if row[0] <= target and row[len(row)-1] >= target:
                for col in row:
                    if col == target:
                        return True 


        return False