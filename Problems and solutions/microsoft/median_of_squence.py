"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""
from decimal import Decimal


def median(iterable):
    iterable = sorted(iterable)
    if len(iterable) % 2 == 0:
        start_i = int(len(iterable) / 2)
        return Decimal((iterable[start_i - 1] + iterable[start_i]) / 2)
    index = int(len(iterable) / 2)
    return iterable[index]


if __name__ == "__main__":
    sequence = [2, 1, 5, 7, 2, 0, 5]
    for i, _ in enumerate(sequence):
        print(median(sequence[: i + 1]))

