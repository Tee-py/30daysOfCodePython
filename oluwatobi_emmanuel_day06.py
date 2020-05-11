"""This is a python function that
accepts a list, string, set or tuple as an
argument and returns the power list of the argument.
It can also be used for an array containing
an element of type str and also a string
argument
"""
def power_list(num_list):
    try:
        from itertools import combinations, chain
        output_list = [[],]
        for i in num_list:
            output_list.append([i])
        num_combs = list(combinations(num_list, k) for k in range(2, len(num_list)+1))
        display_power_list = [list(lst) for lst in chain(output_list, *num_combs)]
        return (display_power_list)
    except TypeError:
        return 'Argument or parameter must be of type str, list, tuple or set'
print((power_list([1,2,3,4])))

