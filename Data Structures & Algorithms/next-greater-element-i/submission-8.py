class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        pairs = {}
        stack = []
        result = []

        # nums1 = [1,2,3]       nums2 = [1,3,2,4]
        # pairs = {1:3, 2:4, 3:4}
        # stack = [3, 2] 4

        for i in range(len(nums2)):

            if i == 0:
                stack.append(nums2[i])
                continue

            elif stack[-1] > nums2[i]:
                stack.append(nums2[i])

            while stack and stack[-1] < nums2[i]:
                small = stack.pop()
                pairs[small] = nums2[i]
                print(stack)
            stack.append(nums2[i])
            
        print(str(pairs))
        for num in nums1:
            if num in pairs:
                result.append(pairs[num])
            else:
                result.append(-1)

        return result


        # for each number in nums1, we need to find out if there is a greater value than it in the nums2 array if its to the right side.

        # the first greater array










        # nums2 = [1,3,4,2]
        
        # nums1 = [4,1,2]

        # stack =[1,3]
        # maxSeen = 2
        # popped = 2 
        # result = [-1]
        # for num in nums1:

        #     stack = nums2
        #     maxSeen = 0
        #     while stack:
        #         popped = stack.pop()
        #         maxSeen = max(maxSeen, popped)
        #         if num == popped:
        #             if maxSeen > num:
                    
        #                 result.append(max)
        #             else:
        #                 result.append(-1)
            

        # return result


