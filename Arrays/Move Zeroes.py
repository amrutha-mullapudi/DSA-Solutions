'''
LEETCODE - 283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
PROBLEM LINK - https://leetcode.com/problems/move-zeroes/description/
'''
'''
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

OPTIMISED APPROACH :
1. First find the index where the first zero is starting. There are 2 uses because of this :
   -> If the array has no zeroes, then we will not be able to find the index, which means we do not have to switch them to end of the array
   -> Based on the index that we find, where the first zero is starting.. we can use a 2 pointer approach to compare and elements and swap.
2. Example : initially lets say i=-1. We use this index to find the first zero where we are getting
3. In this example, we found the zero at the first place only =>  nums = [0,1,0,3,12] 
4. Run a while condition/for-loop from index where we found the first zero to rest of the array
5. i= index of first zero; j= i+1
6. if nums[j]!=0 and nums[i]==0 ; that means we need to swap both the elements and then increment both the counters
'''
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==1:
            return 
        #find the first zero occuring
        i=-1
        for j in range(n):
            if nums[j]==0:
                i=j
                break
        if i==-1:
            return
        j=i+1
        while j<n:
            if nums[j]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
            j+=1
