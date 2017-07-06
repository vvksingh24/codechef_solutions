try:    
    n=input()
    while n>0:
        no=raw_input()
        x=map(int,no)
        print sum(x)
        n=n-1
except EOFError:
    print "EOF"