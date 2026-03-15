"""
Username: img404
Version: 0.3.0
Purpose: Text-based python app for determining riichi mahjong score payments based on user input.
"""


import math


yes_no = ["y", "n"]
yakuman_types = ["counted yakuman", "single yakuman", "double yakuman"]
valid_han_amounts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
valid_fu_amounts = ["20", "25", "30", "40", "50", "60", "70", "80", "90", "100", "120", "130", "140"]
valid_honba_amounts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]


han = 1
fu = 20
basic_points = 160
honba = 0
hand_type = "normal"


print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("Riichi Mahjong Score Calculator")
print("Answer the following questions to score your winning hand.")


while True:
    print("--------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------")
    while True:
        dealer_response = input("Were you the dealer? y/n: ")
        if dealer_response in yes_no:
            dealer = dealer_response == "y"
            break
        print("Please enter either 'y' or 'n'.")

    while True:
        tsumo_response = input("Did you win by tsumo (self-draw)? y/n: ")
        if tsumo_response in yes_no:
            tsumo = tsumo_response == "y"
            break
        print("Please enter either 'y' or 'n'.")

    while True:
        han = int(input("How many han did the hand score? Enter a numeral: "))
        if str(han) in valid_han_amounts:
            break
        else:
            print(f"Han value cannot be '{han}'. Please try again.")

    # If the han value is less than 5, then we must count fu. Otherwise, fu is given a placeholder value of 0.
    if han < 5:
        while True:
            fu = int(input("How many fu did the hand score? Enter a numeral: "))
            if str(fu) in valid_fu_amounts:
                break
            print(f"Fu value cannot be '{fu}'. Please try again.")
    else:
        fu = 20

    # The basic points of the hand are determined using han and fu values.
    if han >= 13:
        while True:
            hand_type = input("Was the hand a counted yakuman, single yakuman, or double yakuman? (Enter counted/single/double:) ") + ' yakuman'
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

    while True:
        honba = int(input("How many honba were on the table? Enter a numeral: "))
        if str(honba) in valid_honba_amounts:
            break
        print(f"'{honba}' is not a possible honba value. Please try again.")

    # Payments must be in multiples of 100, so let's define a function that rounds values up to the next hundred.
    def round_up_100(x):
        return math.ceil(x / 100) * 100

    # Score payments are calculated based on dealer, tsumo, basic points, and honba.
    if dealer:
        if tsumo:
            payment = str(round_up_100(2 * basic_points) + 100 * honba) + " from each player."
        else:
            payment = str(round_up_100(6 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."
    else:
        if tsumo:
            payment = str(round_up_100(basic_points) + 100 * honba) + " from each non-dealer player and " +  str(round_up_100(2 * basic_points) + 100 * honba) + " from the dealer."
        else:
            payment = str(round_up_100(4 * basic_points) + 300 * honba) + " from the player who discarded your winning tile."

    print("--------------------------------------------------------------------------------------------------------------------")
    if dealer:
        if tsumo:
            print("Dealer tsumo.")
        else:
            print("Dealer ron.")
    else:
        if tsumo:
            print("Non-dealer tsumo.")
        else:
            print("Non-dealer ron.")

    if hand_type == 'normal':
        print(str(han) + " han, " + str(fu) + " fu; " + str(honba) + " honba.")
    else:
        print(hand_type.capitalize() + "; " + str(honba) + " honba.")

    print("Payment: " + payment)
    print("--------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------")

    yes_no = ["y", "n"]
    while True:
        response = input("Score another hand? y/n: ")
        if response in yes_no:
            break
        print("Please enter either 'y' or 'n'.")
    if response == "n":
        break