try:
    n=input()
    while n>0:
        s=raw_input()
        a=s[::-1]
        a=int(a)
        print a
        n=n-1
except EOFError:
    print "EOF" 