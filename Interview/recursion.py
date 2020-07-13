"""
This question is asked by Amazon
Q. How many number of ways are their to climb n stairs. Take a vriation of {1,2} once and finally {1,3,5}

"""
import sys

def num_of_ways(n):
    n = int(n)
    if n == 0 or n == 1: return 1
    return num_of_ways(n-1)+num_of_ways(n-2)

def num_of_ways_iteration(n):
    n = int(n)
    if n == 0 or n == 1: return 1
    num = [None] * (n+1)
    num[0] = 1
    num[1] = 1
    for i in range(2, n+1):
        num[i] = num[i-1] + num[i-2]
    return num[n]


def num_of_ways_variation(n, X):
    '''
    The value of item in X shold not exceed value of n
    '''
    n = int(n)
    if n==0: return 1
    x = len(X)
    if x == 2:
        return num_of_ways(n-1)+num_of_ways(n-2)
    if x == 3:
        return num_of_ways(n-1)+num_of_ways(n-2)+num_of_ways(n-3)
    if x == 4:
        return num_of_ways(n-1)+num_of_ways(n-2)+num_of_ways(n-3)+num_of_ways(n-4)


def num_of_ways_variation_iteration(n, X):
    '''
    The value of item in X shold not exceed value of n
    '''
    n = int(n)
    if n==0: return 1
    total = 0
    for i in X: 
        if n-i >=0: total+=num_of_ways_variation_iteration(n-i, X)
    return total

def efficient_num_of_ways(n, X):
    '''
    The value of item in X shold not exceed value of n
    '''
    n = int(n)
    if n==0: return 1
    total = 0
    num = [None] * (n+1)
    num[0] = 1
    for i in range(1, n+1):
        for j in X: 
            if i-j >=0: 
                total+=num[i-j]
        num[i] = total
    return num[n]


if __name__ == "__main__":
    '''
    Call the fuction form command line

    For example:
    python recursion.py num_of_ways 4
    '''
    if sys.argv[3]:
        variation = list(map(int, sys.argv[3: ]))
        print(variation)
        print(globals()[sys.argv[1]](sys.argv[2], variation))
    elif sys.argv[2]:
        print(globals()[sys.argv[1]](sys.argv[2]))