class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting solution: sort each string in alphabetical order
        # compare the two strings, check if they are the exact same, return true, if not return false
        # O(nlogn)

        # s = "jar" , t= "arj"
        # s = "ajr" , t = "ajr" 
        # compare both strings, since same, return true


        # map1 = [0] * 26, map2 = [0] * 26
        # take id of each character in string using ord and append it to correlating index
        # check if each array are the same after going through each string
        # O(2n) = O(n)



        map1 = [0] * 26
        map2 = [0] * 26

        if len(s) != len(t):
            return False

        #s = "abc"  t = "cba"
        for ch in s:
            map1[ord(ch) - ord("a")] += 1
        #   map1 = [1,1,1,0,0,0,0...]
        
        for ch in t: 
            map2[ord(ch) - ord("a")] += 1

        # map2 = [1,1,1,0,0,0,0,...]
        if map1 == map2:
            return True
        return False



