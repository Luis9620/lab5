from heap import Heap
import unittest

def heap_sort(number_list):
    H = Heap()
    for number in number_list:
        H.print()
        H.insert(number)
        H.print()
    for i in range(len(number_list)):
        H.print()
        number_list[i] = H.extract_min()
        H.print()
    return number_list


if __name__ == '__main__':
    number_list = [10,9,4,3,2,1,0]
    sorted_list = heap_sort(number_list)
    print(sorted_list)






