class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        count = [0] * 26
        window_count = [0] * 26
        for i in range(len(p)):
            count[ord(p[i]) - ord('a')] += 1

        # length of window is the length of string p
        for i in range (len(s) - len(p) + 1):
            if i != 0:
                    window_count[ord(s[i+len(p)-1]) - ord("a")] += 1

            else:   # starting case (sets up the window count hash map)
                for k in range (len(p)):
                    window_count[ord(s[k]) - ord("a")] += 1 # [1, 1, 0, 0, ...]

            # check if window is an anagram
            if window_count == count:
                result.append(i)
            
            # update window_count by removing prev index
            window_count[ord(s[i]) - ord('a')] -= 1

        return result






    
        