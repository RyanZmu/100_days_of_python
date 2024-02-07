"""
Silent Auction:
- Ask for name
- Ask for bid
- Ask if there are more bidders
- Repeat

Store the users bids and determine who has the highest bid
"""
bid_list: list = []


# Functions
def add_new_bid(name, bid_amount):
    bid_list.append({"name": name, "bid_amount": bid_amount})
    return bid_list


def highest_bidder(bids):
    high_bid: int = 0
    high_bidder: str = ""

    for index in range(0, len(bids)):
        current_bid: int = bids[index]["bid_amount"]
        current_bidder: str = bids[index]["name"]

        if current_bid > high_bid:
            high_bid = current_bid
            high_bidder = current_bidder

    winner_text: str = f"The highest bidder is {high_bidder}! With a bid of ${high_bid}!"
    return winner_text


def display_inputs():
    # Inputs
    user_name: str = input("What is your name?")
    user_bid: int = int(input("What is your bid?"))

    # Add bid to list
    add_new_bid(name=user_name, bid_amount=user_bid)

    # Ask user to continue
    user_continue: str = input("Are there more bidders?").lower()

    # Continue the bid collecting or end the auction
    if user_continue == "yes":
        continue_auction()
    else:
        winning_bid: str = highest_bidder(bids=bid_list)
        print(winning_bid)


# Display inputs if auction continues
def continue_auction():
    display_inputs()


# Start program
display_inputs()
