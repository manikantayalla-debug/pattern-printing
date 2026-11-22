#To solve this batterfly pattern we need 2 loops
#n is the number of lines of the batterly pattern which are in increasing order which can be dynamic
n = 5

#First loop for increasing number of elements in the pattern
#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for i in range(1,n+1):
    #In every iteration there are i times "* " elements in the start
    print("* "*i,end="")
    #In every itearation there ares (n-2) * 2 times spaces
    print("  "*((n-i)*2),end="")
    #In every iteration there are i times "* " elements in the end
    print("* "*i)

#Second loop for decreasing number of elements in the pattern
#loop for number of lines starting from n-1 and ending at 1 (0 cause its exclusive) and -1 step in every iteartion
for i in range(n-1,0,-1):
    #In every iteration there are i times "* " elements in the start
    print("* "*i,end="")
    #In every itearation there ares (n-2) * 2 times spaces
    print("  "*((n-i)*2),end="")
    #In every iteration there are i times "* " elements in the end
    print("* "*i)