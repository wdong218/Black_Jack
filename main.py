import pygame
from game_screen import GameScreen

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Blackjack Game")

# GameScreen 초기화
game_screen = GameScreen(screen)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_screen.handle_event(event)  # 이벤트 처리

    game_screen.draw()  # 매 프레임 화면 업데이트

pygame.quit()
