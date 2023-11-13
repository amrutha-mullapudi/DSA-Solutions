"""
PROBLEM LINK : https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""
"""
SOLUTIONS:
Lets consider a number n=36, it had multiple factors ranging from [1,2,3,4,6,9,12,18,36].These are all the factors of number 36.
If we ever have to find the divisors for a number we need to keep these points in mind:
     1.All the divisors are going to range within 1 to N
     2.If a number i for example is a divisor then naturally N//i is also going to be a divisor.
"""
"""
APPROACH 1:
1. We run a loop through numbers 1 to N and check if each number that we are fetching in the index is divisible by N or not. If divisible print it.
TC - O(N) ; SC - O(1)
"""
def printDivisors(n):
  for i in range(1,n+1):
    #here we are checking the divisibility                    
      if (n%i==0):
        print(i)
#THIS APPROACH IS OF GOOD COMPLEXITY BUT IF THERE ARE VALUES WITH HIGHER VALUE, THEN IT MIGHT NOT BE AN OPTIMAL SOLUTION

"""
APPROACH 2 :
-> Give a brief look on all the divisors that we have written for n = 36
-> if you observe clearly :
(1,36)   (36,1)
(2,18)   (18,2)
(3,12)   (12,3)
(4,9)    (9,4)
(6,6)    

-> Here we can see that all the numbers which are not equal to or nearly equal to the square root of the number (here it is 36, so square root is 6) have 2 divisors.
-> if 1 is a divisor of 36 then 36 is also a divisor of 36 .... similarly if 2 is divisible by 36 then 36//2 = 18 is also a divisor of the number 36.
-> According to this approach it is evident that you do not require an elaborate loop to check from 1 to N for all divisors. You can simply check from 1 to sqrt(N)
-> IMPORTANT - EDGE CASE HERE : If you see the sqrt(n) is repeated twice ie 6 in this case. So we need to consider printing it only once.
"""
def printDivisors(n):
     i=1
     while (i*i<=n):
          if (n%i==0):
               print(i)
               if (n//i != i):   #this is to check if we are printing the sqrt(n) only once instead of twice.In this case to make sure we print divisor 6 only once.
                    print(n//i)  #This is for printing the other number. Eg: if i==1 then 36//1 =36...Similarly if i==2 which is a divisor then we print (36//2)=18
     i+=1


                    

