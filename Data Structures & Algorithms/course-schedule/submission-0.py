class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courses = {i:[] for i in range(numCourses)}
        for course in prerequisites:
            courses[course[0]].append(course[1])
            
        def dfs(course):
            if course in visited: return False
            if courses[course]==[]: return True

            visited.add(course)
            for c in  courses[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            courses[course]=[]
            return True
            

        for course in courses:
            if not dfs(course):
                return False
        return True
        
        


        

        