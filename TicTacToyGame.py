from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Global variable
active_player = 0
click_count = 0
pw = [0, 0]     # Sum of player 1 and 2 win games
p1 = []         # What player 1 selected
p2 = []         # What player 2 selected

root = Tk()
root.title("Tic Tac Toy: Player {}".format(active_player + 1))


def create_button(btn_id, row, column):
    button = ttk.Button(root, text=" ", command=lambda: button_click(btn_id))
    button.grid(row=row, column=column, sticky="snew", ipadx=40, ipady=40)
    return button


# Create buttons
buttons = [create_button(i, int((i - 1) / 3), (i - 1) % 3) for i in range(1, 10)]


def button_click(btn_id):
    global active_player, p1, p2
    set_layout(btn_id, "X" if not active_player else "O")
    p = p1 if not active_player else p2
    p.append(btn_id)
    print("Player {}: {}".format(active_player + 1, p))

    # No winner or drawn: switch player
    if not check_winner_drawn(active_player, p):
        active_player = not active_player
        root.title("Tic Tac Toy: Player {}".format(active_player + 1))


def set_layout(btn_id, player_symbol="", disabled=True):
    global buttons
    if player_symbol != "":
        buttons[btn_id - 1].config(text=player_symbol)
    else:
        if disabled:
            buttons[btn_id - 1].state(["disabled"])
        else:
            # New game
            buttons[btn_id - 1].config(text="")
            buttons[btn_id - 1].state(["!disabled"])


def check_winner_drawn(player_num, player_list):
    global click_count, pw, pws
    click_count += 1
    winner = -1
    lines = {1: (1, 3, 4), 2: (3,), 3: (2, 3), 4: (1,), 7: (1,)}
    for sn, eds in lines.items():
        for ed in eds:
            if sn in player_list and sn + ed in player_list and sn + ed * 2 in player_list:
                winner = player_num + 1
                pw[player_num] += 1
                break
        if winner != -1:
            messagebox.showinfo(title="Congratulations!", message="Player " + str(winner) + " Win!")
            pws[player_num].config(text="Player {} wins: {}".format(player_num + 1, pw[player_num]))
            for i in range(1, 10):
                set_layout(i)
            return True

    # Drawn game or continue
    if click_count == 9:
        for i in range(1, 10):
            set_layout(i)
        if winner == -1:
            messagebox.showinfo(title="Drawn Game.", message="Two players drew.")
            return True
    else:
        return False


def new_game():
    global active_player, click_count, p1, p2
    active_player = 0
    click_count = 0
    p1.clear()
    p2.clear()
    for i in range(1, 10):
        set_layout(i, disabled=False)


new_game_btn = ttk.Button(root, text="New Game", command=new_game)
new_game_btn.grid(row=3, column=1, sticky="snew", ipadx=40, ipady=20)

p1w = ttk.Label(root, text="Player 1 wins: {}".format(pw[0]), anchor=CENTER)
p1w.grid(row=3, column=0, sticky="snew", ipadx=40, ipady=20)
p2w = ttk.Label(root, text="Player 2 wins: {}".format(pw[1]), anchor=CENTER)
p2w.grid(row=3, column=2, sticky="snew", ipadx=40, ipady=20)

pws = [p1w, p2w]

# Run GUI with IDLE
root.mainloop()
