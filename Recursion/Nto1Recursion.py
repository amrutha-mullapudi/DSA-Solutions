"""
Using recursion print number from N to 1 in decreasing order
"""

CODE -

#RECURSIVE FUNCTION THAT IS BEING 
CALLED INTERNALLY FOR N TIMES
def callnum(l,x):  
    if x==0:
        return
    l.append(x)
    callnum(l,x-1)

def printNos(x):
    l=[]
    callnum(l,x)
    return l

n=int(input())
print(printNos(n))
