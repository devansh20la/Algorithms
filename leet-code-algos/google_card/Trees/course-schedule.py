class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # create a adjacency matrix
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # visit set
        visit = set()
                
        def dfs(currcourse):
            if currcourse in visit:
                return False
            
            if graph[currcourse] == []:
                return True
            
            visit.add(currcourse)
            
            for p in graph[currcourse]:
                if not dfs(p):return False
            
            visit.remove(currcourse)
            
            graph[currcourse] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True