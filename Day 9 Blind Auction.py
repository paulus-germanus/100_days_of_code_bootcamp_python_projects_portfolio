import os

print("Welcome to the secret auction program.")

bids = {}

game_on = True
while game_on:
    name = input("What is your name?: ")
    bid = input("What's your bid in $?: ")

    bids[name] = float(bid)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls')

    if more_bidders == "no":
        game_on = False

        highest_bid = round(max([bids[x] for x in bids]), 2)
print(f"{list(bids.keys())[list(bids.values()).index(highest_bid)]} has won the auction with a bid of {highest_bid}$! Congratulations!")
input("")