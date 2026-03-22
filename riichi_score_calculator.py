"""
Username: img404
Version: 0.4.0
Purpose: Text-based python app for determining riichi mahjong score payments based on user input.
"""


import math


yes_no = ["y", "n"]
yakuman_types = ["counted yakuman", "single yakuman", "double yakuman"]
valid_han_amounts = range(1,60)
valid_fu_amounts = ["20", "25", "30", "40", "50", "60", "70", "80", "90", "100", "120", "130", "140"]
valid_honba_amounts = range(0,20)
SEPARATOR = "-" * 140


def introduction():
    print(SEPARATOR)
    print(SEPARATOR)
    print("Riichi Mahjong Score Calculator")
    print("Answer the following questions to score your winning hand.")
    print(SEPARATOR)
    print(SEPARATOR)


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
    while True:
        honba = input("How many honba were on the table? Enter a numeral: ")
        if int(honba) in valid_honba_amounts:
            honba = int(honba)
            break
        print(f"Honba value cannot be '{honba}'. Please try again.")
    return dealer, tsumo, han, fu, honba


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


def payment_calc(basic_points, dealer, tsumo, honba):
    if dealer:
        if tsumo:
            payment = str(round_up_100(2 * basic_points) + 100 * honba) + " from each player."
        else:
            payment = str(
                round_up_100(6 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."
    else:
        if tsumo:
            payment = str(round_up_100(basic_points) + 100 * honba) + " from each non-dealer player and " + str(
                round_up_100(2 * basic_points) + 100 * honba) + " from the dealer."
        else:
            payment = str(
                round_up_100(4 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."
    return payment

introduction()
dealer, tsumo, han, fu, honba = hand_characteristics()
hand_type, basic_points = type_and_points(han,fu)
payment = payment_calc(basic_points, dealer, tsumo, honba)
print(f"Payment: {payment}")