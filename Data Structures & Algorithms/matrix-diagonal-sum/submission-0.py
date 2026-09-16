class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # example 1: 1 + 5 + 9 + 2 + 7 = 25
        # first diagonal already adds the middle (intersection of both diagonals) so skip on second

        sum = 0


        count = len(mat) - 1
        for row in range(len(mat)):
            print('row: ' + str(row))
            if row == count and (len(mat) % 2 == 1):

                sum += mat[row][row]
            else:
            
                sum += mat[row][row]
                sum += mat[row][count]
            count -= 1

        return sum