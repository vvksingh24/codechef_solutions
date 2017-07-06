import math
try:
    n=input()
    while n>0:
        no=input()
        m=1
        while(no>0):
            m=m*no
            no-=1
        print m
        n=n-1
except EOFError:
    print "EOF" 