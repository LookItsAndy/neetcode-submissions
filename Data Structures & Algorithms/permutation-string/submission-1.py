class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window problem: s1 will determine the sliding window length

        s1Map = [0] * 26

        for ch in s1:
            s1Map[ord(ch) - ord('a')] += 1

        
        #'abc'      'lecabee'
        # 012        0123456


        #'adc'      'dcda'
        # 012        0123
        
        for i in range (len(s2) - len(s1) + 1):
            s2subMap = [0] * 26
            for j in range(len(s1)):
                s2subMap[ord(s2[i + j]) - ord('a')] += 1

            if s2subMap == s1Map:
                return True


        return False
                
                
            


