n=input()
while n>0:
    no=raw_input()
    count=0
    for i in no:
        if i=='4':
            count+=1
    print count
    n=n-1