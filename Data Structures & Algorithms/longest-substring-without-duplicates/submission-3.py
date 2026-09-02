class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use left and right pointers, move left pointer. if left sees existing ch, move right pointer, and remove ch it sweeps until duplicate ch is out of set.
        seen = set()
        left = 0
        longest = 0
        

        for right in range (len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
                




