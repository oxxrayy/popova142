abl = [[n for n in range(0,10)], ['0000000','0001111','0010110','0011001','0100101','0101010','0110011','0111100','1000011','1001100']]
Code = ''
def Distance(A, B):
    K = int(7)
    for i in range(1,8):
        if (int(A)%10) == (int(B)%10):
            K = K-1
        A = A[0:len(A)-1]
        B = B[0:len(B)-1]
    return(K)
while not len(Code) == 7:
    Code = input('Код = ')
Код = 0111111
minD = Distance(Code, Tabl[1][0])
Num = 0
for j in range(1,10):
    D = Distance(Code, Tabl[1][j])
    if D<minD:
        minD = D
        Num = j
if minD == 0:
    print(f'Код верный: символ {Tabl[0][Num]}')
elif minD == 1:
    print(f'Код исправлен: символ {Tabl[0][Num]}')    
else: print('Код неверный.')
Код неверный.
