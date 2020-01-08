#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for index in my_list[:x]:
        try:
            print('{}'.format(index), end='')
        except IndexError:
            return index
    print()
    return index
