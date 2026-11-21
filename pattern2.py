#n is number of lines which can be dynamic
n = 5

#loop for number of lines starting from 1 and ending at 5. (n+1) cause its exclusive.
for i in range(1,n+1):
    #printing '* 'i times in every iteration.
    print(f"* "*i)