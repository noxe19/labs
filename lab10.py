from tkinter import *

player = "X"
stop_game = False


def minimax(board, depth, is_maximizing):
    result = evaluate(board)
    if result is not None:
        return result

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_score = -float("inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def evaluate(board):
    for player in ["X", "O"]:
        for i in range(3):
            if board[i] == [player, player, player] or [board[j][i] for j in range(3)] == [player, player, player]:
                return 1 if player == "O" else -1
        if [board[i][i] for i in range(3)] == [player, player, player] or [board[i][2 - i] for i in range(3)] == [player, player, player]:
            return 1 if player == "O" else -1
    if all(cell != 0 for row in board for cell in row):
        return 0
    return None


def clicked(r, c, state, btns, main, lbl_main):

    global player
    global stop_game

    if player == "X" and state[r][c] == 0 and stop_game == False:
        btns[r][c].configure(text=player)
        state[r][c] = "X"
        win = check_win(state)
        if win == None:
            move = find_best_move(state)
            btns[move[0]][move[1]].configure(text="O")
            state[move[0]][move[1]] = "O"
            win1 = check_win(state)
            if win1 == "O":
                check_win_mes("O", main)
            elif win1 == "X":
                check_win_mes("X", main)
            elif win1 == 0:
                check_win_mes(0, main)
        elif win == 0:
            check_win_mes(win, main)
        else:
            check_win_mes(win, main)


def check_win_mes(win, main):
    info = Toplevel()
    info.title("Конец игры")
    info.geometry("200x200+100+100")
    info.resizable(width=False, height=False)
    info.grab_set()

    if win == 0:
        lbl = Label(info, text="Ничья", font="20", width=18)
    else:
        lbl = Label(info, text=f"Победитель: {win}", width=18, font="20")

    btn_ok = Button(info, text="Ок", width=5, command=lambda window1=main, window2=info: close_game(window1, window2))
    btn_continue = Button(info, text="Ёще раз", width=10, command=lambda window1=main, window2=info: game_restart(window1, window2))

    lbl.grid(column=0, row=0, pady=20)
    btn_ok.grid(column=0, row=2, pady=15)
    btn_continue.grid(column=0, row=3)


def close_game(main, info):

    global player

    info.destroy()
    main.destroy()
    player = "X"


def check_win(state):
    for player in ["X", "O"]:
        for i in range(3):
            if state[i] == [player, player, player] or [state[j][i] for j in range(3)] == [player, player, player]:
                return player

        if [state[i][i] for i in range(3)] == [player, player, player] or [state[i][2 - i] for i in range(3)] == [
            player, player, player]:
            return player
    if any(0 in i for i in state):
        return None
    else:
        return 0


def game():

    global player

    main = Tk()
    main.geometry('425x550+100+100')
    main.resizable(width=False, height=False)
    main.title('Крестики-нолики')

    btns = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    state = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    lbl_main = Label(text=f"Ходит: {player}", font="15", pady=15)

    for i in range(3):
        for j in range(3):
            btns[i][j] = Button(height=6, width=12, font="20", command=lambda r=i, c=j: clicked(r, c, state, btns, main, lbl_main))
            btns[i][j].grid(row=i, column=j)

    lbl_main.grid(row=4, column=1)

    main.mainloop()


def game_restart(main, info):
    global player

    info.destroy()
    main.destroy()
    player = "X"
    game()


game()
