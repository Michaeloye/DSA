# PROBLEM REF: geek for geeks


from collections import defaultdict

#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):

    currNumMap = defaultdict(int)

    #your code here
    def isSafe(node, num):
        # check all adjacent nodes of current node
        for i in range(V):
            if graph[node][i] and currNumMap[i] == num:
                return False
        
        return True

    def dfs(node):
        if node == V:
          return True
    
        for i in range(1, k + 1):
          if isSafe(node, i):
            currNumMap[node] = i
            # run dfs on next node
            if dfs(node + 1):
              return True
    
            currNumMap[node] = 0
    
        return False
    return dfs(0)
