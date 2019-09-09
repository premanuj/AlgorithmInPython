"""

Pure python implementation of binary search algorithm

For doc run following command.

python -m doctest -v binary_search.py

To run file use following command

python -m binary_search.py

"""

#imports
import bisect

def binary_search(sorted_collection, item):
    """
    Prerequists: collections must be sorted in accending order

    :param sorted_collection: any accending sorted collections
    :param item: item to search
    :return: index of item from sorted_collection or none if not found

    Examples:

    >>> binary_search([0, 1, 3, 5, 8, 9], 8)
    4

    >>> binary_search([0, 1, 3, 5, 8, 9], 3)
    2

    """

    left = 0
    right = len(sorted_collection)-1

    while left <= right:
        midpoint = left + (right-left)//2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None

if __name__ == "__main__":
    user_input = input("Enter the numbers seperated by commas: ")
    collections = [int(i) for i in user_input.split(",")]

    find_item = int(input("Enter the number to search: "))
    result = binary_search(collections, find_item)
    
    if result:
        print(f'{find_item} found in {result}')
    else:
        print("The item you are looking is not found.")