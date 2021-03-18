""" Python Solutions to freeCodeCamp algorithms: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference

Problem 1: Find the Symmetric Difference between two or more arrays

Author: John Milley
"""

import copy

a = [1, 2, 3]
b = [2, 3, 4]
c = [3, 4, 5]
d = [10, 2, 3, 1, 4]

# Algorithm: Using unsorted lists

def symmetric_diff_of_two_sets(a, b):
    """Returns the symmetric difference between list a and b"""
    b_copy = copy.copy(b)
    sd = []
    for i in a:
        unique = True
        for j in b_copy:
            if i == j:
                unique = False
                b_copy.remove(j)
        if unique and i not in sd:
            sd.append(i)
    # copy the remaining unmatched elements (if any) from b_copy to sd
    sd += b_copy
    return sd

def symmetric_diff(*args):
    """ Handles list argruments, passing two at a time to symmetric_diff_of_two_sets"""
    if len(args) < 2:
        print('Must supply more than one argument.')
        return

    for arg in args:
        if not isinstance(arg, list):
            print("Each argrument passed to symmetric_diff must be a list.")
            return
    
    sd = symmetric_diff_of_two_sets(args[0], args[1])
    for i in range(2, len(args)):
        sd = symmetric_diff_of_two_sets(sd, args[i])
    return sd

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')
print('--------------')
print(f'a ∆ b: {symmetric_diff(a, b)}')
print(f'a ∆ b ∆ c: {symmetric_diff(a, b, c)}')
print(f'a ∆ b ∆ d: {symmetric_diff(a, b, c, d)}')


# Testing if < 2 arguments supplied
# print(symmetric_diff(a))

# Testing if argument is not a list
# print(symmetric_diff(a, 1))