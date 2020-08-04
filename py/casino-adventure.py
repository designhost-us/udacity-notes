import time
import random

npc_name = ["Anlow", "Arando", "Bram", "Cale", "Dalkon", "Daylen", "Dodd",
            "Dungarth", "Dyrk", "Eandro", "Falken", "Feck", "Fenton",
            "Gryphero", "Hagar", "Jeras", "Krynt", "Lavant", "Leyten",
            "Malfier", "Markus", "Meklan", "Namen", "Navaren", "Nerle",
            "Nilus", "Ningyan", "Norris", "Quentin", "Semil", "Sevenson",
            "Steveren", "Talfen", "Tamond", "Taran", "Tegan", "Vanan", "Vina"]

ambiance = ["The cigarette girl walks by smelling like gin and menthol.",
            "A cheer errupts as somebody wins big.",
            "The band is playing a brassy tune with a nice bounce to it.",
            "The stench of smoke and mildew rise from the carpet "
            "with every step you take.",
            "There are no windows and the only light in the room "
            "comes from neon signs."]

win_reaction = [" congratualtes your lucky throw.",
                " flags down the cocktail waitress to top off your drink.",
                " comps your meal ticket for the buffet.",
                " claps and shouts that you're on a hot streak!"]

loss_reaction = [" quietly sweeps your credits off the table.",
                 " gives you a sympathetic nod.",
                 " assures you the next one will be a winner.",
                 " favors you with a smile while he glances at the cashier."]

name = ""
purse = int(0)
wins = int(0)
losses = int(0)
cashier_name = random.choice(npc_name)
dealer_name = random.choice(npc_name)


def pp(text):  # A "print-and-pause" function.
    print(text)
    time.sleep(1/2)


def pn(text):  # Adds a new line above a print-and-pause function.
    pp("")
    pp(text)


def banner():
    print("Adventure")
    print(" ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ ")
    print("██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗")
    print("██║     ███████║███████╗██║██╔██╗ ██║██║   ██║")
    print("██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║")
    print("╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
    print("                             by Mike Battaglia")


def lobby(name, purse, wins, losses, cashier_name, dealer_name):
    pn("You are in the lobby.")
    pp(random.choice(ambiance))
    pn("(1) Play Dice.")
    pp("(2) Visit Cashier.")
    z = input("(3) Retire.\n")
    if z == '1':
        dice_table(name, purse, wins, losses, cashier_name, dealer_name)
    elif z == '2':
        cashier(name, purse, wins, losses, cashier_name, dealer_name)
    elif z == '3':
        retire(name, purse, wins, losses, cashier_name, dealer_name)
    else:
        lobby(name, purse, wins, losses, cashier_name, dealer_name)


def cashier(name, purse, wins, losses, cashier_name, dealer_name):
    pn(f"The cashier, {cashier_name}, smiles from behind a wall of glass.")
    if name == "":  # New user must enter name, returning user sees stats.
        pp("\"I see you're new here. Welcome!\"")
        while name == "":
            pp("\"If you'll enter your name, I can fund your account"
                "with 100 free credits.\"")
            name = input("Name: ")
        purse = 100
        pp(f"\"Very well, {name}. You have 100 credits in your account.\"")
        pp("\"Good luck, and come back here anytime to check your stats.\"")
        lobby(name, purse, wins, losses, cashier_name, dealer_name)
    else:
        pn("\"I hope you're having fun!\"")
        stats_out(name, purse, wins, losses, cashier_name, dealer_name)
        lobby(name, purse, wins, losses, cashier_name, dealer_name)


def dice_table(name, purse, wins, losses, cashier_name, dealer_name):
    pn("You approach the dice table.")
    if purse < int(1):  # Give instruction to user with empty purse.
        pp("You'll need to get some credits from the cashier "
           "before you can play.")
        lobby(name, purse, wins, losses, cashier_name, dealer_name)
    else:
        pp(f"You are greeted by the dealer, {dealer_name}.")
        pp(f"\"Welcome, {name}!\"")
        wager(name, purse, wins, losses, cashier_name, dealer_name)


def wager(name, purse, wins, losses, cashier_name, dealer_name):
    while True:
        pn(f"You have {purse} credits in your purse.")
        waged = input("How many credits do you wager? ")
        try:  # Validate wager is a positive intiger.
            val = int(waged)
            if val < 1:
                print("You can't wager less than 1 credit.")
                continue
            break
        except ValueError:
            print("Quit messing around! "
                  "Enter the number of credits you'd like to wager.")
    pp(f"{dealer_name} matches your {waged} credits.")
    while True:
        pp("\"Low, or high?\" the dealer asks.")
        pp("(1) Low.")
        bet = input("(2) High.\n")
        if bet == '1':
            pp(f"\"Low roller!\" {dealer_name} shouts and rolls the dice.")
            break
        elif bet == '2':
            pp(f"\"High roller!\" {dealer_name} shouts and rolls the dice.")
            break
    roll(name, purse, wins, losses, cashier_name, dealer_name, waged, bet)


def roll(name, purse, wins, losses, cashier_name, dealer_name, waged, bet):
    r = random.randint(1, 7)
    pn(f"The die tumbled across the tabled and landed on {r}...")
    if r >= 4:
        pp("a high number!")
        if bet == '1':
            lose(name, purse, wins, losses, cashier_name, dealer_name, waged)
        else:
            win(name, purse, wins, losses, cashier_name, dealer_name, waged)
    else:
        pp("a low number!")
        if bet == '2':
            lose(name, purse, wins, losses, cashier_name, dealer_name, waged)
        else:
            win(name, purse, wins, losses, cashier_name, dealer_name, waged)


def win(name, purse, wins, losses, cashier_name, dealer_name, waged):
    pp(f"Well done! You won {waged} credits.")
    print(f"{dealer_name}", random.choice(win_reaction), sep="")
    purse += int(waged)
    wins += 1
    play_again(name, purse, wins, losses, cashier_name, dealer_name)


def lose(name, purse, wins, losses, cashier_name, dealer_name, waged):
    pp(f"Oh no! You lost {waged} credits.")
    print(f"{dealer_name}", random.choice(loss_reaction), sep="")
    purse -= int(waged)
    losses += 1
    if purse == 0:
        pp("You're broke!")
        retire(name, purse, wins, losses, cashier_name, dealer_name)
    else:
        play_again(name, purse, wins, losses, cashier_name, dealer_name)


def play_again(name, purse, wins, losses, cashier_name, dealer_name):
    if purse > 0:
        pn("Play again?")
        print("(1) Yes.")
        again = input("(2) No.\n")
        if again == '1':
            wager(name, purse, wins, losses, cashier_name, dealer_name)
        elif again == '2':
            lobby(name, purse, wins, losses, cashier_name, dealer_name)
        else:
            play_again(name, purse, wins, losses, cashier_name, dealer_name)


def stats_out(name, purse, wins, losses, cashier_name, dealer_name):
    pn(f"Statistics: {name}")
    print(f"You have {purse} credits.")
    print(f"You have {wins} wins and {losses} losses.")


def retire(name, purse, wins, losses, cashier_name, dealer_name):
    pn("Are you sure you'd like to quit?")
    pp("(1) Quit.")
    quit = input("(2) Cancel.\n")
    if quit == '1':
        pn("You gotta know when to hold 'em,")
        pp("know when to fold 'em")
        pp("Know when to walk away")
        pp("And know when to run!")
        stats_out(name, purse, wins, losses, cashier_name, dealer_name)
    else:
        lobby(name, purse, wins, losses, cashier_name, dealer_name)


banner()
lobby(name, purse, wins, losses, cashier_name, dealer_name)
