'''
LEETCODE - 189
PROBLEM LINK : https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

'''
APPRAOCH 1:
This is the Brute Force Approach, where we move the elements in the array one at a time.
Input: arr = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

STEPS:
1. Run a loop from 0 to k
2. initialize p1 to n-2
3. Store the value of last element in temp ie temp=arr[n-1]
4. nested while loop from p1 to 0 {
       here we replace the value of arr[p1] with adjacent element arr[p1+1]
       which means we are moving the array to the right by 1 position
       decrement p1 by 1 ie p1-=1
   }
5. set the arr[0] value as temp (here we are setting the last element value that we stored 
   priorly to arr[0] 
'''

def rotatearray(arr,k):
   n=len(arr)
   for i in range(0,k):
      p1=0
      temp= arr[n-1]
      while p1>=0:
         arr[p1] = arr[p1+1] #moving adjacent element to right
         p1-=1
      arr[0]=temp
   return arr
'''
NOTE : The outer loop internally calls the nested loop k number of times. The nested loop moves an element
to the right by 1 place, everytime it is being called. So calling it k times, moves the array to right by k times.

TC - O(N**2); SC - O(1)
'''
------------------------------------------------------------------------------------------------------------------------
APPROACH 2:


        
       

