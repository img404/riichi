"""
Username: img404
Version: 0.4.1
Purpose: Text-based python app for determining riichi mahjong score payments based on user input.
"""


import math


# Defines valid sets and ranges for user input validation, as well as a constant later used for visual separation.
yes_no = ["y", "n"]
yakuman_types = ["counted yakuman", "single yakuman", "double yakuman"]
valid_han_amounts = range(1,60)
valid_fu_amounts = ["20", "25", "30", "40", "50", "60", "70", "80", "90", "100", "120", "130", "140"]
valid_honba_amounts = range(0,20)
SEPARATOR = "-" * 140


# Function that introduces the program to the user.
def introduction():
    print(SEPARATOR)
    print(SEPARATOR)
    print("Riichi Mahjong Score Calculator")
    print("Answer the following questions to score your winning hand.")
    print(SEPARATOR)
    print(SEPARATOR)


# Function that requests and validates user input, storing them to new variables for use later.
def hand_characteristics():
    while True:
        dealer_response = input("Were you the dealer? y/n: ").lower().strip()
        if dealer_response in yes_no:
            dealer = dealer_response == "y"
            break
        print("Please enter either 'y' or 'n'.")
    while True:
        tsumo_response = input("Did you win by tsumo (self-draw)? y/n: ").lower().strip()
        if tsumo_response in yes_no:
            tsumo = tsumo_response == "y"
            break
        print("Please enter either 'y' or 'n'.")
    while True:
        honba = input("How many honba were on the table? Enter a numeral: ")
        if int(honba) in valid_honba_amounts:
            honba = int(honba)
            break
        print(f"Honba value cannot be '{honba}'. Please try again.")
    while True:
        han = input("How many han did the hand score? Enter a numeral: ")
        if int(han) in valid_han_amounts:
            han = int(han)
            break
        else:
            print(f"Han value cannot be '{han}'. Please try again.")

    # If the han value is less than 5, then we must count fu. Otherwise, fu is given a placeholder value of 0.
    if han < 5:
        while True:
            fu = input("How many fu did the hand score? Enter a numeral: ")
            if fu in valid_fu_amounts:
                fu = int(fu)
                break
            print(f"Fu value cannot be '{fu}'. Please try again.")
    else:
        fu = 20
    return dealer, tsumo, honba, han, fu


# Function that uses han and fu to determine hand type and basic points, stored to new variables. Also includes yakuman validation.
def type_and_points(han, fu):
    if han >= 13:
        while True:
            yakuman_response = input("Was the yakuman counted, single, or double?) ").lower().strip()
            hand_type = yakuman_response + ' yakuman'
            if hand_type in yakuman_types:
                break
            print(f"'{hand_type}' isn't a valid input. Please enter counted, single, or double.")
        if hand_type == "double yakuman":
            basic_points = 16000
        elif hand_type in ["single yakuman", "counted yakuman"]:
            basic_points = 8000
    elif han >= 11:
        hand_type = "sanbaiman"
        basic_points = 6000
    elif han >= 8:
        hand_type = "baiman"
        basic_points = 4000
    elif han >= 6:
        hand_type = "haneman"
        basic_points = 3000
    elif han >= 5 or (han == 4 and fu >= 30) or (han == 3 and fu >= 60):
        hand_type = "mangan"
        basic_points = 2000
    else:
        hand_type = "normal"
        basic_points = fu * 2 ** (2 + han)
    return hand_type, basic_points


# Payments must be made in multiples of 100, and raw values are rounded up if they aren't already a multiple of 100.
def round_up_100(x):
    return math.ceil(x / 100) * 100


# Function that uses previously defined variables to calculate the win type and payments, stored to new variables.
def payment_calc(basic_points, dealer, tsumo, honba):
    if dealer:
        if tsumo:
            win_type = "Dealer tsumo. "
            payment = str(round_up_100(2 * basic_points) + 100 * honba) + " from each player."
        else:
            win_type = "Dealer ron. "
            payment = str(
                round_up_100(6 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."
    else:
        if tsumo:
            win_type = "Non-dealer tsumo. "
            payment = str(round_up_100(basic_points) + 100 * honba) + " from each non-dealer player and " + str(
                round_up_100(2 * basic_points) + 100 * honba) + " from the dealer."
        else:
            win_type = "Non-dealer ron. "
            payment = str(
                round_up_100(4 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."
    return win_type, payment


# Function that prints hand information & payment details back to the user.
def results(SEPARATOR, win_type, han, fu, honba, hand_type, payment):
    print(SEPARATOR)
    print(win_type)
    if hand_type == 'normal':
        print(f"{han} han, {fu} fu; {honba} honba.")
    else:
        print(f"{hand_type.capitalize()}, {honba} honba.")
    print(f"Payment: {payment}")
    print(SEPARATOR)


# This is what runs when the user opens the program.
introduction()
while True:
    dealer, tsumo, honba, han, fu = hand_characteristics()
    hand_type, basic_points = type_and_points(han,fu)
    win_type, payment = payment_calc(basic_points, dealer, tsumo, honba)
    results(SEPARATOR, win_type, han, fu, honba, hand_type, payment)
    response = input("Score another hand? y/n: ")
    if response not in yes_no:
        print("Please enter either 'y' or 'n'.")
        break
    elif response == "n":
        break
    print(SEPARATOR)
