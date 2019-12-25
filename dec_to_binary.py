n=int(input())
s=[]
while(n!=0):
	d=n%2
	s.append(d)
	n=n//2
h=s[::-1]
print(*h,sep="")