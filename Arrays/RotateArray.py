'''
LEETCODE - 189
PROBLEM LINK : https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
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
   
NOTE : The outer loop internally calls the nested loop k number of times. The nested loop moves an element
to the right by 1 place, everytime it is being called. So calling it k times, moves the array to right by k times.

TC - O(N**2); SC - O(1)
------------------------------------------------------------------------------------------------------------------------

APPROACH 2:
An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
Input: arr = [1,2,3,4,5,6,7], k = 3

If rotated array is brr for example :
1. arr[0]=1 ; this element will be present in brr[(i+k)%len(arr)] ie brr[(0+3)%7 => brr[3]
2. arr[1]=2 ; this element will be present in brr[(i+k)%len(arr)] ie brr[(1+3)%7 => brr[4]
.
....Similarly
the rotated array will be generated as brr = [5,6,7,1,2,3,4]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=[0]*len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)]=nums[i]
        for i in range(len(a)):
            nums[i]=a[i]
        return nums
        
 TC : O(N); SC - O(N)      
------------------------------------------------------------------------------------------------------------------------

APPROACH 3:
We can also observe that an array rotated by k times is similar to this :
Input: arr = [1,2,3,4,5,6,7], k = 3
1. reverse the array => arr = [7,6,5,4,3,2,1]
2. reverse the array from 0 to k => [5,6,7,4,3,2,1]
3. reverse the array from k+1 to n => [5,6,7,1,2,3,4]  (this is the final array that is generated)

VERY IMPORTANT NOTE : 
Here there might be cases where the size of array = 1; but the number of rotations that are expected is 2
Input: arr = [1], k = 3  (In this case if you iterate over the code it will give you list index out of bounds error, as you 
are trying to iterate from 0 to 2 here according to the logic, but the total size of the array is only 1
-> In that case we need to do k%=len(arr); 2%=1 gets converted to 0.

def reverse_array(self,arr,p1,p2):
        while p1<p2:
            temp=arr[p1]
            arr[p1]=arr[p2]
            arr[p2]=temp
            p1+=1
            p2-=1
        return arr

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        self.reverse_array(nums,0,n-1)
        self.reverse_array(nums,0,k-1)
        self.reverse_array(nums,k,n-1)



