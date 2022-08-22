# Создайте программу для игры в "Крестики-нолики".

# board = list(range(1,10))

# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#         print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#         player_answer = input("Куда поставим " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if(str(board[player_answer-1]) not in "x0"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("x")
#         else:
#            take_input("0")
#         counter += 1
#         if counter > 4:
#            name = check_win(board)
#            if name:
#               print(name, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")

# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,. приоритет операций стандартный.

# import re

# actions = { "+": lambda x, y: str(float(x) + float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "-": lambda x, y: str(float(x) - float(y))}
 
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
# def my_eval(expresion: str) -> str:
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
#     return expresion
 
# exp = input('Введите выражение для вычисления ')
# print(my_eval(exp)) 

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def file_encode(data): 
#     encoding = '' 
#     prev_char = '' 
#     count = 1 
#     if not data: 
#         return '' 
#     for char in data: 
#         if char != prev_char:
#             if prev_char: 
#                 encoding += str(count) + prev_char 
#             count = 1 
#             prev_char = char 
#         else: count += 1
#     else: 
#         encoding += str(count) + prev_char 
#         return encoding

# encoded_val = file_encode('qqqqwwwweeerrrtyyyuiiii') 
# file_encode = open('encoded.txt', 'w')
# file_encode.write(encoded_val)

# def file_decode(data): 
#     decode = '' 
#     count = '' 
#     for char in data: 
#         if char.isdigit(): 
#             count += char 
#         else: 
#             decode += char * int(count) 
#             count = '' 
#     return decode

# decoded_val = file_decode('4q4w3e3r1t3y1u4i') 
# file_decode = open('decoded.txt', 'w')
# file_decode.write(decoded_val)
           
