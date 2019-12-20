#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary
    for index in new_dic:
        new_dic[index] *= 2
    return new_dic
