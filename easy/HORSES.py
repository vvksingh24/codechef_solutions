# cook your code here
try:
    n=input()
    while n>0:
        h=input()
        s=map(int,raw_input().split())
        s.sort()
        m=999999999
        for i in range(1,len(s)):
            d=s[i]-s[i-1]
            if d<m:
                m=d
        print m
        n=n-1
except EOFError:
    print "EOF"