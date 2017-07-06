# cook your code here
import math
try:
    a,b=raw_input().split()
    d=int(a)-int(b)
    if d%10==9:
        d-=1
    else:
        d+=1
    print d
except EOFError:
    print "EOF"