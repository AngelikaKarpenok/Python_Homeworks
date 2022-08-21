# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

list = ['qwe', '5', 'fhg', 'vj', '456', 'jgj', '23']

def FindNum():
    new_list = []
    i = 0
    while i < len(list):
        list_int = ''
        a = list[i]
        while '0' <= a <= '9':
            list_int += a
            i += 1
            if i < len(list):
                a = list[i]
            else:
                break
        i += 1
        if list_int != '':
            new_list.append(int(list_int))
    print(new_list)    

FindNum()

# Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

str = "asd", "qwe", "asd", "qwe", "zxc", "asd", "123"

def Entry():
    word = input()
    count = str.count(word)
    print(count)

Entry()