"""the Outputs in a loop Change according to where the initilisation of variable is done
   whether it is inside loop or outside loop"""
   
#Exmaple 1: initilization Outside loop

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
""" Output is : Iteration 0 ; count is 12
                Iteration 1 ; count is 24
                Iteration 2 ; count is 36
                Iteration 3 ; count is 48
                Iteration 4 ; count is 60"""
            #-------------------------------------
                #WHY? 
                """since iteration < 5 we get 5 iterations.
                   in the first iteration, count(variable) counts the no. of 
                   characters present in "hello, world" ( including ',' and space)
                   so we get count = 12 in first iteration.
                   in the second iteration, we already have count as 12,
                   now it adds 12 to count (count[value 12] + 12 = 24).
                   and these iterations go on ... until 4th iteration."""
                   
#---------------------------------------------------------------------------------------------------------------------------------------------

#Example 2: Initilization Inside the loop
"""
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
                                                                                   """
"""Output is : Iteration 0 ; count is 12
              Iteration 1 ; count is 0
              Iteration 2 ; count is 12
              Iteration 3 ; count is 0
              Iteration 4 ; count is 12"""
           #-----------------------------------
            #WHY?
            """ here initilization is inside the loop, so 
            for every iteration, count gets updated to zero(0). 
            so after every iteration, count becomes 0 and the interpreter
            will start counting from zero."""
