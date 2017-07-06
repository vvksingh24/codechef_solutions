def computeHCF(x, y):
   while(y):
       x, y = y, x % y
 
   return x
try:
    n=input()
    while n>0:
        i=map(int,raw_input().split())
        flag=0
        hcf=0
        i.pop(0)
        hcf = reduce(lambda x,y:computeHCF(x,y),i)
        for x in i:
            print x/hcf,
        print ""
        n=n-1
except EOFError:
    print "EOF" 