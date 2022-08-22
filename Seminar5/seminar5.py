#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов. 
#Это не просто сумма всех коэффициентов.
#Сумма многочленов равна многочлену, членами которого 
#являются все члены данных многочленов.

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratio(k):
#     ratio = [randint(0, 10) for i in range (k + 1)]
#     while ratio[0] == 0:
#         ratio[0] = randint(1, 10) 
#     return ratio

# def get_polynomial(k, ratio):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio, var, range(k, 1, -1), 
#     fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')

# ratio = get_ratio(k)
# polynom1 = get_polynomial(k, ratio)

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom1)

# k = randint(2, 5)

# ratio = get_ratio(k) 
# polynom2 = get_polynomial(k, ratio)

# with open('Polynomial2.txt', 'w') as data:
#     data.write(polynom2)

# import re
# import itertools

# file_sum = 'Sum_polynomials.txt'

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = polynom1
# pol2 = polynom2
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)

#Дан список чисел. Создайте список, в который попадают числа, 
#описываемые возрастающую последовательность. 
#Порядок элементов менять нельзя.

# nums = [3, 8, 9, 3, 2, 6, 1, 7]

# def Increase(nums):
#     incr = [nums[0]]
#     for i in nums:
#         if i > max(incr):
#             incr.append(i)
#     return incr
    
# print(Increase(nums))

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# from random import randint, choice

# greeting = ('Привет! Это игра "Кто съест все конфеты?" '
#             'Правила игры: На столе лежит определённое количество конфет, '
#             'за один ход можно взять не более заданного количества конфет. '
#             'Все конфеты оппонента достаются сделавшему последний ход. '
#             'Итак, начнём!')

# messages = ['теперь твоя очередь брать конфеты', 'берите конфеты',
#             'сколько конфет хотите?', 'берите, не стесняйтесь', 'Ваш ход']


# def introduce_players():
#     player1 = input('Привет. Как тебя зовут?\n')
#     player2 = 'Медок'
#     print(f'Очень приятно, меня зовут {player2}')
#     return [player1, player2]


# def get_rules(players):
#     n = int(input('Сколько будет конфет?\n '))
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = int(input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [n, m, int(first)]


# def play_game(rules, players, messages):
#     count = rules[2]
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = randint(1, rules[1])
#             print(f'Я беру {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(f'Это слишком много, можно взять не более {rules[1]} конфет{letter}')
#                 shot = 3
#                 while shot > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуй ещё раз, у тебя {shot} попытки')
#                     move = int(input())
#                     shot -= 1
#                 else:
#                     return print(f'Очень жаль, у тебя не осталось попыток.')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[count % 2]

# print(greeting)

# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# if not winer:
#     print('Game over')
# else:
#     print(f'Поздравляю, победил {winer}!')