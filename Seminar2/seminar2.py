#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Input number ')

def SumOfDigits(num):
    x = num.split(".") 
    a = int(x[0]) 
    b = int(x[1]) 
    sum = 0
    while (a != 0):
        sum += a % 10
        a = a // 10
    while (b != 0):
        sum += b % 10
        b = b // 10
    print(sum)

SumOfDigits(num)


#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Input number '))

def Multiple(num):
    mult = 1
    for i in range(num):
        mult*= i+1
        print(mult)
    
Multiple(num)
