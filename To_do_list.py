import datetime
with open('Categorii.txt', 'w+') as file:
    nume_var = input('Alege categoria: ')
    file.write(nume_var)
with open('Taskuri.txt', 'w+') as file:
    nume_var1 = input('Alege taskul: ')
    file.write(nume_var1)
    file.write(input('Alege numele persoana care face taskul:'))
    file.write(input('Selectati data death line: '))
   #if list[nume_var1]