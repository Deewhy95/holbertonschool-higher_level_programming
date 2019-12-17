#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        cp = my_list[:]
        cp[idx] = element
        return cp
