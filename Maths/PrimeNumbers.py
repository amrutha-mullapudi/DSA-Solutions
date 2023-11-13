PROBLEM LINK : https://www.codingninjas.com/studio/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""
A prime number has only 2 divisors that is 1 and the number itself. We can check whether a number is prime or not in an optimised way in O(sqrt(N)) complexity.
Lets say n = 36 - Inorder to check if 36 is prime or not, there is no need to iterate a loop till 36, we can simply check till sqrt(n) as there are
repetitive divisors for the number.  (CHECK PrintDivisors.py file for in depth explanation)
"""
CODE :

n=int(input())
count=0
i=1
while((i*i)<=n):
    if n%i==0:
        count+=1
        if (n//i!=i):
            count+=1
    i+=1
if count==2:
    print("YES")
else:
    print("NO")

"""
If the count > 2, then it is not a prime number. The condition n%i==0 checks for the divisor and if it is a divisor then (n//i!=i) also add the other divisor.
Example if i=2 which is a divisor of 36, then 36//2 = 18 is also a divisor of 36, hence count becomes 2. After looping till sqrt(n), if count>2 then it non-prime.
