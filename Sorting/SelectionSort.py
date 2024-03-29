"""
Selection Sort Algorithm
PROBLEM LINK : https://www.codingninjas.com/studio/problems/selection-sort_624469?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
"""

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n=len(arr)
    for i in range(n):
        mini=i
        j=i+1
        while j<n:
            if arr[j]<arr[mini]:
                mini=j
            j+=1
        temp=arr[i]
        arr[i]=arr[mini]
        arr[mini]=temp
    return arr

"""
DETAILED APPROACH :

"""
