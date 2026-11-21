#n is number of lines which can be dynamic
n = 5

#loop for number of lines starting from 5 and ending at 0 cause its exclusive and -1 step in every iteration.
for i in range(n,0,-1):
    #printing '* ' i times in every iteration.
    print("* "*i)