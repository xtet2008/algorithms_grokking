# coding:utf-8
# @Time : 2019-10-02 18:47 
# @Author : Andy.Zhang
# @Desc : 


graph = {
    'Guitar': {
        'cost': 1,  # day
        'value': 1500
    },
    'Voice': {
        'cost': 4,
        'value': 3000,
    },
    'Notebook':{
        'cost': 3,
        'value': 2000,
    },
    'iPhone':{
        'cost': 1,
        'value': 2000
    }
}

cells = [[0 for col in range(4)] for row in range(4)]
keys = graph.keys()
max_cost = 4
print(cells)

for key_index in range(graph.keys().__len__()):
    row = key_index
    key_cost = graph[keys[key_index]]['cost']
    key_val = graph[keys[key_index]]['value']
    print(keys[key_index], key_cost)

    for cost in range(max_cost):
        capacity = cost + 1
        if capacity >= key_cost:  # can be put in bag
            last_max_value = cells[row-1 if row >0 else 0][cost]  #在该容易下之前能装的最大价值（所以必须是上一行，row-1）
            if row and capacity-key_cost-1 >= 0:  # row > 1  必须得先有剩余容量，第一行肯定不可能有剩余价值，另外容易列需要-1，从0开始
                rest_value = cells[row-1 if row > 0 else 0][capacity-key_cost-1]  #剩余空间价值
            else:
                rest_value = 0
            cells[row][cost] = max(last_max_value, key_val + rest_value)
        else:
            cells[row][cost] = max(cells[row][cost-1 if cost > 0 else 0], cells[row-1 if row > 0 else 0][cost])


print(cells)