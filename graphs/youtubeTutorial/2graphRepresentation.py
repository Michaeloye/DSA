
# 0(N^2)
def matrixGraphRepresentation():
    # nodes
    n = int(input("Enter number of nodes: "))
    # edges
    m = int(input("Enter number of edges: "))

    print("### edges ###")
    # create graph
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(m):
        u = int(input("Enter  node: "))
        v = int(input(f"node {u} connects to: "))

        graph[u][v] = 1
        graph[v][u] = 1

    for j in graph:
        print(j)
# matrixGraphRepresentation()


# 0(2 * M) undirected
def listGraphRepresentation():
    # nodes
    n = int(input("Enter number of nodes: "))
    # edges
    m = int(input("Enter number of edges: "))

    print("### edges ###")

    graph = {i: set() for i in range(n + 1)}

    for i in range(m):
        u = int(input("Enter node: "))
        v = int(input(f"node {u} connects to: "))

        graph[u].add(v)
        graph[v].add(u)

    print(graph)


# listGraphRepresentation()


def matrixGraphWithWeightRepresentation():
    # nodes
    n = int(input("Enter number of nodes: "))
    # edges
    m = int(input("Enter number of edges: "))

    print("### edges ###")
    # create graph
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = input(
            "Enter  node, connecting node, edge weight (u, v, w): ").split(',')

        u = int(u)
        v = int(v)
        w = int(w)

        graph[u][v] = w
        graph[v][u] = w

    for j in graph:
        print(j)


matrixGraphWithWeightRepresentation()


def listGraphWithWeightRepresentation():
    # nodes
    n = int(input("Enter number of nodes: "))
    # edges
    m = int(input("Enter number of edges: "))

    print("### edges ###")

    graph = {i: set() for i in range(n + 1)}

    for _ in range(m):
        u, v, w = input(
            "Enter  node, connecting node, edge weight (u, v, w): ").split(',')

        u = int(u)
        v = int(v)
        w = int(w)

        graph[u].add((v, w))
        graph[v].add((u, w))

    print(graph)


listGraphWithWeightRepresentation()
