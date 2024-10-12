# Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution1(number):
    a,b=set(),set()
    if number>0:     
        for x in range(3,number,3):
            a.add(x)
        for y in range(5,number,5):
            b.add(y)
        return sum(a|b)
    else:
        return 0

def solution2(number):
    num=number-1
    k,l,m = 0,0,0
    if number>-1:
        if num>14:
            for x in range(0,number,15):
                k=k+x
                
        for y in range(0,number,3):
            l=l+y
            
        for z in range(0,number,5):
            m=m+z
        return l+m-k
    else:
        return 0