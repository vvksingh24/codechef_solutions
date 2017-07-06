try:    
    n=input()
    while n!=0:
        lst=map(int,raw_input().split())
        newlst=[None]*n
        for i in range(n):
            newlst[int(lst[i])-1]=i+1
        if newlst==lst:
            print "ambiguous"
        else:
            print "not ambiguous"
        n=input()
except EOFError:
    print "EOF"