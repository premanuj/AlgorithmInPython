"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def prod(iterable):
    result = 1
    for i in iterable:
        result*=i
    return result

def new_list_with_division(iterable):
    result = []
    product = prod(iterable)
    for i in iterable:
        result.append(product//i)
    return result

def new_list_without_division(iterable):
    result = []
    for i, _ in enumerate(iterable):
        result.append(prod(iterable[i+1:]))
    return result

if __name__ == "__main__":
    total_numbers = int(input("Enter the size of list: "))
    iterable = []
    for i in range(total_numbers):
        num = int(input())
        iterable.append(num)
    print(f"The given list: {iterable}")
    print(f"The new list using division: {new_list_with_division(iterable)}")
    print(f"The new list without using division: {new_list_with_division(iterable)}")
        