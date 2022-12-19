#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # variable to keep track of number of elements printed
    try:
        for i in range(x):  # loop through x elements
            print(my_list[i], end=' ')  # print the element followed by a space
            count += 1  # increment the count
        print()  # print a newline after all elements have been printed
    except IndexError:  # if the index is out of range, catch the exception
        pass  # do nothing
    return count  # return the number of elements printed
