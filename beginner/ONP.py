
try:    
    n=input()
    while n>0:
	s=raw_input()
	temp=[]
	st=""
	i=0
	while (i<len(s)):
		if s[i]=='(':
			i+=1
		if s[i].isalpha():
			st=st+s[i]
		else:
			if s[i]!=')' and s[i]!='(':
				temp.append(s[i])
		if s[i]==')':
				st=st+temp[-1]
				temp.pop()
			
		i=i+1
	print st
        n=n-1
except EOFError:
    print "EOF"