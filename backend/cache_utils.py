import json


def save_to_cache(data, filename):
    dumped_json_cache = json.dumps(data)
    fw = open(filename, "w")
    fw.write(dumped_json_cache)
    fw.close()


def open_cache(filename):
    """
    :param filename: the name of cache file
    :return: an empty dictionary if the cache does not exist, else return the loaded dictionary
    """
    try:
        cache_file = open(filename, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict
