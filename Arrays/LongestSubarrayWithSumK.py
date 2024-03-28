PROBLEM LINK: https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_6682399
'''
BRUTE FORCE (SOLUTION 1)
‘a’ = [1, 2, 3, 1, 1, 1, 1]
k=3

1. find all the subsets present in this array ie [1],[1,2],[1,2,3],[1,2,3,1] and so on, then find the sum of each subset and compare it with the k value
2. first we iterate from i=0 to i<n (this is the outer loop)
3. second we have an inner loop which creates subarrays from i to n ie
    [1],[1,2],[1,2,3]
    [2],[2,3],[2,3,4]....
4. in order to find the sum of subarray between a given i and j we are running another loop k from i to j and calculating the sum for it.
'''

PSUEDOCODE:

sum=0
maxlen=0
for i in range(0,n):
  for j in range(i,n):
    sum=0
    for k in range(i,j):
      sum+=a[k]
  if sum==k:
    maxlen=max(maxlen,j-i+1)
return maxlen

'''
TC = O(N*N*N) , SC = O(1)
------------------------------------------------------------------------------------------------------------------------------------------------------

SOLUTION 2:
1. since we are anyway adding each of the digits in the array to find the sum, we can remove the third loop from i to j and just add the sum in 
second loop itself
'''

sum=0
maxlen=0
for i in range(0,n):
  sum=0
  for j in range(i,n):
    sum+=a[k]
    if sum==k:
      maxlen=max(maxlen,j-i+1)
return maxlen

'''TC = O(N*N) , SC = O(1)'''
------------------------------------------------------------------------------------------------------------------------------------------------------

SOLUTION 3: (BETTER APPROACH)
1. For a better approach we can consider using a dictionary. 
WATCH : https://youtu.be/frf7qxiN2qU

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n=len(a)
    s=0
    for i in range(n):
        s+=a[i]
    if s==k:
        return n
    d=dict()
    maxlen=0
    sum=0
    for i in range(n):
        sum+=a[i]
        d[sum]=i
        if sum==k:
            maxlen=max(maxlen,(i+1))
        elif (sum-k) in d:
            temp=sum-k
            maxlen=max(maxlen,d[sum]-d[temp])
    return maxlen
  
  '''TC = O(N) , SC = O(N)
------------------------------------------------------------------------------------------------------------------------------------------------------
SOLUTION 4: (BETTER APPROACH)
1. Optimal approach can be achieved using the 2 pointer method.
2. we consider 3 cases for that 
    a) if sum < k then just increase p2
    b) if sum==k then calculate maxlength, increase p2
    c) if sum> k then we need to remove a[p1] from the sum and make it less than or equal to k 
'''

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    p1=0
    p2=0
    sum=a[p1]
    n=len(a)
    maxlen=0
    while p2<n:
        if sum<k:
            p2+=1
            if (p2<n):
                sum+=a[p2]
        elif sum==k:
            maxlen=max(p2-p1+1,maxlen)
            p2+=1
            if (p2<n):
                sum+=a[p2]
        else:
            sum-=a[p1]
            p1+=1
    return maxlen                                                                                                                               
