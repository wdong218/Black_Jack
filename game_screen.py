import pygame
from button import Button # Button 클래스를 가져옴
from Deck import Deck
from Card import Card
from player import player
from dealer import dealer
class GameScreen:
    def __init__(self, screen):
        # 초기화
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.deck = None  # 초기에는 None
        self.card = None
        # 버튼 생성
        self.buttons = [
            Button(100, 500, 100, 40, "Start", (0, 0, 255), (0, 255, 0), (255, 255, 255), self.start_game),
            Button(250, 500, 100, 40, "Hit", (0, 0, 255), (0, 255, 0), (255, 255, 255), self.hit),
            Button(400, 500, 100, 40, "Stand", (0, 0, 255), (0, 255, 0), (255, 255, 255), self.stand),
        ]

        # 플레이어 상태 초기화
        self.player_assets = 1000
        self.player_score = 15
        self.bet_amount = 50
        self.player_cards = [1, 2, 3]
        self.dealer_cards = [1, 2]

    # 버튼 동작
    def start_game(self):
        print("Game Started!")
        self.deck = Deck()  # Deck 객체 생성
        self.deck.create_Deck()
        self.deck.shuffle()
        self.card = Card(self.deck)
        self.player = player()
        self.dealer = dealer()
        print(self.deck.cards)


    def hit(self):
        print("카드를 분배 중 입니다!")
        player_card = self.card.player_Card_Hit()  # Deck에서 카드 한 장 뽑기
        self.player.add_player_card(player_card)  # 카드 추가 및 점수 업데이트
        dealer_card = self.card.dealer_Card_Hit()
        self.dealer.add_dealer_card(dealer_card)
        print("Player's cards:", self.player.get_player_card())
        print("Player's score:", self.player.get_player_score())

        print("Dealer's cards:", self.dealer.get_dealer_card())
        print("Dealer's score:", self.dealer.get_dealer_score())

    def stand(self):
        print("Stand!")

    # 이벤트 처리
    def handle_event(self, event):
        for button in self.buttons:
            button.check_click(pygame.mouse.get_pos(), event)

    # 화면 업데이트
    def update(self):
        pass  # 필요 시 추가

    # 화면 그리기
    def draw(self):
        # 화면 초기화
        self.screen.fill((255, 255, 255))

        # 카드 그리기
        self.draw_cards(self.player_cards, 200, 400)
        self.draw_cards(self.dealer_cards, 200, 100)

        # 플레이어 정보 그리기
        self.draw_player_info((10, 10))

        # 버튼 그리기
        for button in self.buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(self.screen, self.font)

    # 카드 그리기
    def draw_cards(self, cards, start_x, y):
        CARD_WIDTH = 60
        CARD_HEIGHT = 80
        CARD_GAP = 10

        for i, card in enumerate(cards):
            x = start_x + i * (CARD_WIDTH + CARD_GAP)
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT))

    # 플레이어 정보 그리기
    def draw_player_info(self, position):
        asset_text = f"Assets: ${self.player_assets}"
        score_text = f"Score: {self.player_score}"
        bet_text = f"Bet: ${self.bet_amount}"

        x, y = position
        self.screen.blit(self.font.render(asset_text, True, (0, 0, 0)), (x, y))
        self.screen.blit(self.font.render(score_text, True, (0, 0, 0)), (x, y + 30))
        self.screen.blit(self.font.render(bet_text, True, (0, 0, 0)), (x, y + 60))
