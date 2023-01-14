for i in range(1,100):
    N=''
    N2= (bin(i)[2:])
    if N2.count('1')%2==0:
        N= '10' + N2[2:] + '0'
    if N2.count('1')%2!=0:
        N= '1'+ '11'+ N2[2:]
    if int(N,2)>40:
        print(i, int(N,2))
        break
