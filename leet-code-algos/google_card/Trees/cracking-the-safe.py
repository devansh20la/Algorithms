class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join([str(_) for _ in range(k)])
        
        # Hierholzer's algorithm to find euler's path/circuit in the graph
        # Euler circuit is a path that traverses every edge of a graph, and the path ends on the starting vertex.
        # create a graph with all nodes of n -1 digits
        adjlist = defaultdict(list)
        for comb in product(range(k), repeat=n):
            adjlist["".join(map(str, comb[:-1]))].append("".join(map(str, comb[1:])))
                
        path = []
        def dfs(node):
            while(adjlist[node]):
                dfs(adjlist[node].pop())
            path.append(node[0])
        
        start_node = "0"*(n-1)
        dfs(start_node)
        return "".join(path[::-1] + ["0"*(n-2)])
        