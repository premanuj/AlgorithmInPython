"""
Implementation of insertion sort using core python 3

"""

def insertion_sort(collection):
    size = len(collection)

    for i in range(1, size):
        slice_list = collection[:i]
        for j in range(len(slice_list)):
            if collection[i-1] < collection[j]:
                collection[i-1], collection[j] = collection[j], collection[i-1]

    return collection