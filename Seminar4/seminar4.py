#Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.

num = int(input('Integer: '))

def Factors(n):
    div = 2
    while div ** 2 <= n:
        if n % div == 0:
            n //= div
            print(div)
        else:
            div += 1
    if n != 1:
        print(n)

Factors(num)

