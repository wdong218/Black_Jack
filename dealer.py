class dealer():
    def __init__(self):

        self.dealer_card = []
        self.dealer_score = 0

    def get_dealer_card(self):
        return self.dealer_card

    def add_dealer_card(self, card):
        self.dealer_card.append(card)
        self.dealer_score += self.calculate_score(card)

    def get_dealer_score(self):
        return self.dealer_score

    def calculate_score(self, card):
        if card in ("A"):
            return 11
        elif card in ["J", "Q", "K"]:  # J, Q, K는 10
            return 10
        else:
            return int(card)