class Solution:
    def firstUniqChar(self, s: str) -> int:
        numberCharacter = {}    # each key gets [index, # times appeared in s]

        for i, ch in enumerate(s):      # enumerate gives the index, and character
            if ch not in numberCharacter:
                numberCharacter[ch] = [i, 1]

            else:
                 numberCharacter[ch][1] += 1
            
        for i, numAppeared in numberCharacter.values():
            if numAppeared == 1:
                return i
        return -1
        
