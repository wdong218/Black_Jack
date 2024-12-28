from Deck import Deck


class Card:
    def __init__(self,deck):
        self.deck = deck # Deck 인스턴스 생성

    def player_Card_Hit(self):
        if len(self.deck.cards) == 0:
            print("카드가 존재하지 않습니다")
            print(self.deck.cards)
        else:
            return print(self.deck.cards.pop())

    def dealer_Card_Hit(self):
        if len(self.deck.cards) == 0:
            print("카드가 존재하지 않습니다")
        else:
            return self.deck.cards.pop()
    def cards_Left(self): # 카드 갯수 반환
        return len(self.deck.cards)





