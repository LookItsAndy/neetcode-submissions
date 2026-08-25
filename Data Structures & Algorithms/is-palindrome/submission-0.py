class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(s) - 1
        for i in range (len(s)//2):
            
            if (s[right] == s[left]):
        
                left += 1
                right -= 1
                continue
            else: 
                return False

        return True