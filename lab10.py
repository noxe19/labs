from random import *
from tkinter import *

player = "X"
stop_game = False


def bot(r, c, state, btns, main, lbl_main):
    global player

    if any(0 in i for i in state):
        while True:
            r = randint(0, 2)
            c = randint(0, 2)
            if state[r][c] == 0:
                state[r][c] = "O"
                btns[r][c].configure(text=player)
                main.update()
                check_win(state, main)
                player = "X"
                lbl_main.configure(text=f"Ходит: {player}")
                break


def clicked(r, c, state, btns, main, lbl_main):
    global player
    global stop_game

    if player == "X" and state[r][c] == 0 and stop_game == False:
        btns[r][c].configure(text=player)
        state[r][c] = "X"
        check_win(state, main)
        player = "O"
        lbl_main.configure(text=f"Ходит: {player}")
        bot(r, c, state, btns, main, lbl_main)

    elif player == "O" and state[r][c] == 0 and stop_game == False:
        btns[r][c].configure(text=player)
        state[r][c] = "O"
        check_win(state, main)
        player = "X"
        lbl_main.configure(text=f"Ходит: {player}")
        bot(r, c, state, btns, main, lbl_main)


def check_win_mes(win, main):
    info = Toplevel()
    info.title("Конец игры")
    info.geometry("200x200+100+100")
    info.resizable(width=False, height=False)
    info.grab_set()
    if win != 0:
        lbl = Label(info, text=f"Победитель: {win}", width=18, font="20")
    else:
        lbl = Label(info, text="Ничья", font="20", width=18)
    btn_ok = Button(info, text="Ок", width=5, command=lambda window1=main, window2=info: close_game(window1, window2))
    btn_continue = Button(info, text="Ёще раз", width=10,
                          command=lambda window1=main, window2=info: game_restart(window1, window2))

    lbl.grid(column=0, row=0, pady=20)
    btn_ok.grid(column=0, row=2, pady=15)
    btn_continue.grid(column=0, row=3)


def close_game(main, info):
    global player

    main.destroy()
    info.destroy()
    player = "X"


def check_win(state, main):
    if state[0][0] == state[0][1] == state[0][2] != 0:
        check_win_mes(state[0][0], main)
    elif state[1][0] == state[1][1] == state[1][2] != 0:
        check_win_mes(state[1][0], main)
    elif state[2][0] == state[2][1] == state[2][2] != 0:
        check_win_mes(state[2][0], main)
    elif state[0][0] == state[1][0] == state[2][0] != 0:
        check_win_mes(state[0][0], main)
    elif state[0][1] == state[1][1] == state[2][1] != 0:
        check_win_mes(state[0][1], main)
    elif state[0][2] == state[1][2] == state[2][2] != 0:
        check_win_mes(state[0][2], main)
    elif state[0][0] == state[1][1] == state[2][2] != 0:
        check_win_mes(state[0][0], main)
    elif state[2][0] == state[1][1] == state[0][2] != 0:
        check_win_mes(state[2][0], main)
    elif not (any(0 in i for i in state)):
        check_win_mes(0, main)


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
            btns[i][j] = Button(height=6, width=12, font="20",
                                command=lambda r=i, c=j: clicked(r, c, state, btns, main, lbl_main))
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