import math
try:
    n=input()
    while n>0:
        no=map(int,raw_input().split())
        no.sort()
        print no[-2]
        n=n-1
except EOFError:
    print "EOF" 