import os
from art import logo

print(logo)
print("Welcome to the Secret Auction")

running = True
bids_dict = {}

while running:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids_dict[name] = bid
    keep_running = input("Are there other users who would like to bid?\n")
    if keep_running.lower() == "no":
        running = False
        top_bidder = ""
        top_bid = 0
        for key in bids_dict:
            if bids_dict[key] > top_bid:
                top_bid = bids_dict[key]
                top_bidder = key
        print(f"The highest bid is {top_bid} by {top_bidder}.")
    else:
        os.system('clear')
