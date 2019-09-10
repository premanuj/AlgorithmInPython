"""
Implementation of bubble sort using core python3

"""

def bubble_sort(collection):
    size = len(collection)
    for i in range(size-1):
        for j in range(i+1, size-i):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]
    return collection

if __name__ == "__main__":
    raw_collection = input("Enter numbers seperrated by commas: \n")
    collection = [int(i) for i in raw_collection.split(",")]
    print(bubble_sort(collection))
    