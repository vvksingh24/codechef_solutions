n=input()
while n>0:
    s=map(int,raw_input().split())
    if s[1]<s[0]:
        print "%d %d"%(s[0],sum(s))
    else:
        print "%d %d"%(s[1],sum(s))
    n=n-1