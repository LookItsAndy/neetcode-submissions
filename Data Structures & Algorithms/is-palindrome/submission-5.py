class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left, right = 0, len(s) - 1


        while left < right:

            while left < right and not s[left].isalnum():    # if character is not alphanumeric, move pointer
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1 

            if not s[left] == s[right]:
                return False

            left += 1
            right -= 1

        return True


