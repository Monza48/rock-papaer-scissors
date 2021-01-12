import random
from tkinter import *

# Motståndare till spelet. (40 st)
opponents = ["Anders", "Stefan", "Lisa", "Greta", "Oscar", "Algot", "Måns", "Lovisa", "Björn", "Fredrik", "Johanna",
             "Sofia", "Henrik", "Jacob", "Filippa", "Emilia", "Gustaf", "Maria", "Klara", "Tova", "Erik", "Filip",
             "Theo", "Lars", "Sixten", "Isac", "Leo", "Markus", "August", "Mikael", "Thea", "Adrian", "Wilma", "Karl",
             "Gabriel", "Axel", "Stina", "Frans", "Ebba", "Matilda"]

# Skapar startvärden för motståndaren och använderens poäng samt rundor spelade.
opponent_score = 0
user_score = 0
rounds_played = 0
opponent_name = ''

# Skapar reglerna så att datorn senare ska veta vad som slår vad.
game_rules = {
    "sten": {"sten":1, "påse":0, "sax":2},
    "påse": {"sten":2, "påse":1, "sax":0},
    "sax": {"sten":0, "påse":2, "sax":1}
}

# Skapar en funktion som ger använderen en slumpad motståndare.
def random_opponent_name():
    return random.choice(opponents)

# Skapar en funktion som senare kommer användas för att visa meny layouten igen
def show_menu():
    for x in menu_labels:
        x.grid()

# Skapar en funktion som senare kommer användas för att ta bort själva spel-layouten.
def remove_game_labels():
    for x in game_labels:
        x.grid_remove()

# Skapar en funktion som senare kommer användas för att ta bort själva game over layouten.
def remove_game_over_labels():
    for x in game_over_labels:
        x.grid_remove()

# Skapar själva start-layouten för spelet.
def start_game(playername):
    global opponent_name
    opponent_name = random_opponent_name()

    # For loopen tar bort start menyn.
    for x in menu_labels:
        x.grid_remove()

    # Meddelar att spelet har startat samt vem man möter.
    label_game_header.config(text = f'Du möter nu {opponent_name}. Lycka till!')
    label_game_header.grid(row=0, columnspan=6, padx=115, pady=(10, 0))
    label_line.config(text = f'{draw_line * 95}')
    label_line.grid(row=1, columnspan=10)
    label_outcome_header.config(text = "Resultat")
    label_outcome_header.grid(row=3, column = 2, columnspan = 2)

    # Motståndarens statistik
    label_opponent_name.config(text=opponent_name)
    label_opponent_name.grid(row=3, column=4, columnspan=2)
    label_opponent_choice.config(text=f'val: ')
    label_opponent_choice.grid(row=4, column= 4, columnspan = 2)
    label_opponent_score.config(text=f'poäng: {opponent_score}')
    label_opponent_score.grid(row = 5, column= 4, columnspan = 2)

    # Användarens statistik
    label_username.config(text=playername)
    label_username.grid(row=3, columnspan=2)
    label_user_choice.config(text=f'val: ')
    label_user_choice.grid(row=4, column= 0, columnspan = 2)
    label_user_score.config(text=f'poäng: {user_score}')
    label_user_score.grid(row = 5, column= 0, columnspan = 2)

    # Sten, sax, påse knapparna
    btn_rock.config(text="Sten", image=photo_rock, compound=LEFT)
    btn_rock.grid(row=2, column=0, pady=20)
    btn_scissor.config(text="Sax", image=photo_scissor, compound=LEFT)
    btn_scissor.grid(row = 2, column = 2, columnspan=2)
    btn_paper.config(text="Påse", image=photo_paper, compound=LEFT)
    btn_paper.grid(row=2, column=5)

    if rounds_choice.get() == 0:
        label_best_of_rounds.config(text=f'Du spelar med oändligt många rundor', font="Arial 13")
        label_best_of_rounds.grid(row=6, columnspan=6, pady=(30, 0))

    else:
        label_best_of_rounds.config(text=f'Bäst av {rounds_choice.get()} rundor!', font="Arial 13")
        label_best_of_rounds.grid(row=6, columnspan=6, pady=(30, 0))

