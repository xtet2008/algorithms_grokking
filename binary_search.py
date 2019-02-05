def binary_search(list, item):
    low = 0
    high = list.__len__() - 1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid -1
    return None


my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3))
print (binary_search(my_list, 4))