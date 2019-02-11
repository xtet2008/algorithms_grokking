# coding:utf-8
# 宽度优先算法示例

from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jony"] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    searched = []  # this array is how you keep track of which people you've searched before.
    search_queue = deque()
    search_queue += graph[name]

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
