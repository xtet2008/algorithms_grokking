# coding:utf-8
# 贪婪算法（近似算法求最接近目标结果）

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  # 包含要覆盖的州
stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}
final_stations = set()  # 存储最终选择的广播台
final_states = set()  # 存储最终覆盖的州（近似值)

while states_needed:  # 不断循环，直到要覆盖的集合为空（即：都找到相应的广播台包含期子集了）
    best_station = None  # 最佳广播台（即该台里覆盖的未覆盖的洲数量最多）
    states_covered = set()  # 包含该广播台里覆盖的所有尚未覆盖的州的交集

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # 当前广播台中包含的所有州与目标州列表求 交集
        if len(covered) > len(states_covered):  # 如果当前广播台覆盖的州数比 最佳广播台覆盖的州数还多的话，则更新当前广播台为最佳广播台
            best_station = station
            states_covered = covered

    states_needed -= states_covered  # 将这些覆盖的州 要覆盖的所有州总集合中移除，即：后面判断交集的时候不需要覆盖这些州了
    final_stations.add(best_station)  # 将最佳广播台添加到最终选择的广播台集合中
    final_states |= states_covered

print (final_stations), (' # stations')
print (final_states), (' # states')
