p1,n=input().split()
ob=abs(len(p1)-len(n))
for i in range(len(p1)):
	if len(n)==1 and n[i] in p1:
		break
	elif i>=len(p1) or i>=len(n):
		break
	elif n[i]!=n[i] and n[i]:
		ob=ob+1
print(ob)