# Denna funktionen kommer köras varje gång man klickar sten, sax eller påse.
def outcome_handler(user_choice):
    global opponent_score
    global user_score
    global rounds_played
    rounds_played += 1
    opponent_choice = random.choice(['sten', 'sax', 'påse'])
    best_of_rounds = rounds_choice.get()

    # Detta väljer resultaten mellan användarens val och motståndarens. (Se game_rules dictionaryn på line 21.)
    result = game_rules[user_choice][opponent_choice]

    # Detta visar att användaren har vunnit rundan och därmed får ett poäng.
    if result == 2:
        user_score += 1
        label_outcome.config(text = f'{username.get()} vann!', fg="green")
        label_outcome.grid(row = 4, column=2, columnspan=2)

    # Detta visar att rundan blev lika och ingen får något poäng.
    elif result == 1:
        label_outcome.config(text = f'Lika!', fg="orange")
        label_outcome.grid(row = 4, column=2, columnspan=2)

    # Detta visar att motståndaren har vunnit rundan och därmed får ett poäng.
    elif result == 0:
        opponent_score += 1
        label_outcome.config(text = f'{opponent_name} vann!', fg="red")
        label_outcome.grid(row = 4, column=2, columnspan=2)

    label_user_choice.config(text=f'val: {user_choice}')
    label_user_choice.grid(row=4, column= 0, columnspan = 2)
    label_user_score.config(text=f'poäng: {user_score}')
    label_user_score.grid(row = 5, column= 0, columnspan = 2)

    label_opponent_choice.config(text=f'val: {opponent_choice}')
    label_opponent_choice.grid(row=4, column= 4, columnspan = 2)
    label_opponent_score.config(text=f'poäng: {opponent_score}')
    label_opponent_score.grid(row = 5, column= 4, columnspan = 2)

    label_rounds_played.config(text=""f'Rundor spelade: {rounds_played}')
    label_rounds_played.grid(row=5, column=2, columnspan=2)

    points_labels = [label_opponent_choice, label_opponent_score, label_user_choice, label_user_score, label_rounds_played]

    # Här skapar vi ett if-statement som läser av om antalet valda rundor har spelats
    if rounds_played == best_of_rounds:
        remove_game_labels()
        for x in points_labels:
            x.grid_remove()

        if user_score > opponent_score:
            label_game_over_score.config(text=f'Resultatet blev: {user_score} - {opponent_score} till', fg = "green")
            label_game_over_score.grid(row=0, columnspan=6, pady=20, padx = 40)
            label_winner_name.config(text=f'{username.get()}!', fg = "green")
            label_winner_name.grid(row=1, columnspan=6, pady=(0, 30))

            btn_main_menu.config(text="Main Menu", bg="black", fg="white")
            btn_main_menu.grid(row=2, column=2, columnspan=1)

            btn_new_opponent.config(text="Ny motståndare", bg="black", fg="white")
            btn_new_opponent.grid(row=2, column=3, columnspan=1)

            txt_file = open("winners.txt", "a")
            txt_file.write(f'{username.get()} vann\n')
            txt_file.close()

            opponent_score = 0
            user_score = 0
            rounds_played = 0

        elif user_score < opponent_score:
            label_game_over_score.config(text=f'Resultatet blev: {user_score} - {opponent_score} till', fg = "red")
            label_game_over_score.grid(row=0, columnspan=6, pady=20, padx = 40)
            label_winner_name.config(text=f'{opponent_name}!', fg = "red")
            label_winner_name.grid(row=1, columnspan=6, pady=(0, 30))

            btn_main_menu.config(text="Main Menu", bg="black", fg="white")
            btn_main_menu.grid(row=2, column=2, columnspan=1)

            btn_new_opponent.config(text="Ny motståndare", bg="black", fg="white")
            btn_new_opponent.grid(row=2, column=3, columnspan=1)

            txt_file = open("winners.txt", "a")
            txt_file.write(f'{opponent_name} vann\n')
            txt_file.close()

            opponent_score = 0
            user_score = 0
            rounds_played = 0

        elif user_score == opponent_score:
            label_game_over_score.config(text=f'Resultatet blev: {user_score} - {opponent_score}', fg = "orange")
            label_game_over_score.grid(row=0, columnspan=6, pady=20, padx = 70)
            label_winner_name.config(text=f'Lika!', fg = "orange")
            label_winner_name.grid(row=1, columnspan=6, pady=(0, 30))

            btn_main_menu.config(text="Main Menu",bg="black", fg="white")
            btn_main_menu.grid(row=2, column=2)

            btn_new_opponent.config(text="Ny motståndare", bg="black", fg="white")
            btn_new_opponent.grid(row=2, column=3)

            txt_file = open("winners.txt", "a")
            txt_file.write(f'Matchen blev lika\n')
            txt_file.close()

            opponent_score = 0
            user_score = 0
            rounds_played = 0


# ---------------------------------- GUI BÖRJAR HÄR ----------------------------------- #
root = Tk()
root.geometry("469x300")
blank_space = " "
draw_line = "-"
root.title(f'{40 * blank_space} Sten Sax Påse')

