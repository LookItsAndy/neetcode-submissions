class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        preMap = {i:[] for i in range(numCourses)}      # this fills every key with empty [] for numCourses-1 amount

        # [0,1]
        # course, prerequisites

        # track the prerequisites each course has 
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()        # visitSet tracks the nodes that have been visited

        def dfs(course):
            # base case
            if course in visitSet:
                # if course is looped then return False
                return False
            if preMap[course] == []:
                # no more prerequisites to check,
                return True
            visitSet.add(course)

            for pre in preMap[course]:
                if not dfs(pre): return False
            
            visitSet.remove(course)
            preMap[course] = []
            return True


        for course in range (numCourses):
            if not dfs(course): return False
        return True
