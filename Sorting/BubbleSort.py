"""
Bubble Sort
PROBLEM LINK : https://www.codingninjas.com/studio/problems/bubble-sort_624380?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
"""

def bubbleSort(arr,n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr
