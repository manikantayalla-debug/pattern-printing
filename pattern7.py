#n is number of lines which can be dynamic
n = 5

#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for  i in range(1,n+1):
    #Spaces per iteration is n-i times
    print("  "*(n-i),end="")
    #'*' elements in per iteration is i*2-1 in every iteration
    print("* "*((i*2)-1),end="")
    #print for new line after every iteration
    print()
