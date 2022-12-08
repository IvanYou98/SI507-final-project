import json
from cache_utils import open_cache, save_to_cache

"""
    sort the input array in descending order by their ratings
"""


def sort(arr):
    build_min_heap(arr)
    # now we have a min heap, so on the top of our heap is the lowest rated restaurant, we need to swap it with the last
    # element of array (since we want to sort in descending order), and sink the current top of heap.
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
    print(arr)


"""
    build a min heap based on input array
"""


def build_min_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        sink(arr, i, len(arr))


"""
sink down the tree node to its correct position
arr: input array
root: the index of the tree node in the input array
end: the right boundary of array (exclusive)
"""


def sink(arr, root, end):
    if root >= end:
        return
    left = root * 2 + 1
    right = root * 2 + 2
    smaller = root
    # if one of the child node has lower rating than the root node, we will swap the lower rated child node
    # with the root node
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
