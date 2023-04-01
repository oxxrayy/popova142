spisok=[20,2,5,0,10,5]   #список 
a=1
while a==1:   #выполняет последовательность действий, пока условие истинной 
    for i in range (len(spisok)-1):  #ограничения значений
        if spisok[i]>spisok[i+1]:   #условие при котором мы потом переставляем элементы списка
            spisok[i],spisok[i+1]=spisok[i+1],spisok[i]  #перестановка
    if all(spisok[i]<=spisok[i+1] for i in range(len(spisok)-1)):  #сортировка списка на истинность
        a=2
print(spisok)
    
