

"""The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

    gcd(2, 12) = 2

    gcd(6, 12) = 6

    gcd(9, 12) = 3

    gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
Code Editor"""


def gcdIter(a, b):

    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    '''
    # Your code here

    testval = min(a,b) #taking a testValue, min() method returns the least val b/w a,b.

    while a % testval != 0 or b % testval != 0:

          testval = testval - 1

    return testval
