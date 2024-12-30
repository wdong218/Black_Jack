import pygame
from button import Button # Button 클래스를 가져옴
from Deck import Deck
from Card import Card
from player import player
from dealer import dealer
from GameManager import GameManager
class GameScreen:
    def __init__(self, screen,font):
        # 초기화
        self.screen = screen
        self.font = font  # 메인에서 전달받은 폰트 사용
        self.background_image = pygame.image.load("background_image/1_image.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))  # 크기 조정

        self.deck = None  # 초기에는 None
        self.card = None
        self.stand_push = False
        self.player = None  # 초기값 설정
        self.dealer = None  # 초기값 설정
        self.player_cards = []  # 플레이어 카드 초기화
        self.dealer_cards = []
        self.player_score = 0
        self.game_started = False # 게임 시작 여부를 나타내는 속성 초기화
        self.show_text = False
        # 버튼 생성
        self.buttons = [
            Button(490, 640, 100, 40, "Start", "#6C91C2", "#9AB9E8", "#FFFFFF", self.start_game),  # 파란색 버튼
            Button(610, 640, 100, 40, "Hit", "#8EC6A6", "#B4DEC5", "#FFFFFF", self.hit),  # 초록색 버튼
            Button(730, 640, 100, 40, "Stand", "#E9A869", "#F4C089", "#FFFFFF", self.stand),  # 주황색 버튼
        ]

        self.card_image_map = {
            "AS": "card_image/AS.png", "2S": "card_image/2S.png", "3S": "card_image/3S.png", "4S": "card_image/4S.png",
            "5S": "card_image/5S.png", "6S": "card_image/6S.png", "7S": "card_image/7S.png", "8S": "card_image/8S.png",
            "9S": "card_image/9S.png", "10S": "card_image/10S.png", "JS": "card_image/JS.png",
            "QS": "card_image/QS.png", "KS": "card_image/KS.png",

            "AH": "card_image/AH.png", "2H": "card_image/2H.png", "3H": "card_image/3H.png", "4H": "card_image/4H.png",
            "5H": "card_image/5H.png", "6H": "card_image/6H.png", "7H": "card_image/7H.png", "8H": "card_image/8H.png",
            "9H": "card_image/9H.png", "10H": "card_image/10H.png", "JH": "card_image/JH.png",
            "QH": "card_image/QH.png", "KH": "card_image/KH.png",

            "AD": "card_image/AD.png", "2D": "card_image/2D.png", "3D": "card_image/3D.png", "4D": "card_image/4D.png",
            "5D": "card_image/5D.png", "6D": "card_image/6D.png", "7D": "card_image/7D.png", "8D": "card_image/8D.png",
            "9D": "card_image/9D.png", "10D": "card_image/10D.png", "JD": "card_image/JD.png",
            "QD": "card_image/QD.png", "KD": "card_image/KD.png",

            "AC": "card_image/AC.png", "2C": "card_image/2C.png", "3C": "card_image/3C.png", "4C": "card_image/4C.png",
            "5C": "card_image/5C.png", "6C": "card_image/6C.png", "7C": "card_image/7C.png", "8C": "card_image/8C.png",
            "9C": "card_image/9C.png", "10C": "card_image/10C.png", "JC": "card_image/JC.png",
            "QC": "card_image/QC.png", "KC": "card_image/KC.png"
        }

        # 플레이어 상태 초기화
        self.player_assets = 1000
        self.bet_amount = 50


    # 버튼 동작
    def start_game(self):
        self.show_message("카드를 섞는 중입니다!", (255, 255, 255),duration= 1000)  # 결과 메시지
        self.deck = Deck()  # Deck 객체 생성
        self.deck.create_Deck()
        self.deck.shuffle()
        self.card = Card(self.deck)
        self.player = player()  # 플레이어 초기화
        self.dealer = dealer()  # 딜러 초기화
        self.player_cards = self.player.get_player_card()  # 플레이어 카드 초기화
        self.dealer_cards = self.dealer.get_dealer_card()  # 딜러 카드 초기화
        self.player_score = self.player.get_player_score()
        self.stand_push = False
        self.game_started = True  # 게임 시작 상태로 설정
        self.draw()  # 화면 업데이트

    def show_message(self, message, color, duration=2000):
        """메시지를 화면에 일정 시간 동안 표시"""
        text_surface = self.font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(600, 300))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()  # 화면 업데이트
        # 일정 시간 대기
        pygame.time.wait(duration)

    def hit(self):
        if self.game_started:
            if not self.stand_push:
                # 카드 분배 로직
                player_card = self.card.player_Card_Hit()  # Deck에서 카드 한 장 뽑기
                self.player.add_player_card(player_card)  # 카드 추가 및 점수 업데이트
                print(self.player.player_card)
                print(self.player.player_score)

                # 버스트 체크
                if self.player.get_player_score() > 21:
                    self.show_message("버스트! 딜러가 승리했습니다", (255, 215, 0))  # 결과 메시지
                    self.stand_push = True  # 게임 종료 상태
            else:
                self.show_message("게임이 이미 종료되었습니다. Start 버튼을 누르세요", (255, 0, 0))  # 빨간색 메시지
        else:
            self.show_message("Start 버튼을 누르세요", (255, 0, 0))  # 빨간색 메시지
    def stand(self):
        if self.player.player_score > 21:
            self.show_message("버스트! 딜러가 승리했습니다.", (255, 215, 0))  # 결과 메시지
        else:
            while self.dealer.dealer_score < 17:
                dealer_card = self.card.dealer_Card_Hit()
                self.dealer.add_dealer_card(dealer_card)
            if self.dealer.get_dealer_score() > 21:
                self.show_message("딜러 버스트 ! 당신이 승리했습니다", (0, 0, 255))  # 결과 메시지
                self.stand_push = True
            else:
                self.GameManager = GameManager(self.player, self.dealer)
                self.GameManager.comparison()
                self.show_message("승자는 : " + self.GameManager.get_winner(),(0, 128, 0))
                self.stand_push = True

    # 이벤트 처리
    def handle_event(self, event):
        for button in self.buttons:
            button.check_click(pygame.mouse.get_pos(), event)
        pygame.display.flip()

        # 화면 업데이트
    def update(self):
        pass  # 필요 시 추가

    # 화면 그리기
    def draw(self):
        # 배경 이미지 그리기
        self.screen.blit(self.background_image, (0, 0))  # 화면에 배경 이미지 표시

        # 게임 시작 후 카드 및 정보를 그리기
        if self.game_started:
            self.draw_cards(self.player.get_player_card(), 200, 400)
            self.draw_dealer_cards()
            self.draw_player_info((10, 10))

        # 버튼 그리기
        for button in self.buttons:
            button.is_hovered(pygame.mouse.get_pos())
            button.draw(self.screen, self.font)

        pygame.display.flip()  # 화면 업데이트

    # 카드 그리기
    def draw_cards(self, cards, start_x, y):
        """플레이어의 카드 이미지를 화면에 표시"""
        CARD_WIDTH = 150  # 카드 가로 크기
        CARD_HEIGHT = 170  # 카드 세로 크기
        CARD_GAP = 20  # 카드 간 간격

        for i, card in enumerate(cards):
            # 카드 위치 계산
            x = start_x + i * (CARD_WIDTH + CARD_GAP)

            # 카드 이미지 매칭
            if card in self.card_image_map:
                image_path = self.card_image_map[card]  # 카드 이미지 경로 가져오기
            else:
                image_path = "card_image/default.png"  # 기본 이미지 경로 (없을 경우)

            # 카드 이미지를 로드하고 화면에 표시
            try:
                card_image = pygame.image.load(image_path)  # 이미지 로드
                card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))  # 크기 조정
                self.screen.blit(card_image, (x, y))  # 화면에 이미지 그리기
            except FileNotFoundError:
                print(f"이미지 파일을 찾을 수 없습니다: {image_path}")

    def draw_dealer_cards(self):
        """딜러의 카드를 화면에 표시"""
        CARD_WIDTH = 150  # 카드 가로 크기
        CARD_HEIGHT = 170  # 카드 세로 크기
        CARD_GAP = 20  # 카드 간 간격
        DEALER_START_X = 200  # 딜러 카드 시작 x좌표
        DEALER_Y = 50  # 딜러 카드 y좌표

        dealer_cards = self.dealer.get_dealer_card()  # 딜러 카드 리스트 가져오기

        for i, card in enumerate(dealer_cards):
            x = DEALER_START_X + i * (CARD_WIDTH + CARD_GAP)  # 위치 계산

            if card in self.card_image_map:
                image_path = self.card_image_map[card]  # 카드 이미지 경로 가져오기
            else:
                image_path = "card_image/default.png"  # 기본 이미지 경로

            try:
                card_image = pygame.image.load(image_path)  # 이미지 로드
                card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))  # 크기 조정
                self.screen.blit(card_image, (x, DEALER_Y))  # 화면에 이미지 그리기
            except FileNotFoundError:
                print(f"이미지 파일을 찾을 수 없습니다: {image_path}")

    # 플레이어 정보 그리기
    def draw_player_info(self, position):
        asset_text = f"Assets: ${self.player_assets}"
        score_text = f"Score: {self.player.get_player_score()}"
        bet_text = f"Bet: ${self.bet_amount}"

        x, y = position
        self.screen.blit(self.font.render(asset_text, True, (255, 255, 255)), (x, y))
        self.screen.blit(self.font.render(score_text, True, (255, 255, 255)), (x, y + 30))
        self.screen.blit(self.font.render(bet_text, True, (255, 255, 255)), (x, y + 60))
