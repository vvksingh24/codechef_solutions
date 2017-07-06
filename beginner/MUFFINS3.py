try:
    t=input()
    for i in xrange(t):
        n=input()
        a=int((n/2)+1)
        if n==2:
            print '2'
        else:
            print a
except Exception, error:
    print "EofError" 