import pygame
from game_screen import GameScreen  # GameScreen 클래스를 가져옴

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack - Card Layout Example")

# GameScreen 초기화
game_screen = GameScreen(screen)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 이벤트 처리
        game_screen.handle_event(event)

    # 화면 업데이트 및 그리기
    game_screen.update()
    game_screen.draw()

    pygame.display.flip()

pygame.quit()
