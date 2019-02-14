# coding:utf-8
# 动态规划算法


# 求两字符串中最长公共子串（最长公共子序列）：两个单词中都有的序列包含的字母数，例如Word中的拼写检查，纠正功能
def count_sequence_word(word_a, word_b):
    cell = [[0 for col in word_b] for row in word_a]
    match_words = []
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                match_words.append(word_a[i])
                # 如果字母相同，则用左上角单元格（行-1,列-1)的值+1
                cell[i][j] = cell[0 if i-1 < 0 else i-1][0 if j-1 < 0 else j-1] + 1  # 需要考虑是否第一行或第一列的情况
            else:
                # 如果字母不同，则用左边单元格(col-1)和上面单元格(row-1)的值比较并取最大值
                cell[i][j] = max(cell[0 if i-1 < 0 else i-1][j], cell[i][0 if j-1 < 0 else j-1])
    print word_a, '&', word_b, '=', match_words, ",", cell[i][j], ' words matched'


count_sequence_word("zhang", "sheng")
count_sequence_word("fort", "fosh")
count_sequence_word("fish", "fosh")
count_sequence_word("ang", "zhang")
count_sequence_word("zhang", "ang")


# 旅游行程最优化问题 (两天的旅游行程选择哪几个地点能旅游价值最大化)
graph = {
    '特教堂': {
        'cost': 0.5,  # day
        'value': 7
    },
    '剧场': {
        'cost': 0.5,
        'value': 6,
    },
    '美术馆':{
        'cost': 1,
        'value': 9,
    },
    '博物馆':{
        'cost': 2,
        'value': 9
    },
    '大教堂':{
        'cost': 0.5,
        'value': 8
    }
}
keys = graph.keys()
columns = [0.5, 1, 1.5, 2]  # column = graph.cost
last_row = 0
cell = [[0 for col in columns] for row in graph.keys()]
cell_selection_keys = {}
last_selection_keys = []
rest_selection_keys = []


def get_col_index(value):
    for index, element in enumerate(columns):
        if element == value:
            return index
    else:
        return -1  # default value


for row in range(len(keys)):  # row = graph.key.index
    for col in range(len(columns)):
        last_row = 0 if row-1 < 0 else row-1
        last_max_value = cell[last_row][col]  # 上一行同列单元格永远为目前为止最大值
        if row == 0:
            last_max_selection = cell_selection_keys['0,' + str(col-1)] if col else []
        else:
            last_max_selection = cell_selection_keys[str(last_row) + ',' + str(col)]
        current_key = keys[row]
        current_key_cost = graph[current_key]['cost']  # 当前商品(地点)所对应的开销
        current_col_cost = columns[col]  # 当前开销列对应的值

        if current_col_cost < current_key_cost:  # 当前列对应的开销容量不满足当前key所对应的cost，即不满足条件，包装不下
            cell[row][col] = last_max_value  # 将之前所求出的最大值保存起来 （永远保证到最后一格是保存的是最大值)
            cell_selection_keys[str(row) + ',' + str(col)] = last_max_selection
            last_selection_keys = cell_selection_keys[str(row) + ',' + str(col)]
        else:  # >= current_key_cost  # 如果当前开销列的值 >= 当前商品所对应的开销值，即满足特定条件，包装得下
            current_key_value = graph[keys[row]]['value']  # 当前key的分值

            rest_col_max_value = get_col_index(current_col_cost - current_key_cost)  # 获取剩余容量中存储最大值的列号index
            if rest_col_max_value != -1 and row > 0:  # 如果有剩余容量并且，不是第一行的情况下，才有可能获取剩余容量的最大价值
                rest_value = cell[last_row][rest_col_max_value]  # 如有剩余容量话，才有剩余价值
            else:
                rest_value = 0  # 如果没有剩余容量或第一行的情况下，根本不存在剩余容量最大值的存在，所以为0

            cell[row][col] = max(last_max_value, current_key_value + rest_value)

            if row == 0:  # 如果第一行，特殊处理，直接存储当前key对应的信息
                last_selection_keys = [current_key]
                cell_selection_keys[str(row) + ',' + str(col)] = last_selection_keys
            else:
                # if rest_col_max_value >= 0 and current_key_value + rest_value > last_max_value:  # 如果有剩余容量并且 当前价值 + 剩余空间最大价值 > 目前存储最大值，则更新背包
                if current_key_value + rest_value > last_max_value:  # 如果有剩余容量并且 当前价值 + 剩余空间最大价值 > 目前存储最大值，则更新背包
                    if rest_col_max_value >= 0:
                        rest_selection_keys = cell_selection_keys[str(last_row) + ',' + str(rest_col_max_value)]  # 剩余容易最大值keys
                    else:
                        rest_selection_keys = []
                    cell_selection_keys[str(row) + ',' + str(col)] = rest_selection_keys + [current_key]  # 背包添加
                    last_selection_keys = cell_selection_keys[str(row) + ',' + str(col)]  # 记录目前最佳的选择
                else:  # 还不如以前最大价值大（或差不多），那没必要更新背包，就选择以前的背包就好了
                    last_selection_keys = cell_selection_keys[str(last_row) + ',' + str(col)]  # 获取之前最大背包存储的选择值
                    last_selection_keys = last_selection_keys if last_selection_keys else []  # 考虑{}字典中找不到，返回None的情况
                    cell_selection_keys[str(row) + ',' + str(col)] = last_selection_keys

print ('\nbest state selection:')
for i in range(len(last_selection_keys)):
    print last_selection_keys[i], ':', graph[last_selection_keys[i]]
# 最后一次最佳的背包选择值
print 'total value:', cell[-1][-1]  # 数组的最后一行，最后一列存储的为最大值