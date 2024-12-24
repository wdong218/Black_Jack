import pygame
from pygame.locals import *

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack - Card Layout Example")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# 카드 상태 정의
player_cards = [1, 2, 3]
dealer_cards = [1, 2]

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 화면 초기화
    screen.fill(WHITE)

    # 카드 그리기
    draw_cards(screen, player_cards, 200, PLAYER_Y)  # 플레이어 카드
    draw_cards(screen, dealer_cards, 200, DEALER_Y)  # 딜러 카드

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()