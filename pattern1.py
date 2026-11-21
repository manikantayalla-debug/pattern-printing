#n is number of lines which can be dynamic
n = 4
#loop for number of lines starting from 1 and ending at 4. (n+1) cause its exclusive.
for i in range(1,n+1):
    #printing '*' and space n times in every iteration
    print(f"* "*n)
