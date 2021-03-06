"""
Implementation of selection sort using python

"""

def selection_sort(collection):
    size = len(collection)

    for i in range(size-1):
        least = i
        for j in range(i+1, size):
            if collection[j] <= collection[least]:
                least = j
        collection[least], collection[i] = collection[i], collection[least]
    return collection


if __name__ == "__main__":
    user_input = input("Enter the collection of numbers: ").strip()
    random_numbers = [int(item) for item in user_input.split(',')]
    print(selection_sort(random_numbers))