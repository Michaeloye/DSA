
# 0(N^2)
def matrixGraphRepresentation():
  # nodes
  n = int(input("Enter number of nodes: "))
  # edges
  m = int(input("Enter number of edges: "))

  print("### edges ###")
  # create graph
  graph = [[0 for _ in range(n + 1)] for _ in range (n + 1)]

  for i in range(m):
    u = int(input("Enter  node: "))
    v = int(input(f"node {u} connects to: "))

    graph[u][v] = 1
    graph[v][u] = 1

  for j in graph:
    print(j)
matrixGraphRepresentation()

