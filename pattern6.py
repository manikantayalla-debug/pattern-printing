#n is number of lines which can be dynamic
n = 5

#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for i in range(1,n+1):
    #Spaces '  ' are (n-i) times in every i iteration
    print("  "*(n-i),end="")
    #Elements '* 'are i times in every i iteration.
    print("* "*i)