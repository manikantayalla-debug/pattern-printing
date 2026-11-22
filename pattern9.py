#The solution for this pattern is combination of patter 7 and pattern 8
#Need to loops to print this pattern.
#n is number of lines which are increasing elements in the star
n = 5

#loop 1 is for increasing order of elements
#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for i in range(1,n+1):
    #Spaces per iteration is n-i times
    print("  "*(n-i),end="")
    #'*' elements in per iteration is i*2-1 in every iteration
    print("* "*((i*2)-1),end="")
    #print for new line after every iteration
    print()


#loop 2 is for decreasing order of elements
#loop for number of lines starting from 4 and ending at 1. (n-1) cause its exclusive.
for i in range(n-1,0,-1):
    #Spaces per iteration is n-i times
    print("  "*(n-i),end="")
    #'*' elements in per iteration is i*2-1 in every iteration
    print("* "*((i*2)-1),end="")
    #print for new line after every iteration
    print()