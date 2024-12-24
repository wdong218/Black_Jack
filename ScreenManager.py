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


def draw_player_info(screen, font, player_assets, player_score, bet_amount, position):
    """
    플레이어 정보를 화면에 출력하는 함수.

    Parameters:
    - screen: Pygame 화면 Surface
    - font: Pygame Font 객체
    - player_assets: 플레이어의 자산 (int)
    - player_score: 플레이어의 점수 (int)
    - bet_amount: 현재 베팅 금액 (int)
    - position: 텍스트 출력 시작 위치 (튜플, 예: (x, y))
    """
    # 텍스트 메시지 생성
    asset_text = f"Assets: ${player_assets}"
    score_text = f"Score: {player_score}"
    bet_text = f"Bet: ${bet_amount}"

    # 텍스트 렌더링
    asset_surface = font.render(asset_text, True, (0, 0, 0))  # 하얀색
    score_surface = font.render(score_text, True, (0, 0, 0))  # 하얀색
    bet_surface = font.render(bet_text, True, (0, 0, 0))  # 하얀색

    # 텍스트 위치 계산 및 화면에 그리기
    x, y = position
    screen.blit(asset_surface, (x, y))
    screen.blit(score_surface, (x, y + 30))  # 다음 텍스트는 아래로 약간 내려서
    screen.blit(bet_surface, (x, y + 60))
# 폰트 설정
font = pygame.font.Font(None, 30)

# 자산, 점수, 베팅 금액 초기화
player_assets = 1000  # 플레이어 자산
player_score = 15     # 플레이어 점수
bet_amount = 50       # 베팅 금액
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

    #플레이어 정보 그리기 점수,자신 및 베팅 금액
    draw_player_info(screen, font, player_assets, player_score, bet_amount, (10, 500))  # 왼쪽 아래에 표시


    # 화면 업데이트
    pygame.display.flip()

pygame.quit()