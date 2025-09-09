#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = my_list[:]
    for i in range(0, len(res)):
        if res[i] == search:
            res[i] = replace
    return res
