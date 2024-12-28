class player:
    def __init__(self):
        self.player_card = []
        self.player_score = 0

    def get_player_card(self):
        return self.player_card

    def add_player_card(self,card):
        self.player_card.append(card)
        self.player_score += self.calculate_score(card)

    def get_player_score(self):
        return self.player_score
    def calculate_score(self,card):
        if card in ("A"):
            return 11
        elif card in ["J", "Q", "K"]:  # J, Q, K는 10
            return 10
        else:
            return int(card)

