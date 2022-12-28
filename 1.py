def f():
     def ff (f):
          return f
     a= input ('Введите фамилию : ')
     a=ff (a)
     print (a)
     
sp = ['1. программа вывода фамилии ']
print (sp)
b = input('выбирете пункт ')
if b == '1' :
     f()
     
