import random

class Deck:
    def __init__(self):
        self.cards = []
    def create_Deck(self): #카드 뭉치 생성
        print("카드 생성중...")
        suits = ["♣", "♥", "♠", "♦"]  # 클로버, 하트, 스페이드, 다이아몬드
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [rank + suit for suit in suits for rank in ranks]
    def shuffle(self): # 무작위 순서로 카드 섞기
        print("카드 섞는 중...")
        random.shuffle(self.cards)

