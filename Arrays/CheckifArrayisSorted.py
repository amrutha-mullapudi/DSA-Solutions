'''
LEETCODE - 1752
Check if array is sorted - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
'''

'''
Approach 1: 
Initialize a counter cnt to keep track of the number of inversions.
Iterate through the elements of the vector starting from the second element (index 1) to the last element (index n-1).

For each pair of adjacent elements, compare them.
If the element at the previous index (nums[i-1]) is greater than the current element (nums[i]), increment the cnt counter. This indicates an inversion.
After the loop, check if the last element of the vector (nums[n-1]) is greater than the first element (nums[0]).

If it is, increment the cnt counter again. This checks for an inversion between the last and first elements (a circular check).
Finally, return true if cnt is less than or equal to 1, indicating that the array can be rotated to become sorted with at most one inversion. Otherwise, return false.

In summary, the code counts inversions in the array and checks if there are at most one inversion, which would allow the array to be rotated into a sorted order.
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        counter=0
        p1=1
        while p1<n:
            if nums[p1-1]>nums[p1]:
                counter+=1
            p1+=1
        if nums[n-1]>nums[0]:
            counter+=1
        if counter>1:
            return False
        return True
      
-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
APPROACH 2:
-> Find the index of the maximum element, which is followed by minimum element. 
-> Example [3,4,5,1] Find the index of 5 as it is followed by 1 in order to find where the increment breaks.
-> An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
-> Set an index element to zero; 
-> loop through 0 to n, if an element if lesser than index element then it means the array is not sorted.
-> else set the value to index (this means the elements that are iterated are in sorted order).
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        a=[0]*n
        p1=0
        maxi=0
        while p1<(n-1):
            if nums[p1]>nums[p1+1]:
                maxi=p1+1
            p1+=1
        index=0
        for i in range(n):
            value = nums[(i+maxi)%n]
            if index>value:
                return False
                break
            else:
                index=value
        return True

'''

