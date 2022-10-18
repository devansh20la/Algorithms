class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(defaultdict)
        
        #build graph
        for (p, q), v in zip(equations, values):
            self.graph[p][q] = v
            self.graph[q][p] = 1/v
        
        results = []
        for p,q in queries:
            if p not in self.graph or q not in self.graph:
                res =  -1.0
            elif p == q:
                res = 1.0
            else:
                visited = set()
                res = self.backtrack(p, q, 1, visited)
            
            results.append(res)
        
        return results
    
    def backtrack(self, curr_node, target_node, acc_product, visited):
        visited.add(curr_node)
        ret = -1.0
        neighbors = self.graph[curr_node]
        if target_node in neighbors:
            ret = acc_product * neighbors[target_node]
        else:
            for n, v in neighbors.items():
                if n in visited:
                    continue
                ret = self.backtrack(n, target_node, acc_product * v, visited)
                if ret != -1.0:
                    break
            visited.remove(curr_node)
        return ret
        
            