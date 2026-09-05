class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window


        count = [0] * 26        # frequency map for letters
        result = 0

        left = 0
        maxCount = 0
        s = s.lower()
        for right in range(len(s)):
            
            count[ord(s[right]) - ord('a')] += 1
            maxCount = max(maxCount, count[ord(s[right]) - ord('a')])
            while (right-left + 1 - maxCount > k):
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
                

            result = max(result, right - left + 1)
        return result
            
            

