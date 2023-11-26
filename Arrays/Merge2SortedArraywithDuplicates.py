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

2. NOW USE A 2-POINTER APPROACH TO SORT BOTH THE ARRAYS. 
NOTE : ALWAYS USE IF-ELIF-ELSE CONDITION TO COMPARE THE ELEMENTS IN THE ARRAYS.
'''
def getdups(arr,n):
    #this in place removes the duplicates of the array
    i,j=0,1
    while j<n:
        if arr[i]<arr[j]:
            arr[i+1]=arr[j]
            i+=1
        j+=1
    return i+1

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here\\
    n=len(a)
    m=len(b)
    p1,p2=0,0
    if n>1:
        #find dups for array a
        p1=getdups(a,n)

    if m>1:
        #find dups for array b
        p2=getdups(b,m)
        
    temp=[]
    i,j=0,0
    #2-pointer approach to compare the elements and merge them.
    while i<p1 and j<p2:
        if a[i]==b[j]:
            temp.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            temp.append(a[i])
            i+=1
        else:
            temp.append(b[j])
            j+=1

    '''there might be cases where one array is finished prior to the other one during previous while loop
    like a[1,2,3,4] but b=[1,2]; so the remaning [3,4] elements in array a would be left out as the loop
     (while i<p1 and j<p2) would end before comparing [3,4] in array a. The 2 while loops mentioned below
     will iterate for the rest of the array.'''
    while i<p1:
        temp.append(a[i])
        i+=1
    while j<p2:
         temp.append(b[j])
         j+=1
    return temp

