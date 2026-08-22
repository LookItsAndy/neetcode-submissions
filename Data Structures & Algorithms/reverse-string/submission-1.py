class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointer swap method


        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]       # this works because python first stores s[right] and s[left] somewhere else
            left += 1                                   # so no need to worry about values being overwritten
            right -= 1
            


    # [n,e,e,t]
    #  0 1 2 3