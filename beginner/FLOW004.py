try:
    n=input()
    while n>0:
        s=raw_input()
        a=int(s[0])+int(s[-1])
        print a
        
        n=n-1
except EOFError:
    print "EOF" 