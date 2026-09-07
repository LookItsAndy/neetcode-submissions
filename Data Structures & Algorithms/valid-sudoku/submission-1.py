class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use 3 hash sets, row, column, square


        cols = defaultdict(set)      # each col has a set
        rows = defaultdict(set)      # each row has a set
        square = defaultdict(set)   # each square has a set

        # need to fill in each hash set

        for row in range (9):
            for col in range (9):
                # skip "."

                element = board[row][col]
                if element == '.':
                    continue
                if (element in rows[row] or 
                element in cols[col] or 
                element in square[(row//3, col//3)]):
                    return False

                cols[col].add(element)
                rows[row].add(element)
                square[(row//3, col//3)].add(element)

        return True


