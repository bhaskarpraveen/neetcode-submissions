class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = {i:deque() for i in range(numCourses)}
        cycle = set()

        for course in prerequisites:
            prereq[course[0]].append(course[1])

        def dfs(course):
            if course in cycle: return False
            if not prereq[course]: return True
           
            cycle.add(course)
            while prereq[course]:
                if not dfs(prereq[course].pop()):
                    return False

            cycle.remove(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        # print(len(visited),numCourses,cycle)
        return True