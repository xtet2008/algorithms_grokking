# coding:utf-8
# 狄克斯特拉算法(求最短路径，用乐谱以最小的花费交换钢琴问题)

# 存储所有的节点，以及每个节点所有的邻居
graph = {
    'score': {
        "album": 5,
        "poster": 0
    },
    "album": {
        "guitar": 15,
        "drum": 20
    },
    "poster": {
        "guitar": 30,
        "drum": 35
    },
    "guitar": {
        "piano": 20
    },
    "drum": {
        "piano": 10
    },
    "piano": {}  # 终于没有邻居
}

# 存储每个节点的开销 (从起点到该节点的花费)，后期运算需要不断更新这个花费表（如果找到比现在默认更低的花费情况下）
costs = {
    "album": 5,
    "poster": 0,
    "guitar": float('inf'),  # 对于尚未知的开销先假设为无穷大，方便后期发现有小于这个开销的case就更新这个值
    "drum": float('inf'),  # 对于尚未知的开销先假设为无穷大
    "piano": float('inf')  # 对于尚未知的开销先假设为无穷大
}

# 存储每个节点的父节点，后期运算需要不断不断这个父节点表（如果找到比现在默认更短的路径情况下）
parents = {
    "album": "score",  # "child": "parent"
    "poster": "score",
    "guitar": None,  # 对于有多个父节点的情况下，我们不知道哪个路径最短，先默认为None空，后期找到最短路径再更新其父节点信息
    "drum": None,
    "piano": None
}

processed = []  # 存储处理过的节点，对于同一个节点，不用处理多次

'''伪代码如下
1，从costs节点开销图表中遍历所有的节点，找出待处理的节点 （找出开销最小，最便宜的那个节点，即：离起点最近的节点，并且该点还要未被处理过）
2，重新计算经该节点到其所有邻居所需的开销花费，如果找到更小的开销花费，则更新期邻居开销（如果邻居开销被更新，则同时更新期父节点）
3、将该节点标记为处理为，并循环返回到步骤1
4、最终被更新的 costs 存储的就是从起点到终点（以及途径各点）的最短路径开销，parents 存储的为从起点到终点的最短开销路径子父关系
'''


# 遍历图中各个点，每次找到并返回从起点算，最小开销的那个节点名
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")  # 默认无穷大
    lowest_cost_node = None # 假设待返回的最短路径节点名尚未知道

    # 遍历所有节点
    for node in costs:
        cost = costs[node]  # 获取当前节点的开销
        if cost < lowest_cost and node not in processed:  # 如果当前节点小于目前最小节点的开销，并且尚未处理过
            lowest_cost = cost  # 则更新更小开销节点信息，并将当前节点名作为此函数待返回的结果
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)  # 从节点开销图中找出开销最小的那个节点名
while node is not None:  # 假设找到了开销最小的节点
    cost = costs[node]  # 获取其开销值

    # 遍历该节点所有的邻居，并重新计算经该节点到其所有邻居节点的开销
    neighbors = graph[node]
    for key in neighbors.keys():  # key 代表该节点的所有邻居节点名
        new_cost = cost + neighbors[key]  # 计算经该节点到期邻居点的总开销
        if new_cost < costs[key]:  # 如果经该节点到期邻居点的开销 小于 开销表中 costs原先存储的其邻居点的开销值
            costs[key] = new_cost  # 在开销表中更新期邻居节点的开销值
            parents[key] = node  # 同时在子父节点表中更新期邻居点的父节点为当前节点，代表着经由当前节点的路径最短

    processed.append(node)  # 更新完该节点的所有邻居后代表着该节点已经处理完，后续在节点开销表中寻找最小开销点的函数中不会再重复处理该节点
    node = find_lowest_cost_node(costs)  # 继续在开销表中遍历找出其他尚未处理节点列表中，开销最短的点，看能尚找出到终点的更短路径

print ("Cost from the start to each node:")
print (costs), (" # 'node': 'cost'")
print (parents), (" # 'child': 'parent'")