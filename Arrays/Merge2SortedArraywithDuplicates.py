'''
PROBLEM LINK : https://www.codingninjas.com/studio/problems/sorted-array_6613259
'''

'''
APPROACH 1 : BRUTE FORCE
1. Using a SET in Python. We initialize a set, add the elements from both the arrays into it to remove duplicates and then remove sort it again because the 
elements added into a set are by default not sorted.
'''
def sortedArray(a: [int], b: [int]) -> [int]:
    s=set(a+b)
    return sorted(s)

'''
APPROACH 2 : Using IN PLACE REMOVAL OF DUPLICATES and 2-POINTER APPROACH TO MERGE THE NON-DUPLICATE ARRAYS
1. Remove the duplicates in place for both the arrays.
MECHANISM : 
