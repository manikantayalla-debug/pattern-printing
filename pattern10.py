#n is number of lines of square which can be dynamic
n = 5

#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for  i in range(1,n+1):
    #the starting and ending line of square if is '* ' element n times
    if i == 1 or i == n:
        print("* "*n)
    #otherwise theres an element at start and end and rest are spaces so n-2 times spaces in every else iteration
    else:
        print("* ",end="")
        print("  "*(n-2),end="")
        print("*")
    