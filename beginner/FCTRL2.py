def fact(x):
    if x<=1:
        return 1
    else:
        return x*fact(x-1)
no=raw_input("")
lst=list()
n=int(no)
while n>0:
    a=raw_input("")
    x=int(a)
    lst.append(x)
    n=n-1
for b in lst:
    y=fact(b)
    print y 