
class Auction:
    def __init__(self, itemName, startingBid):
        self.itemName = itemName
        self.startingBid = startingBid
        self.currentBid = startingBid
        self.bidders = []
        self.highestBidder = None

    def placeBid(self, bidderName, bidAmount):
        if bidAmount > self.currentBid:
            self.currentBid = bidAmount
            self.highestBidder = bidderName
            self.bidders.append((bidderName, bidAmount))
            print(f"New highest bid of {bidAmount} by {bidderName}")
        else:
            print("Bid too low. Try again.")

    def getHighestBidder(self):
        return self.highestBidder, self.currentBid

    def auctionSummary(self):
        print(f"Auction for: {self.itemName}")
        print(f"Starting Bid: {self.startingBid}")
        print(f"Current Highest Bid: {self.currentBid} by {self.highestBidder}")
        print("All Bids:")
        for bidder, bid in self.bidders:
            print(f"{bidder}: {bid}")


auction = Auction("Painting", 100)

auction.placeBid("Ramesh", 120)
auction.placeBid("Suresh", 150)
auction.placeBid("Lakshmi", 170)
auction.placeBid("Padma", 160)
auction.placeBid("Ramya", 200)
auction.placeBid("Rajesh", 180)
auction.placeBid("Ravi", 220)
auction.placeBid("Anitha", 190)
auction.placeBid("Srikanth", 230)
auction.placeBid("Kavitha", 210)
auction.placeBid("Sunitha", 240)
auction.placeBid("Praveen", 250)

auction.auctionSummary()

winner, winningBid = auction.getHighestBidder()
print(f"\nWinner: {winner} with a bid of {winningBid}")


