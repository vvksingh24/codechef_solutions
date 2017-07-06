# cook your code here
try:
    n=input()
    while n>0:
        a,b=raw_input().split()
        lst=[]
        c=""
        s=""
        l=[]
        for i in range(int(a)):
            lst.append(i+1)
        l=map(int,raw_input().split())
        for i in l:
            lst.remove(i)
        lst.sort()
        for i in range(0,len(lst),2):
            c=c+" "+str(lst[i])
        for i in range(1,len(lst),2):
            s=s+" "+str(lst[i])
        print c
        print s
        n=n-1
except EOFError:
    print "EOF"