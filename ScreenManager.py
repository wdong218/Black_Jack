import pygame
from pygame.locals import *

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack - Card Layout Example")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 카드 크기 및 위치 설정
CARD_WIDTH = 60
CARD_HEIGHT = 80
CARD_GAP = 10  # 카드 간 간격
PLAYER_Y = 400
DEALER_Y = 100

# 카드 위치 계산 함수
def draw_cards(screen, cards, start_x, y, color=BLACK):
    for i, card in enumerate(cards):
        x = start_x + i * (CARD_WIDTH + CARD_GAP)
        pygame.draw.rect(screen, color, (x, y, CARD_WIDTH, CARD_HEIGHT))

# 플레이어 정보 출력 함수
def draw_player_info(screen, font, player_assets, player_score, bet_amount, position):
    asset_text = f"Assets: ${player_assets}"
    score_text = f"Score: {player_score}"
    bet_text = f"Bet: ${bet_amount}"

    x, y = position
    screen.blit(font.render(asset_text, True, BLACK), (x, y))
    screen.blit(font.render(score_text, True, BLACK), (x, y + 30))
    screen.blit(font.render(bet_text, True, BLACK), (x, y + 60))

# 버튼 클래스
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action):
        # 버튼의 위치와 크기 정의
        self.rect = pygame.Rect(x, y, width, height)  # 버튼 영역을 정의하는 pygame Rect 객체
        # 버튼 텍스트와 색상
        self.text = text  # 버튼에 표시할 텍스트
        self.color = color  # 기본 버튼 색상
        self.hover_color = hover_color  # 마우스가 버튼 위에 있을 때 색상
        self.text_color = text_color  # 텍스트 색상
        # 버튼 동작
        self.action = action  # 버튼이 클릭되었을 때 실행할 함수
        # 상태
        self.is_hovered = False  # 마우스가 버튼 위에 있는지 여부를 추적

    def draw(self, screen, font):
        # 버튼 색상을 설정하고 버튼 그리기
        if self.is_hovered:  # 마우스가 버튼 위에 있을 경우
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:  # 마우스가 버튼 위에 없을 경우
            pygame.draw.rect(screen, self.color, self.rect)
        # 텍스트 렌더링
        text_surface = font.render(self.text, True, self.text_color)  # 텍스트를 렌더링
        text_rect = text_surface.get_rect(center=self.rect.center)  # 텍스트를 버튼 중앙에 배치
        screen.blit(text_surface, text_rect)  # 화면에 텍스트 그리기

    def check_hover(self, pos):
        # 마우스가 버튼 위에 있는지 확인
        self.is_hovered = self.rect.collidepoint(pos)  # 마우스 위치가 버튼 영역에 있는지 확인

    def check_click(self, pos, event):
        # 버튼이 클릭되었는지 확인하고 실행
        if self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.action()  # 클릭되었으면 연결된 함수 실행


# 버튼 클릭 시 실행할 함수들
def start_game():
    print("Game Started!")

def hit():
    print("Hit!")

def stand():
    print("Stand!")

# 버튼 생성
font = pygame.font.Font(None, 30)
buttons = [
    Button(100, 500, 100, 40, "Start", BLUE, GREEN, WHITE, start_game),
    Button(250, 500, 100, 40, "Hit", BLUE, GREEN, WHITE, hit),
    Button(400, 500, 100, 40, "Stand", BLUE, GREEN, WHITE, stand),
]

# 플레이어 상태 초기화
player_assets = 1000
player_score = 15
bet_amount = 50
player_cards = [1, 2, 3]
dealer_cards = [1, 2]

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # 버튼 클릭 처리
        for button in buttons:
            button.check_click(pygame.mouse.get_pos(), event)

    # 화면 초기화
    screen.fill(WHITE)

    # 카드 그리기
    draw_cards(screen, player_cards, 200, PLAYER_Y)
    draw_cards(screen, dealer_cards, 200, DEALER_Y)

    # 플레이어 정보 그리기
    draw_player_info(screen, font, player_assets, player_score, bet_amount, (10, 10))

    # 버튼 상태 업데이트 및 그리기
    for button in buttons:
        button.check_hover(pygame.mouse.get_pos())
        button.draw(screen, font)

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
