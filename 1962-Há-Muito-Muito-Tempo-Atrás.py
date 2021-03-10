Nentr = int(input())
for i in range(0, Nentr):
	N = int(input())
	if 2015 - N < 0:
		print('%d A.C.'%(N-2014))
	elif 2015 - N == 0:
		print('1 A.C.')
	else:
		print('%d D.C.'%(2015-N))
