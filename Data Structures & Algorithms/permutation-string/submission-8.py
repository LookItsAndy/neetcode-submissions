class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window problem: s1 will determine the sliding window length

        #'abc'      'lecabee'
        # 012        0123456


        #'adc'      'dcda'
        # 012        0123
        
        # how to optimize this Solution: instead of rebuilding entire s2subMap, remove the character leaving the window, so remove inner loop


        # catch edge cases

        if len(s1) > len(s2):
            return False
        s1Map = [0] * 26
        s2subMap = [0] * 26

        # build hash map
        for ch in s1:
            s1Map[ord(ch) - ord('a')] += 1

        # set up the window
        for i in range (len(s1)):
            s2subMap[ord(s2[i]) - ord('a')] += 1

        if s2subMap == s1Map:
            return True


        for i in range (len(s2) - len(s1)):
            
            # check if window matches substring

            # slide the window
            # add next character to the s2 hash map
            s2subMap[ord(s2[i + len(s1)]) - ord('a')] += 1

            # remove old character from the hash map
            s2subMap[ord(s2[i]) - ord('a')] -= 1
            if s2subMap == s1Map:
                return True

        return False
                
                
            


