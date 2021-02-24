#Problem 1:

# s be any string
s = input('enter any string')
count = 0 #initilize a variable before for-loop
for char in s:  #here you can take i or j ,instead of 'char'
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(count) 

#_____________________________________________________________________________________________________________

#Problem 2:

s = input("enter a string")
count = 0
for word in range(1, len(s) - 1):
    if s[word:word+3] == 'bob':
#here s[word:word+3] selects 3-substring characters as a selactive string('bob' together).
    #instead of 'b' 'o' 'b' detecting them seperately.
        
         count += 1
        
print('Number of times bob occurs is:' + str(count))

#_____________________________________________________________________________________________________________

# Problem 3:

 #------------------------------------------------------------------------------------------------------------
 #this is METHOD 1
 
s = input("Enter a String")
words = total = s[0]
for i in range(1, len(s)):
    if s[i] >= words[-1]:                      
        words += s[i]
        if len(words) > len(total):
            total = words
    else:
        words = s[i]

print('Longest substring in alphabetical order is:'+ str(total))

#-------------------------------------------------------------------------------------------------------------

#Method 2: (Preferred and Optimised Method)

s = input("Enter a String")
current = '' #here we are using Dynamic Variables (values can be extended).
longest = ''
for i in range(len(s)):
    if (s[i] > s[i-1]):                      
        current += s[i]
    else:
        current = s[i]
    
    if len(current) > len(longest):  #since 'current' has more character in it
        longest = current            # assign longest = current

print('Longest substring in alphabetical order is:'+ str(total))


#_______________________________________________________________________________________________________________

"""That's All Fellas"""