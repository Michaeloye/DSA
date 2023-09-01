def createNode(val=None, next=None):
    return {"val": val, "next": next}


# 1,2,3
node3 = createNode(3)
node2 = createNode(2, node3)
node1 = createNode(1, node2)

print(node1["next"]["next"])
