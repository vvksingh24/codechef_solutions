# cook your code here
import math
try:
    n=input()
    while n>0:
        r=input()
        p=[]
        for i in range(3):
            row=map(int,raw_input().split())
            p.append(row)
        d1=math.sqrt(pow((p[1][0]-p[0][0]),2)+pow((p[1][1]-p[0][1]),2))
        d2=math.sqrt(pow((p[1][0]-p[2][0]),2)+pow((p[1][1]-p[2][1]),2))
        d3=math.sqrt(pow((p[2][0]-p[0][0]),2)+pow((p[2][1]-p[0][1]),2))
        if d1<=r and d2<=r:
            print "yes"
        elif d2<=r and d3<=r:
            print "yes"
        elif d1<=r and d3<=r:
            print "yes"
        else:
            print "no"
        n=n-1
except EOFError:
    print "EOF"