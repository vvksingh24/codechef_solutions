try:    
    n=input()
    while n>0:
        no=map(int,raw_input().split())
        r=no[0]%no[1]
        print r
        n=n-1
except EOFError:
    print "EOF"