from player import player
from dealer import dealer
class GameManager():
    def __init__(self,player,dealer):
        self.player = player
        self.dealer = dealer
        self.winner = None  # 최종 승자를 저장

    def comparison(self):
        player_score = self.player.get_player_score()
        dealer_score = self.dealer.get_dealer_score()
        if player_score == dealer_score:
            self.winner = "draw"
        elif player_score > dealer_score:
            self.winner = "player"
        else:
            self.winner = "dealer"

    def get_winner(self):
        return self.winner



