class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alist = []
        nums.sort()
        for n in nums:
            if n in alist:
                return True
            alist.append(n)
        return False