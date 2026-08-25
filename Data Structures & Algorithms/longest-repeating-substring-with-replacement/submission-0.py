class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # intuitiion: use frequency map count to track the number a character has appeared. the logic uses
        # the length of window - highest number of characters inside window <= k
        # as long as that is true, then there are enough replacements to be made. change maxLength to return later
        # if the number of replacements to be made exceeds the replacements given, must shrink the window and decrement the character count
        maxLength = 0
        left, right = 0, 0
        count = [0] * 26

        while right < len(s):
            count[ord(s[right]) - ord('A')] += 1
            windowLength = right - left + 1
            if not (windowLength - max(count) <= k):        # if the num replacements exceeds k, shrink the window
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right +=1

        return maxLength



