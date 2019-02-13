# coding:utf-8
# 狄克斯特拉算法(求最短路径)

# the graph 记录了整个图中的每个点，以及该点到期邻居点的距离（边长）
graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}
}

# the costs table 记录了从起点到每个点的总距离（终点因为暂时不知道，就默认当：无穷大）
costs = {
    "a": 6,
    "b": 2,
    "fin": float("inf")  # 无穷大
}

# the parents table 记录了每个点之间的上一层路径关系，默认按图表示上一层的路径关系，后续算法每次找到了更短距离就会更新其关系
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")  # 默认为无穷大
    lowest_cost_node = None  # 最短路径尚未知道
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # Find the lowest-cost node that you haven't processed yet.
while node is not None:  # If you've processed all the nodes, this while loop is done.
    cost = costs[node]

    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for key in neighbors.keys():
        new_cost = cost + neighbors[key]
        if costs[key] > new_cost:  # If it's cheaper to get to this neighbor by going through this node...
            costs[key] = new_cost  # ... update the cost for this node.
            parents[key] = node  # This node becomes the new parent for this neighbor.

    processed.append(node)  # Mark the node as processed.
    node = find_lowest_cost_node(costs)  # Find the next node to process, and loop.

print("Cost from the start to each node:")
print(costs)
print(parents)