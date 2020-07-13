"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def isSumEqualsTarget(iterable, target):
    for i in iterable:
        if target-i in iterable:
            return True
        return False

if __name__ == "__main__":
    total_numbers = int(input("Enter the size of list: "))
    iterable = []
    for i in range(total_numbers):
        num = int(input())
        iterable.append(num)
    target = int(input("Give the input for target: "))
    print(f"The given list: {iterable}")
    print(f"The given target: {target}")
    print(f"Do the sum of any two number equals the target?\t {isSumEqualsTarget(iterable, target)}")