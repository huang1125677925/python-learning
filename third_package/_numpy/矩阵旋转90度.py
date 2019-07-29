'''
http://liao.cpython.org/numpy13/

'''

import numpy as np
mat = np.array([[1,3,5],
                [2,4,6],
                [7,8,9]
                ])
print(mat, "# orignal")
mat90 = np.rot90(mat, 1)
print(mat90, "# rorate 90 <left> anti-clockwise")
mat90 = np.rot90(mat, -1)
print(mat90, "# rorate 90 <right> clockwise")
mat180 = np.rot90(mat, 2)
print(mat180, "# rorate 180 <left> anti-clockwise")
mat270 = np.rot90(mat, 3)
print(mat270, "# rorate 270 <left> anti-clockwise")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for item in lists:
            while item:
                temp.append(item.val)
                item = item.next

        temp = temp.sort()

        a = ListNode(temp[0])
        temp = temp[1:]
        b = a
        while temp:
            a.next = ListNode(temp[0])
            temp = temp[1:]

        return b

