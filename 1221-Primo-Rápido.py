Nentr = int(input())

for i in range(0, Nentr):
    primo=int(input())
    div=0
    #for j in range(2, int(sqrt(primo))):
    j=2
    while j*j <= primo:
        if primo%j == 0:
            div+=1
            break
        j+=1
    if div == 0:
        print('Prime')
    else:
        print('Not Prime')
