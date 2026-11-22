#n is number of lines of triangle which can be dynamic
n = 5

#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for i in range(1,n+1):
    #in the triangle line 1,2 and n entirely contains "* " of elements
    if i in [1,2,n]:
        print("* "*(i))
    #otherwise every iteartion has 2 elements are rest are spaces
    else:
        print("* ",end="")
        #in every else loop spaces are i-2 times
        print("  "*(i-2),end="")
        print("* ")