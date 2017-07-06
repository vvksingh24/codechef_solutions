import math
try:
    n=input()
    while n>0:
        no=input()
        s=math.sqrt(no)
        print int(s)
        n=n-1
except EOFError:
    print "EOF" 