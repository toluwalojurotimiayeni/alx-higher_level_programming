#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def ser(elm):
        return (elm if elm != search else replace)
    return list(map(ser, my_list))
