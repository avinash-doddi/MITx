#Mid-Term Exam


"""Write a Python function, twoQuadratics, that takes in two sets of coefficients and x-values and prints the sum of the results of evaluating two quadratic equations. It does not do anything else. That is, you should evaluate and print the result of the following equation: a1∗x21+b1∗x1+c1+a2∗x22+b2∗x2+c2

You are given the following function, evalQuadratic

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c
    

Use the given function (you don't need to redefine evalQuadratic in this box; when you call evalQuadratic, our definition will be used)."""


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here 
    
    x= evalQuadratic(a1, b1, c1, x1)  
    y= evalQuadratic(a2, b2, c2, x2)
    print(x+y)
    
#----------------------------------------------------------------------------------------------------------   
    
    
    
""" Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

    assume L is not empty
    assume 0 < n <= len(L)

This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]

Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.   """
    
    def getSublists(L, n):
	list_of_sublists = [] 	
	for i in range(len(L)-n+1):
		list_of_sublists.append(L[i:i+n]) 
		#create sublists of length n for every i and adds this sublist to master sublist
	return list_of_sublists
	
#---------------------------------------------------------------------------------------------------------	
	
	
	
"""Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list."""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    

	
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    fullList = []
    uniList = []
    keyList = []
    tracker = 0
    
    #place all values into a list
    for value in aDict.values():
      fullList.append(value)
    
    #create a unique list of values
    for i in range(len(fullList)):
      tracker = fullList.count(fullList[i])
      if tracker == 1:
        uniList.append(fullList[i])
    
    #create a list of unique keys
    for key, value in aDict.items():
      if value in uniList:
        keyList.append(key)
    
    #sort list
    keyList.sort()
    
    return keyList
     
    
myDict = {'1':3, '2':4, '5':4, '10':12}   
uniqueValues(myDict)    


#------------------------------------------------------------------------------------------------



"""Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer."""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    
def sumDigits(n):
    n = str(n)
    if n is "":
       # Base Case: Return 0 when there is nothing left
      return 0    
   else:
       # Default Case: Return the first number + sum of the rest)
        return int(n[0]) + sumDigits(n[1:])
        

#-------------------------------------------------------------------------------------------------- 
    


"""Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    """Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

"""run_satisfiesF(L, satisfiesF)

For your own testing of satisfiesF, for example, see the following test function f and test code:

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)

Should print:

2
['a', 'a']

Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases."""

def satisfiesF(L):
    i = 0
    while len(L) > i:
        if f(L[i]): 
           i += 1
        else:
           L.pop(i)
   return len(L)

run_satisfiesF(L, satisfiesF)
   
#--------------------------------------------------------------------------------------------

"""<<< That's all Folks >>>"""
