import random


def recursive_sum(arr):
    _tmp = 0
    if arr.__len__() == 0:
        return 0
    elif arr.__len__() == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])


print (recursive_sum([1, 3, 5]))
print (recursive_sum([0]))


def recursive_count(arr):
    if arr == []:
        return 0
    else:
        return 1 + recursive_count(arr[1:])


print (recursive_count([]))
print (recursive_count([0]))
print (recursive_count([1, 3, 5]))


def recursive_max(arr):
    if arr.__len__() == 0:
        return None
    elif arr.__len__() == 1:
        return arr[0]
    else:
        _sub_max = recursive_max(arr[1:])
        return arr[0] if arr[0]> _sub_max else _sub_max


print (recursive_max([1, 5, 3]))


# the worst times: O(n*n), the average times: O(n * log n)
stack_hight = 0


def quick_sort(arr):
    global stack_hight
    stack_hight += 1
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(larger)


print (quick_sort([5, 3, 7, 2, 6, 4]))
print ('\n')
print (quick_sort([5, 3, 7, 2, 6, 4, 8, 1, 9, 4, 10, 0, 24, 21, 25, 23, 22, 26, 27, 30]))
print ('in quick_sort, stack_hight=', stack_hight)


stack_hight = 0


# support random pivot selection for quick_sort
def quick_sort_random_pivot(arr):
    global stack_hight
    stack_hight += 1
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(random.randint(0, len(arr)-1))
        less = [i for i in arr if i <= pivot]
        larger = [i for i in arr if i > pivot]
        return quick_sort_random_pivot(less) + [pivot] + quick_sort_random_pivot(larger)


print ('\n')
print (quick_sort_random_pivot([5, 3, 7, 2, 6, 4, 8, 1, 9, 4, 10, 0, 24, 21, 25, 23, 22, 26, 27, 30]))
print ('in quick_sort_random_pivot, stack_hight=', stack_hight)