"""
Username: img404
Date: 3/12/26
Purpose: Text-based python app for determining riichi mahjong score payments based on user input. 
"""


import math


# Introduce the program to the user.
print("----------------------------------------------------------")
print("Riichi Mahjong Score Calculator")
print("Answer the following questions to score your winning hand.")
print("----------------------------------------------------------")


# Ask the user if they were the dealer and if they won by self-draw and convert the inputs to a bool.
dealer = input("Were you the dealer? y/n: ") in ["y", "yes", "yeah"]
tsumo = input("Did you win by tsumo (self-draw)? y/n: ") in ["y", "yes", "yeah"]


# Ask the user to input han value, and convert the input to an integer.
han = int(input("How many han did the hand score? Enter a numeral: "))


# If the han value is less than 5, ask for fu, and convert the input to an integer.
if han < 5:
    fu = int(input("How many fu did the hand score? Enter a numeral: "))


# Ask the user how many repeats there were, and convert the input to an integer.
honba = int(input("How many honba were on the table? Enter a numeral: "))


# Using han and fu values, determine the hand type and basic points.
if han >= 13:
    hand_type = input("Was the hand a counted yakuman, single yakuman, or double yakuman? (Enter counted/single/double:) ") + ' yakuman'
    if hand_type == 'double yakuman':
        basic_points = 16000
    elif hand_type in ['single yakuman', 'counted yakuman']:
        basic_points = 8000
elif han >= 11:
    hand_type = 'sanbaiman'
    basic_points = 6000
elif han >= 8:
    hand_type = 'baiman'
    basic_points = 4000
elif han >= 6:
    hand_type = 'haneman'
    basic_points = 3000
elif han >= 5 or (han == 4 and fu >= 30) or (han == 3 and fu >= 60):
    hand_type = 'mangan'
    basic_points = 2000
else:
    hand_type = 'normal'
    basic_points = fu * 2 ** (2 + han)


# Payments must be in multiples of 100, so let's define a function that rounds values up to the next hundred.
def round(x):
    return math.ceil(x / 100) * 100


# Determine score payments based on dealer, tsumo, basic points, and honba.
if dealer:
    if tsumo:
        payment = str(round(2 * basic_points) + 100 * honba) + ' from each player.'
    else:
        payment = str(round(6 * basic_points) + 300 * honba) + ' from the player who discarded your winning tile.'
else:
    if tsumo:
        payment = str(round(basic_points) + 100 * honba) + ' from each non-dealer player and ' +  str(round(2 * basic_points) + 100 * honba) + ' from the dealer.'
    else:
        payment = str(round(4 * basic_points) + 300 * honba) + ' from the player who discarded your winning tile.'


# Print the hand conditions & payment owed.
print("-------------------------------------------------")
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
print("-------------------------------------------------")