"""

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

def missing_positive(iterable):
    iterable.sort()
    for i, num in enumerate(iterable):
        if num < 0:
            continue
        if len(iterable) <= i and num != iterable[i+1]-1:
            return num+1
    else:
        return "No missing number"

if __name__ == "__main__":
    iterable = [int(i.strip()) for i in input("Enter the number seperated by commas: ").split(",")]
    print(missing_positive(iterable))