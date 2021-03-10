S, V, F = map(int, input().split())
if S+V < 24 and S+V+F < 24:
	if S+V+F < 0:
		print(S+V+F+24)
	else:
		print(S+V+F)
elif S+V < 24 and S+V+F >=24:

		print(S+V+F-24)
elif S+V >= 24:
	if S+V+F <0:
		print(S+V+F+24)
	else:
		print(S+V-24+F)