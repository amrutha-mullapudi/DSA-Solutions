'''
PROBLEM LINK : https://leetcode.com/problems/max-consecutive-ones/description/
LEEETCODE : 485
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

CASES TO BE CONSIDERED :
nums= [0] or [1] (input array with size of 1)
nums = [1,0,1,0,1,1], [0,1,0,1,1,1](starting with zero), [1,1,1,1,1,1](there is no zero)

APPROACH :
1.Find the index where we find the first occurence of the zero in the array. 
Why do we do this? 
-> In order to check if there are any zeros present or if the array is completely filled with 1's and no zeros. Example lets say for nums=[1,1,1,1]
-> if i-=1 is the pointer that we are using to find the first zero; after iterating through the array this would still be at -1. Stating there are no zeros in the array.

2. If the first zero is present at say ith index, that means all elements from 0 to i are 1's. So we need to calculate the count of those 1's
-> Example: [1,1,1,0,1,1,0,1,1] ; here the first zero is present at 3rd index. So number of 1's present till i is 3; stored in a count variable

3. Using 2 pointer approach, we use i,j where j=i+1. We iterate and check 
(if nums[j]==1 ) { 
  we need to iterate the counter by 1 }
else {
  we found a zero, that means we need to find the count of 1's between the zero present at index i and index j.
  in order to do that we do count=j-i-1
  example : [1,0,1,1,0,1] first zero at index 1; second zero at index 4
  if i=1; j=4 => count of 1's = 4-1-1 = 2
}

4.For arrays like nums=[0,1,0,1,1,1], there is a chance the else condition in while where we check the count of 1's will not
  get executed, as there is no zero at the end. In that case after ending the while loop, we do this step for one last time.
        count=j-i-1
        maxcount=max(maxcount,count)

NOTE : DO A DRY RUN WITH THE EXAMPLE ARRAYS UNDER CASES TO BE CONSIDERED, TO COVER ALL THE POSSIBILITIES.
        
''' 


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''finding the first occuring zero, so that we can start looping and 
        finding from that zero to rest of the array'''
        n=len(nums)
        i=-1
        for ele in range(n):
            if nums[ele]==0:
                i=ele
                break
        
        if i==-1: #checks if zero is present or not
            return n
        maxcount=max(i,0)
        count=0

        j=i+1
        while j<n:
            if nums[j]==1:
                j+=1
            else:
                count=j-i-1
                maxcount=max(maxcount,count)
                i=j
                j=i+1
        
        '''this final check is when you might have consecutive 1's in the end
        #example [1,0,1,0,1,1,1] here i would be at 3rd place ie i=3 and j would 
        increment till the end,but there is no zero at the end so that the else condition 
        in while j<n would get satisified, so we do a final check of j-i-1 here to keep a track 
        of last 3 consecutive 1's that we have. count=7-3-1=3
        '''
        count=j-i-1
        maxcount=max(maxcount,count)
        return maxcount

