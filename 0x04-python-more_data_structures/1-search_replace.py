#!/usr/bin/python3

def search_replace(my_list, search, replace):
    rp_list = []
    for i in my_list:
        if search == i:
            rp_list.append(replace)
        else:
            rp_list.append(i)
    return rp_list
