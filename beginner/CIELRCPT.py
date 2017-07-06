try:
    t=input()
    for j in xrange(t):
        p=input()
        count=0
        i=11
        while(p!=0):
            if (p/pow(2,i))>=1:
                p=p-pow(2,i)
                count=count+1
            else:
                i=i-1
        print count
        
except Exception, error:
    print "EofError" 