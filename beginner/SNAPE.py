import math
try:    
    n=input()
    while n>0:
        no=map(int,raw_input().split())
        rs1=math.sqrt(no[1]*no[1]-no[0]*no[0])
        rs2=math.sqrt(no[1]*no[1]+no[0]*no[0])
        print "%.5f %.5f"% (rs1,rs2)
        n=n-1
except EOFError:
    print "EOF"