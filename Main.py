
def display(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])


board = [" "," "," "," "," "," "," "," "," "," "]


display(board)


def player_input():
    marker = ''
    while marker != "X" and marker != "O":
        marker = input(" Player 1 choose 'X' or 'O' ").upper()
    p1 = marker
    if p1 == 'X':
        return 'X','O'
    else :
        return'O','X'


p1,p2 = player_input()


def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[7] == board[5] == board[3] == marker))


def pos_availability(pos):
    return not board[pos] == ' '


def logic():
    flag = 0
    game_on = False
    while not game_on:
        if flag == 0:
            pos = int(input("Player 1's turn"))
            while pos_availability(pos):
                pos = int(input("place already taken Enter a new position"))
                pos_availability(pos)
            flag = 1
            board[pos] = p1
            display(board)
            game_on = win_check(board, p1)

        else:
            pos = int(input("Player 2's turn"))
            while pos_availability(pos):
                pos = int(input("place already taken Enter a new position"))
                pos_availability(pos)
            flag = 0
            board[pos] = p2
            display(board)
            game_on = win_check(board, p2)

    if game_on:
        if flag == 1:
            print("Winner is Player 1")
        else:
            print("Winner is player 2")


logic()