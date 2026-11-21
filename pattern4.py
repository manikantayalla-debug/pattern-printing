#n is number of lines which can be dynamic
n = 5

#Outer loop is for number of lines(1 to 6 cause 6 is exclusive)
for i in range(1,n+1):
    #Inner loop is for printing elements (1 to i val) in every iteration
    for j in range(1,i+1):
        #Printing vals from 1 to i in every iteration and making sure print cause create a new line
        print(f"{j}",end=" ")
    #Forcing a new liner at the end of J loop in every i iteration
    print()