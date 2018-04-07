#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午3:38
# @Author  : weitao
# @Site    : 
# @File    : demo.py
# @descrip :
# @Software: PyCharm Community Edition

###快速排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


#print(quicksort([3, 6, 8, 10, 1, 2, 1]))
# Prints "[1, 1, 2, 3, 6, 8, 10]"

# animals = {'cat', 'dog'}
# a = {}
# print('cat' in animals)

# import numpy as np
#
# a = np.array([1, 2, 3])  # Create a rank 1 array
# print(type(a) )           # Prints "<type 'numpy.ndarray'>"
# print(a.shape)            # Prints "(3,)"
# print(a[0], a[1], a[2])   # Prints "1 2 3"
# a[0] = 5                 # Change an element of the array
# print(a)                # Prints "[5, 2, 3]"
#
# b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
# print(b.shape)                    # Prints "(2, 3)"
# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"



# import numpy as np
#
# # Create the following rank 2 array with shape (3, 4)
# # [[ 1  2  3  4]
# #  [ 5  6  7  8]
# #  [ 9 10 11 12]]
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#
# # Use slicing to pull out the subarray consisting of the first 2 rows
# # and columns 1 and 2; b is the following array of shape (2, 2):
# # [[2 3]
# #  [6 7]]
# b = a[:2, 1:3]
# print(b)
#
# # A slice of an array is a view into the same data, so modifying it
# # will modify the original array.
# print(a[0, 1])   # Prints "2"
# b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
# print(a[0, 1])   # Prints "77"

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape) # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape) # Prints "[[5 6 7 8]] (1, 4)"


