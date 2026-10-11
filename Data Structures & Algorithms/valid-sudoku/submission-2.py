class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #brute force:
        # first check, row: iterate through each row, add each seen number to a set, check if new current number is inside that set, then that means the board is invalid. 
        # second check, column: iterate thorugh each, use same set method as first check, to check for duplicates
        # third check, 3x3 boxes: 


        # optimized solution: 
        # set for each row
        # set for each column
        # set for each sub-box (use //3 to determine the key value for each sub box)

        rowDict = defaultdict(set)
        columnDict = defaultdict(set)
        subBoxDict = defaultdict(set)


        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in columnDict[col]:
                    return False
                if board[row][col] in rowDict[row]:
                    return False
                if board[row][col] in subBoxDict[(row//3, col//3)]:
                    return False
                
                rowDict[row].add(board[row][col])
                columnDict[col].add(board[row][col])

                subBoxDict[(row//3, col//3)].add(board[row][col])

        
        return True
        

        # time - O(n^2)
        # space - O(n)



