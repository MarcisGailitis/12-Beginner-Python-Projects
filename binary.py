import random
import time


def naive_search(list, target):

    for pos, i in enumerate(list):
        if i == target:
            return pos
    else:
        return -1


def binary_search(list, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(list)-1

    if high < low:
        return -1

    midpoint = (low + high) // 2
    # print(low, midpoint, high)

    if list[midpoint] == target:
        return midpoint

    elif list[midpoint] > target:
        return binary_search(list, target, low, midpoint-1)

    elif list[midpoint] < target:
        return binary_search(list, target, midpoint+1, high)


if __name__ == '__main__':
    nrs = 100_000_000
    list = [i for i in range(nrs)]
    target = random.randint(0, nrs)

    print(f'target {target}')
    t0_naive = time.time()
    print(f'target using naive search {naive_search(list, target)}')
    time_naive = time.time()-t0_naive
    t0_bin = time.time()
    print(f'target using binary search {binary_search(list, target)}')
    time_binary = time.time()-t0_bin

    print(f'{round(time_naive / time_binary)} times faster')
