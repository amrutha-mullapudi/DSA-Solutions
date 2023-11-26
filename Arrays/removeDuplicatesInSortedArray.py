'''
PROBLEM LINK : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
LEETCODE 26 - Remove Duplicates from Sorted Array
'''
'''
APPROACH 1:
BRUTE FORCE :
1. In order to remove the duplicates prevelant in the array, add them into a set.
2. A set removes the duplicate elements which are added.
3. Again move the elements from set to the array (as required per the problem statement)
4. The length of the set is the count of unique elements in the array.
'''

arr=[1,2,2,3,3,4,5]
s=set()
#iterating through the array and adding elements in set
#this creates set s=(1,2,3,4,5)
for i in arr:
    s.add(i)

ele=0
#iterating through the set and moving the elements back to array
for i in s:
    arr[ele]=i
    ele+=1
print(ele,sorted(arr))

OUTPUT : 5 [1, 2, 3, 4, 5, 3, 4]
TC : O(N)+O(NLOGN); SC : O(N)
------------------------------------------------------------------------------------------------------------------------------------------------------
'''
APPROACH 2:
OPTIMISED IN PLACE APPROACH :
1. In this array : arr=[1,2,2,3,3,4,5] ...we can observe that instead of creating a new set and moving elements we can change the elements in place.
2. But instead of swapping elements here, we can just change their values using 2 pointer approach.
3. Consider p1=0; p2=1 (only when length of input array more than 1)
4. LOGIC : if arr[p1]<arr[p2]; we update the arr[p1+1] element to the value which is present in arr[p2] 
           if arr[p1] == arr[p2] or arr[p1]>arr[p2] we simply increase the p2++ pointer

EXPLANATION :
initially p1=0,p2=1 => IS arr[p1]<arr[p2]? (yes) => arr[p1+1] = arr[p2]; which means arr[0+1] = 2 (increment p1, p2)
p1=1,p2=2 => Is arr[p1]<arr[p2]? (NO)  => INCREMENT P2 pointer p2++
p1=1,p2=3 => IS arr[p1]<arr[p2] = arr[1]<arr[3] (YES) as 2<3; In that case we change the value of arr[p1+1] element to arr[p2] => arr[1+1] = arr[2] = 3
(This results in the array getting changed into [1,2,3,3,3,4,5]; which means 1,2,3 are sorted..
.
.
Similarly we do the same logic for remaining elements as well

'''

def removeDuplicates(self, nums: List[int]) -> int:
  n=len(nums)
  if n==1:
    return n
  p1,p2=0,1
  while p2<n:
    if nums[p1]<nums[p2]:
      nums[p1+1]=nums[p2]
      p1+=1
    p2+=1
  return p1+1

TC : O(N); SC : O(1)
