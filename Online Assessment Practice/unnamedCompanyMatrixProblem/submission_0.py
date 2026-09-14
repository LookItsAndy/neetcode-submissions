def solution(matrix):
    
    keys = {}
    col = 0
    for row in range (len(matrix)):
        bounceRow = row
        bounceCol = 0
       # marks beginning of weight calculation
        key = matrix[row][0]
        
        
        while bounceRow > 0:     # when the row has not reached the top to bounce
            # traveling diagonnally upward to right     row -= 1 col += 1
            
            if bounceCol == 0:
                keys[key] = key
            else:
                keys[key] += (matrix[bounceRow][bounceCol])
            
            bounceRow -= 1      # move up
            bounceCol += 1
            
        # after hitting row = 0, flip
        # traverse diagonally downward right
        while bounceCol < len(matrix):
            
            if bounceCol == 0:
                keys[key] = key
            else:
                keys[key] += (matrix[bounceRow][bounceCol])
            
            bounceRow += 1
            bounceCol += 1
            
    sortKey = sorted(keys.items(), key=lambda pairs: (pairs[1], pairs[0]))
    return [key[0] for key in sortKey]
            
        
        
            
            
            
            
        