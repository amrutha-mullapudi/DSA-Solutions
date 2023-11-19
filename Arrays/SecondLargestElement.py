'''
PROBLEM LINK : https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SOLUTION

The problems expects us to find the second largest and second smallest element in the array.
Solutions:
'''

'''
1. BRUTE FORCE :
-> Sort the array in an increasing order.
-> Find the 2nd smallest and 2nd largest array
Time Complexity : O(n * Log(n)), where ‘n’ is the size of the array ‘a’.As we are sorting the array, it will take the O(n * Log(n)) time. Hence, the time complexity is O(n * Log(n)).
Space Complexity : O(1). As we are using constant extra space. Hence, the space complexity is O(1).
'''
def getSecondOrderElements(n, arr):
    # Sorting out the given input array.
    arr.sort()
    #alternatively you can use merge sort also
    return [arr[n - 2], a[1]]
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

'''
2.FINDING THE MINIMUM AND MAXIMUM ELEMENT, THEN COMPARING THEM TO FIND THE 2ND_MINIMUM AND 2ND_MAXIMUM
First, we will traverse the array and will find the smallest and largest elements. Then we will travel again and will find the element just greater than the smallest 
element and the element just smaller than the largest element. The elements found after words are the required answer.
->Initialize the variables ‘small = INT_MAX’, ‘large = INT_MIN’, ‘secondSmall = INT_MAX’ and ‘secondLarge = INT_MIN’.
->Iterate over the array ‘a’ with iterator ‘i’
    Set ‘large = max(large, a[i])’ and ‘small = min(small, a[i])’
->Iterate from 0 to ‘n’ with iterator ‘i’
    If ‘a[i] < secondSmall && a[i] != small’ then update ‘secondSmall = a[i]’
    If ‘a[i] > secondLarge && a[i] != large’ then update ‘secondLarge = a[i]’
Return ‘{secondLarge, secondSmall}’
Time Complexity : O(n), where ‘n’ is the size of the array ‘a’.
Space Complexity : O(1).

NOTE : This takes 2 loops to find the solution, however we can find the second_smallest and second_largest using a single loop
'''
def getSecondOrderElements(n,a):
    # Initializing the driver variables.
    small = int(1e9)
    secondSmall = int(1e9)
    large = int(-1e9)
    secondLarge = int(-1e9)

    # Iterating over an array and calculating the smaller and larger numbers.
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])

    # Iterating again and updating the second order numbers.
    for i in range(n):
        if (arr[i] < secondSmall and arr[i] != small):
            secondSmall = arr[i]
        if (arr[i] > secondLarge and arr[i] != large):
            secondLarge = arr[i]

    return [secondLarge, secondSmall]
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

'''
We can find the solution in a single loop 
1. Initialise the smallest and largest element to arr[0], and second_largest and second_smallest to 0
2. We traverse the array and check for :
  if (arr[i] < smallest){
  then update arr[i] to smallest and smallest to second_smallest
  }
  else {
  since we are aware that the number is greater than smallest number it has 2 possibilities:
      -> either arr[i]>second_smallest or arr[i]<second_smallest. Since we are initialising the second_smallest number to 0,
      -> we check if second_smallest is equal to zero (it means the second_smallest number is not yet populated from the array) 
      -> or if a[i]<second_smallest, in both of these cases we update the a[i] value to second_smallest
  }
  Similarly we check for the second_largest and populate it.
'''
def getSecondOrderElements(n,a)
    arr=[]
    smallest,largest=a[0],a[0]
    second_smallest,second_largest=0,0
    for i in range(1,n):
        if (a[i]<smallest):
            second_smallest=smallest
            smallest=a[i]
        else:
            if second_smallest==0 or a[i]<second_smallest:
                second_smallest=a[i]
        if (a[i]>largest):
            second_largest=largest
            largest=a[i]
        else:
            if second_largest==0 or a[i]>second_largest:
                second_largest=a[i]
    arr.append(second_largest)
    arr.append(second_smallest)
    return arr
