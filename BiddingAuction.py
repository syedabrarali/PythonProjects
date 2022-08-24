logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from replit import clear
print(logo)
bid_dict = {}
winner = ""
bidding_finished = False  

def bid_func(bidders_input):   #parameter is a dictionary for this function
  highest_bid = 0
  for bidder in bidders_input:
    bid_amount = bidders_input[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"the hishest bidder is {winner} with ${highest_bid}")
  
while not bidding_finished:
  name = str(input("What is your name?\n"))
  bid = int(input("What is your bid amount?\n$"))  
  bid_dict[name] = bid
  more_bidders = str(input("Are there other users that want to bid, type Yes or No\n")).lower()
  if more_bidders == "no":
    bidding_finished = True
    bid_func(bid_dict)
  elif more_bidders == "yes":
    clear()
    


 
  

