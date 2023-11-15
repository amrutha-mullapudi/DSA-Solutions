"""
Selection Sort Algorithm
PROBLEM LINK : https://www.codingninjas.com/studio/problems/selection-sort_624469?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
"""

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n=len(arr)
    for i in range(n):
        min=arr[i]
        j=i+1
        while (j<n):
            if arr[j]<arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
            j+=1
    return arr

"""
DETAILED APPROACH :

"""
