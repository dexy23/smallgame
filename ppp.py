# -*- coding: utf-8 -*-
# Хрестики-нулики

X = "X"
O = "O"
EMPTY = " "
TIE = "Нічия"
NUM_SQUARES = 9

def display_instruct():
"""Відображення ігрової інструкції на моніторі."""
print(
"""
Ласкаво просимо до найбільшого інтелектуального виклику всіх часів: хрестики-нулики.
Щоб зробити хід, введіть число від 0 до 8. Числа відповідають полям дошки, як показано:

0 | 1 | 2
—-------
3 | 4 | 5
—-------
6 | 7 | 8

"""
)

def ask_yes_no(question):
"""Запитання з відповіддю так або ні."""
response = None
while response not in ("y", "n"):
response = input(question).lower()
return response

def ask_number(question, low, high):
"""Просить ввести число з діапазону."""
response = None
while response not in range(low, high):
response = int(input(question))
return response

def pieces():
"""Вирішення хто ходить перший."""
go_first = ask_yes_no("Хочеш ходити першим? (y/n): ")
if go_first == "y":
print("\nНу добре, якщо тобі потрібна фора - грай хрестиками.")
human = X
computer = O
else:
print("\nЗначить я починаю.")
computer = X
human = O
return computer, human

def new_board():
"""Створює нову ігрову дошку."""
board = []
for square in range(NUM_SQUARES):
board.append(EMPTY)
return board

def display_board(board):
"""Відображає ігрову дошку на екрані."""
print("\n\t", board[0], "|", board[1], "|", board[2])
print("\t", "---------")
print("\t", board[3], "|", board[4], "|", board[5])
print("\t", "---------")
print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
"""Створює список доступних ходів."""
moves = []
for square in range(NUM_SQUARES):
if board[square] == EMPTY:
moves.append(square)
return moves

def winner(board):
"""Визначає переможця в грі."""
WAYS_TO_WIN = ((0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6))

for row in WAYS_TO_WIN:
if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
winner = board[row[0]]
return winner

if EMPTY not in board:
return TIE

return None

def human_move(board, human):
"""Отриммує хід людини."""
legal = legal_moves(board)
move = None
while move not in legal:
move = ask_number("Вибери одне з полів (0 - 8):", 0, NUM_SQUARES)
if move not in legal:
print("\nЦе поле вже зайняте, обери інше дурна людино!\n")
print("Добре...")
return move

def computer_move(board, computer, human):
"""Робить хід за комп'ютер."""
board = board[☺
BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

print("Я виберу поле номер", end=" ")

for move in legal_moves(board):
board[move] = computer
if winner(board) == computer:
print(move)
return move
board[move] = EMPTY

for move in legal_moves(board):
board[move] = human
if winner(board) == human:
print(move)
return move
board[move] = EMPTY

for move in BEST_MOVES:
if move in legal_moves(board):
print(move)
return move
Андрій
# -*- coding: utf-8 -*-
# Хрестики-нулики

X = "X"
O = "O"
EMPTY = " "
TIE = "Нічия"
NUM_SQUARES = 9

def display_instruct():
"""Відображення ігрової інструкції на моніторі."""
print(
"""
Ласкаво просимо до найбільшого інтелектуального виклику всіх часів: хрестики-нулики.
Щоб зробити хід, введіть число від 0 до 8. Числа відповідають полям дошки, як показано:

0 | 1 | 2
—-------
3 | 4 | 5
—-------
6 | 7 | 8

"""
)

def ask_yes_no(question):
"""Запитання з відповіддю так або ні."""
response = None
while response not in ("y", "n"):
response = input(question).lower()
return response

def ask_number(question, low, high):
"""Просить ввести число з діапазону."""
response = None
while response not in range(low, high):
response = int(input(question))
return response

def pieces():
"""Вирішення хто ходить перший."""
go_first = ask_yes_no("Хочеш ходити першим? (y/n): ")
if go_first == "y":
print("\nНу добре, якщо тобі потрібна фора - грай хрестиками.")
human = X
computer = O
else:
print("\nЗначить я починаю.")
computer = X
human = O
return computer, human

def new_board():
"""Створює нову ігрову дошку."""
board = []
for square in range(NUM_SQUARES):
board.append(EMPTY)
return board

def display_board(board):
"""Відображає ігрову дошку на екрані."""
print("\n\t", board[0], "|", board[1], "|", board[2])
print("\t", "---------")
print("\t", board[3], "|", board[4], "|", board[5])
print("\t", "---------")
print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
"""Створює список доступних ходів."""
moves = []
for square in range(NUM_SQUARES):
if board[square] == EMPTY:
moves.append(square)
return moves

def winner(board):
"""Визначає переможця в грі."""
WAYS_TO_WIN = ((0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6))

for row in WAYS_TO_WIN:
if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
winner = board[row[0]]
return winner

if EMPTY not in board:
return TIE

return None

def human_move(board, human):
"""Отриммує хід людини."""
legal = legal_moves(board)
move = None
while move not in legal:
move = ask_number("Вибери одне з полів (0 - 8):", 0, NUM_SQUARES)
if move not in legal:
print("\nЦе поле вже зайняте, обери інше дурна людино!\n")
print("Добре...")
return move

def computer_move(board, computer, human):
"""Робить хід за комп'ютер."""
board = board[☺
BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

print("Я виберу поле номер", end=" ")

for move in legal_moves(board):
board[move] = computer
if winner(board) == computer:
print(move)
return move
board[move] = EMPTY

for move in legal_moves(board):
board[move] = human
if winner(board) == human:
print(move)
return move
board[move] = EMPTY

for move in BEST_MOVES:
if move in legal_moves(board):
print(move)
return move

def next_turn(turn):
"""Здійснює перехід ходу."""
if turn == X:
return O
else:
return X


def congrat_winner(the_winner, computer, human):
"""Вітає переможця гри."""
if the_winner != TIE:
print(the_winner, "переміг!\n")
else:
print("Нічия!\n")

if the_winner == computer:
print("Як не дивно, перемога вкотре за мною. \n" \
"Що ще раз доводить що комп'ютери перевершують людей у всьому.")

elif the_winner == human:
print("Тільки не це! Це неможливо! Ти якось зшахраював. \n" \
"Ніколи більше!")

elif the_winner == TIE:
print("Ти неймовірний везунчик: ти зміг звести гру внічию. \n" \
"Святкуй свій успіх... навряд ти зможеш це повторити.")

def main():
display_instruct()
computer, human = pieces()
turn = X
board = new_board()
display_board(board)

while not winner(board):
if turn == human:
move = human_move(board, human)
board[move] = human
else:
move = computer_move(board, computer, human)
board[move] = computer
display_board(board)
turn = next_turn(turn)

the_winner = winner(board)
congrat_winner(the_winner, computer, human)

# запуск
програми
main()
input("\n\nНатисніть Enter для виходу.")