# Bilder på de olika valen
photo_rock = PhotoImage(file = r"bilder\sten.png").subsample(32, 29)
photo_scissor = PhotoImage(file = r"bilder\sax.png").subsample(13, 15)
photo_paper = PhotoImage(file = r"bilder\påse.png").subsample(11, 11)

# Vars
username = StringVar()
rounds_choice = IntVar()


# --------------------------------- Spel Sektion GUI --------------------------------- #
# Spel Labels
label_game_header = Label(root, font='Calibri 14 bold')

label_opponent_choice = Label(root, font="Arial 11 bold")
label_opponent_score = Label(root)
label_opponent_name = Label(root, fg="red", font="Courier 15")

label_user_score = Label(root)
label_user_choice = Label(root, font="Arial 11 bold")
label_username = Label(root, fg="blue", font="Courier 15")

label_outcome_header = Label(root, font="Courier 15", fg ="green")
label_outcome = Label(root, font="Arial 11 bold")
label_rounds_played = Label(root)

label_best_of_rounds = Label(root)

label_line = Label(root)

btn_rock = Button(root, command = lambda: [outcome_handler("sten")])
btn_scissor = Button(root, command = lambda: [outcome_handler("sax")])
btn_paper = Button(root, command = lambda: [outcome_handler("påse")])

# Skapar en lista med alla spel sektions labels för att senare kunna toggla på och av deras grid.
game_labels = [label_opponent_choice, label_opponent_score, label_user_choice, label_user_score, label_line, label_game_header,
               btn_paper, btn_scissor, btn_rock, label_outcome_header, label_outcome, label_username, label_opponent_name, label_best_of_rounds,
               label_rounds_played]
# --------------------------------- Spel Sektion GUI Slut --------------------------------- #


# --------------------------------- Game Over sektion GUI --------------------------------- #
# Label som visar vem som vann
label_game_over_score = Label(root, font="Courier 18 bold")
label_winner_name = Label(root, font="Courier 18 bold")

# Två knapp-alternativ om man vill spela mot en ny motståndare eller tillbaka till menyn.
btn_main_menu = Button(root, command = lambda:[remove_game_labels(), show_menu(), remove_game_over_labels()])
btn_new_opponent = Button(root, command = lambda: [start_game(username.get()), remove_game_over_labels()])

# En lista med alla game over widgets.
game_over_labels = [label_game_over_score, label_winner_name, btn_main_menu, btn_new_opponent]
# --------------------------------- Game Over sektion GUI Slut --------------------------------- #


# --------------------------------- Meny och inställningar GUI Sektion --------------------------------- #
# Meny Labels
label_header = Label(root, text = f'Välkommen till Sten Sax Påse', bg = "orange", font='Helvetica 18 bold', relief = "solid", borderwidth = 2)
label_header.grid(row=0, columnspan=6, pady=20, padx=55, ipadx = 5, ipady = 5)
label_name = Label(root, text='Skriv in spelarnamn:', font='Helvetica 11 bold')
label_name.grid(row=1, columnspan=6)
label_rounds_choice = Label(root, text='Välj antalet rundor som ska spelas', font="Arial 11 bold")
label_rounds_choice.grid(row=3, columnspan=6, pady=(40, 10))

# Radio knappar
r_btn_bo3 = Radiobutton(root, text=f'Bäst av 3', variable=rounds_choice, value=3)
r_btn_bo3.grid(row=4, column=0)
r_btn_bo5 = Radiobutton(root, text=f'Bäst av 5', variable=rounds_choice, value=5)
r_btn_bo5.grid(row=4, column=2, columnspan=2)
r_btn_bo7 = Radiobutton(root, text=f'Bäst av 7', variable=rounds_choice, value=7)
r_btn_bo7.grid(row=4, column=5)

# Meny Entrys
entry_name = Entry(root, textvariable=username)
entry_name.grid(row=2, columnspan=6)

# Meny Knappar
btn_play = Button(root, bg="lightgreen", text=f'Starta Spelet', command = lambda:[start_game(username.get())])
btn_play.grid(row=5, columnspan=6, pady=20)

# Skapar en lista med alla meny labels för att senare kunna toggla på och av deras grid.
menu_labels = [btn_play, entry_name, r_btn_bo5, r_btn_bo3, r_btn_bo7, label_rounds_choice, label_header, label_name]
# --------------------------------- Meny Sektion GUI Slut --------------------------------- #

root.mainloop()
# ---------------------------------- GUI SLUTAR HÄR ----------------------------------- #
