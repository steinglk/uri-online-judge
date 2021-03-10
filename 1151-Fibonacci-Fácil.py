A = 0
B = 1
n=int(input())
for i in range(0, n):
	aux=A
	C = B+A
	A = B
	B = C
	if i < n-1:
		print('%d '%(aux), end="")
	else:
		print('%d'%(aux))