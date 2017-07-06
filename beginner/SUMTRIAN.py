# cook your code here
try:
    n=input()
    while(n>0):
        tn=input()
        arr=list()
        for i in xrange(tn):
            row=map(int,raw_input().split())
            arr.append(row)
        for i in xrange(1,tn):
            arr[i][0]+=arr[i-1][0]
        for i in xrange(1,tn):
            arr[i][i]+=arr[i-1][i-1]
            
        for i in xrange(2,tn):
            for j in xrange(1,i):
                arr[i][j]+=max(arr[i-1][j-1],arr[i-1][j])
                
        print max(arr[tn-1])
        
        n-=1
except EOFError:
    print "EOF"