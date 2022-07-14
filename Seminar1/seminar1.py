#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.

day = int(input('Input day of the week '))

def DayOfWeek(day):
    if day > 5 and day < 8:
        print('Its day of rest')
    if day > 0 and day < 6:
        print('Its workday')     
    if day < 1 or day > 7:
        print('Incorrect number of day')
    return day

DayOfWeek(day)

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
#и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Input X '))
y = int(input('Input Y '))

def FindNumberOfQuart():
    if x > 0 and y > 0:
        print('Quart1')
    if x > 0 and y < 0:
        print('Quart2')
    if x < 0 and y < 0:
        print('Quart3')
    if x < 0 and y > 0:
        print('Quart4')
    if x == 0 and y == 0:
        print('Point of intersection of the axes')
    
FindNumberOfQuart()