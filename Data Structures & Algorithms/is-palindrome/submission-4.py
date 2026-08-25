class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:

            while left < right and not s[left].isalnum():
                #print('ran, skipped: ' + s[left])
                left += 1
            while left < right and not s[right].isalnum():
                #print('ran, skipped: ' + s[right])
                right -= 1
            #print(s[left] + " " + s[right])
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True