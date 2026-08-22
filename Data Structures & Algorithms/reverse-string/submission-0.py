class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        reverseIndex = len(s) - 1
        old_s = s.copy()
        for i in range (len(s)):
            s[i] = old_s[reverseIndex]
            reverseIndex -= 1

    # [n,e,e,t]
    # 0 1 2 3
            
        