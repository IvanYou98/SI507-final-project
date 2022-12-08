import json
from cache_utils import open_cache, save_to_cache
from heap_sort import build_min_heap

if __name__ == '__main__':
    data = open_cache("tree_data.json")
    build_min_heap(data)
    # save_to_cache(data, "tree_data.json")
    print(data)