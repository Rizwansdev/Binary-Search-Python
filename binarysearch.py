
# Proving Binary search is faster than Naive Search

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target):
    # example l = [1, 3, 5, 10, 12]

    midpoint = (len(l)) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]: