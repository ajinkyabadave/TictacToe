board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
isPlayer1 = True


def change_player():
    global isPlayer1
    isPlayer1 = not isPlayer1


# Function to print Tic Tac Toe
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1], values[2], values[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[4], values[5], values[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[7], values[8], values[9]))
    print("\t     |     |")
    print("\n")


def win_check(marker):
    for num in (1, 4, 7):
        if board[num] == board[num + 1] == board[num + 2] == marker:
            return True

    for num in (1, 2, 3):
        if board[num] == board[num + 3] == board[num + 6] == marker:
            return True

    if board[1] == board[5] == board[9] == marker:
        return True

    if board[3] == board[5] == board[7] == marker:
        return True

    return False


def draw_check():
    for num in range(1, 10):
        try:
            int(board[num])
        except:
            return False
    return True


def check_if_occupied(position):
    if board[position] == "X" or board[position] == "O":
        return True
    else:
        return False


def user_input():
    if isPlayer1:
        player = "Player 1"
        marker = "X"
    else:
        player = "Player 2"
        marker = "O"

    while (True):
        try:
            pos = int(input(f"{player} enter the position "))
            if pos not in range(1, 10):
                raise ValueError("Invalid position! Please enter a number between 1-9 ")

            if (check_if_occupied(pos)):
                raise Exception("Position already occupied! Please enter another position")

            board[pos] = marker
            print_board(board)
            change_player()
            break
        except ValueError:
            print("Invalid position! Please enter a number between 1-9 ")
        except:
            print("Position already occupied! Please enter another position")


print_board(board)

while (True):
    if isPlayer1:
        user_input()
        if (win_check('X')):
            winner = "Player 1"
            break;
        if (draw_check()):
            print("Match drawn!")
            break;


    elif (not isPlayer1):
        user_input()
        if (win_check('O')):
            winner = "Player 2"
            break
        if (draw_check()):
            print("Match drawn!")
            break;

print(f'{winner} wins the game!!')
