#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x-amount of element in a list

    Args:
        my_list (list): the list from which element
        is printed
        x (int): the number of element expected to
        be printed

    Return:
        the amount of printed element
        """
    elem_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elem_print += 1
        except IndexError:
            break
    print("")
    return(elem_print)
