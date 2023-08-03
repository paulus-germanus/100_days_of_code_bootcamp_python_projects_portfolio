import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand):
    hand.append(random.choice(cards))


def calculate_score(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    elif set([10, 11]).issubset(hand):
        return 0
    else:
        return sum(hand)


players_hand = []
computers_hand = []

deal_card(players_hand)
deal_card(players_hand)

deal_card(computers_hand)
deal_card(computers_hand)

game_on = True

while game_on:

    if calculate_score(players_hand) == 0:
        print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
        print("You've got a Blackjack! You win!")
        game_on = False
    elif calculate_score(computers_hand) == 0:
        print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
        print("Computer's got a Blackjack! You lose!")
        game_on = False
    elif calculate_score(players_hand) > 21:
        print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
        print(f"You're over 21. You lose!")
        game_on = False
    else:
        another_card = input(f"\nYour hand: {players_hand}. Your sum: {sum(players_hand)}.\nComputer's fist card is [{computers_hand[0]}].\nWould you like another card? Y or N?").lower()
        if another_card == "n":
            while sum(computers_hand) < 17:
                deal_card(computers_hand)
            game_on = False
            if calculate_score(computers_hand) > 21:
                print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
                print(f"Computer's over 21. You win!")
                game_on = False
            elif sum(computers_hand) == sum(players_hand):
                print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
                print("It's a draw!")
            elif sum(computers_hand) > sum(players_hand):
                print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
                print("You lose!")
            elif sum(computers_hand) < sum(players_hand):
                print(f"\nYour hand: {players_hand}, your hand's sum: {sum(players_hand)}.\nComputer's hand: {computers_hand}, computer's hand's sum: {sum(computers_hand)}.")
                print("You win!")
        else:
            deal_card(players_hand)
