import json
from cache_utils import open_cache, save_to_cache


def sort(arr):
    build_min_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
    print(arr)


def build_min_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        sink(arr, i, len(arr))


def sink(arr, root, end):
    if root >= end:
        return
    left = root * 2 + 1
    right = root * 2 + 2
    smaller = root
    if left < end and arr[left]['rating'] < arr[smaller]['rating']:
        smaller = left
    if right < end and arr[right]['rating'] < arr[smaller]['rating']:
        smaller = right
    if smaller != root:
        arr[smaller], arr[root] = arr[root], arr[smaller]
        sink(arr, smaller, end)


#
# def preprocess(file_name):


if __name__ == '__main__':
    file_name = 'Korean@Ann Arbor.json'
    data = open_cache(file_name)
    sort(data['businesses'])
    save_to_cache(data, file_name)
