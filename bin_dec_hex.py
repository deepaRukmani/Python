binary=int(input())
des, i, n = 0, 0, 0
while(binary != 0): 
    dec = binary % 10
    des= des + dec * pow(2, i) 
    binary = binary//10
    i += 1
print(des)     
d=[]
rem=0
while(des>0):
	rem=int(des%16)
	if(rem<10):
		d.append(chr(rem+48))
	else:
		d.append(chr(rem+55))
	des=des//16
hex=d[::-1]
print(*hex,sep="")
