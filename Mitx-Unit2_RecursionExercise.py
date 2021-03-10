

"""Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed. """

def iterPower(base, exp):
     '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    result = 1
    while exp>0:
          result *= base
          exp -= 1
    return result

print(iterPower(int(input("base : ")),int(input('exp : '))))
   
   
 __________________________________________________________________________________________________________________________________________________________________
 
 
 """fibonacci Series Using Recursive Function"""
 
 def fibonacci(n):
     if n ==1 or n == 0:
        return n
     else :
        return fibonacci(n-1)+fibonacci(n-2)
 #call the function here -->
 
 print(fibonacci(int(input("Enter a number to get the position of intput number in fibonacci series"))))
 
 
 """This is kinda irritating to understand..."""
 
 
 
 
