from heap import Heap
import unittest

def heap_sort(number_list):
    H = Heap()
    for number in number_list:
        H.insert(number)
    for i in range(len(number_list)):
        number_list[i] = H.extract_min()
    return number_list

if __name__ == '__main__':
    number_list = [3,2,1,0]
    sorted_list = heap_sort(number_list)
    print(sorted_list)





