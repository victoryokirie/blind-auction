from os import system

from art import logo
print(logo)
print("Welcome to the secret auction program")


# function to find the highest bid
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and (s)he won with a bid of ${highest_bid}")

#empty bidding record
bids={}

bidding_finished=False

#Loop to populate the bidding record and to terminate if there are no more bidders
while not bidding_finished:
    name= input("What is your name?\n")
    price= int(input("What is your bid?  $"))

    bids[name]=price

    should_continue= input("Are there any other bidders? Type 'Yes' or 'No'\n").lower()

    if should_continue == "no":
        bidding_finished=True
        find_highest_bidder(bids) # calls the above function to find the highest bidder from the existing bidding record
    elif should_continue == "yes":
        system('cls') # clear screen for the next bidder to place bid