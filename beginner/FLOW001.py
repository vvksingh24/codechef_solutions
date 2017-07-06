try:    
    n=input()
    while (n>0):
        try:
           a=map(int,raw_input().split())
           print sum(a)
        except EOFError:
            print "EOF"
        n-=1
except EOFError:
    print "EOF"