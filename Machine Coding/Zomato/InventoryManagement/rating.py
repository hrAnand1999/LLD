from InventoryManagement.ratingInterface import RatingInterface

class Rating(RatingInterface):

    def __init__(self, rate: float):
        self.rate = rate

    def getRating(self):
        return self.rate