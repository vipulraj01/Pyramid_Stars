n = int(input("Enter the number of row you want to print : "))
m = int(input(" Press 0 for UPWARD Pyramid \n Press 1 for DOWNWARD Pyramid"))
if m == 0:
    for i in range(0,n+1):
        print("*"*int(i))
if m == 1:
    for i in range(n,0,-1):
        print("*"*int(i))