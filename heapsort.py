from heap import Heap
import unittest

def heap_sort(number_list):
    H = Heap()
    for number in number_list:
        H.print()
        H.insert(number)
        H.print()
    for i in range(len(number_list)):
        number_list[i] = H.extract_min()
        H.print()
    return number_list

def display_menu(words_list):
    global count
    menu = {}
    menu['1'] = "Hard-coded"
    menu['2'] = "Reading file"
    menu['3'] = "Exit"
    while True:
        options = menu.keys()

        for entry in options:
            print(entry, ".- ", menu[entry])
        selection = input("Please Select:")
        if selection == '1':
            while True:
                number_list_harcoded = [10, 200, 101, 420, 9, 4, 100, 8, 4, 7, 3, 2, 1, 0]
                sorted_list_hardcoded = heap_sort(number_list_harcoded)
                print(sorted_list_hardcoded)
                selection = str(input("Press 0 to get back to the menu: "))
                if selection == '0':
                    break
        elif selection == '2':
            while True:
                number_list = words_list
                sorted_list = heap_sort(number_list)
                print(sorted_list)
                selection = str(input("Press 0 to get back to the menu: "))
                if selection == '0':
                    break


if __name__ == '__main__':
    words_file = open("random_numbers_list.txt", "r")
    words_list = list(map(int, words_file.read().split("\n")))
    print(words_list)
    display_menu(words_list)





