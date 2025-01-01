import pygame
from core.game_screen import GameScreen
from sound.SoundManage import SoundManage
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Blackjack Game")
# 한글 지원 폰트 설정
font_path = "assets/font/CookieRun Black.ttf"

try:
    global_font = pygame.font.Font(font_path, 30)  # 전역 폰트
except FileNotFoundError:
    print("폰트 파일을 찾을 수 없습니다. 한글 폰트를 설치하거나 경로를 확인하세요.")
    exit()

# GameScreen 인스턴스 생성 시 폰트를 전달
game_screen = GameScreen(screen, global_font)


# GameScreen 초기화
# GameScreen 인스턴스 생성 시 폰트를 전달
game_screen = GameScreen(screen, global_font)
sound_manager = SoundManage()

# 배경음악 재생 (한 번만 실행)
sound_manager.background_sound()
pygame.mixer.music.set_volume(0.1)
# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_screen.handle_event(event)  # 이벤트 처리

    game_screen.draw()  # 매 프레임 화면 업데이트

pygame.quit()
