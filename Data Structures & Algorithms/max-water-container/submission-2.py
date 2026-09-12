class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maxContainer = 0

        while left < right:

            # use water formula: j-i (no abs needed because j is bigger than i) * min(heights[i], heights[j])

            maxContainer = max(maxContainer, (right - left) * min(heights[left], heights[right]))
            
            if heights[left] > heights[right]:  # if left is greater than right, move right
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:    
                right -= 1
                left += 1

        return maxContainer