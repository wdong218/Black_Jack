class GameManager():
    def __init__(self,player,dealer):
        self.player = player
        self.dealer = dealer
        self.winner = None  # 최종 승자를 저장
        self.winner_TF = 0

    def comparison(self):
        player_score = self.player.get_player_score()
        dealer_score = self.dealer.get_dealer_score()
        if player_score == dealer_score:
            self.winner_TF = 2
            self.winner = "비겼습니다!"
        elif player_score > dealer_score:
            self.winner_TF = 1
            self.winner = "당신입니다!"
        else:
            self.winner = "딜러입니다!"

    def get_winner(self):
        return self.winner
    def get_winnerTF(self):
        return self.winner_TF



