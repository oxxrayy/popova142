
N10 = int(input('Введите исходное 10-тичное число: '))
p = 1
в то время как ((p<2) или (p>9)):
    p = int(input('Введите основание системы счисления в диапазоне [2; 9]: '))
k = int(1)
Np = int(0)
в то время как нет (N10 == 0):
    Np = Np + (N10 % p)*k
    k = k*10
    N10 = N10 // p
print('N' + str(p) + ' = ' + str(Np)))