# 0 index based graph
def breadthFirstSearch(n, graph):
    queue = [0]
    visitedNodes = [0] * (n)
    bfs = []

    while len(queue):
        currNode = queue[0]
        queue.pop(0)
        bfs.append(currNode)
        if not visitedNodes[currNode]:
            visitedNodes[currNode] = 1
        for i in graph[currNode]:
            if not visitedNodes[i]:
                queue.append(i)
                visitedNodes[i] = 1

    return bfs


# 1 index based graph
def breadthFirstSearch(n, graph):
    queue = [1]
    visitedNodes = [0] * (n + 1)
    bfs = []

    while len(queue):
        currNode = queue[0]
        queue.pop(0)
        bfs.append(currNode)
        if not visitedNodes[currNode]:
            visitedNodes[currNode] = 1
        for i in graph[currNode]:
            if not visitedNodes[i]:
                queue.append(i)
                visitedNodes[i] = 1

    return bfs


# 1 index based example
# print(breadthFirstSearch(8, {1: {2, 6}, 2: {1, 3, 4}, 3: {
#       2}, 4: {2, 5}, 5: {4, 7}, 6: {8, 1, 7}, 7: {5, 6}, 8: {6}}))
