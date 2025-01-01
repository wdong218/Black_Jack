import pygame


class SoundManage:
    def __init__(self):
        pygame.mixer.init()
        # 사운드 파일 경로 설정
        self.start_button_sound_file = "assets/sounds/start_button.wav"
        self.up_down_sound_file = "assets/sounds/up_down.wav"
        self.background_sound_file = "assets/sounds/background.mp3"
        self.win_sound_file = "assets/sounds/win.wav"
        self.draw_sound_file = "sounds/draw.wav"
        self.fail_sound_file = "assets/sounds/fail.wav"
        self.hit_sound_file = "assets/sounds/hit.wav"
        self.stand_sound_file = "assets/sounds/stand.wav"

        # 사운드 미리 로드
        self.start_button_audio = pygame.mixer.Sound(self.start_button_sound_file)  # 올바른 초기화
        self.up_down_audio = pygame.mixer.Sound(self.up_down_sound_file)
        self.win_audio = pygame.mixer.Sound(self.win_sound_file)
        # self.draw_audio = pygame.mixer.Sound(self.draw_sound_file)
        self.fail_audio = pygame.mixer.Sound(self.fail_sound_file)
        self.hit_audio = pygame.mixer.Sound(self.hit_sound_file)
        self.stand_audio = pygame.mixer.Sound(self.stand_sound_file)
        self.win_audio.set_volume(0.3)

    def play_start_button_sound(self):
        self.start_button_audio.play()  # 초기화된 속성 사용

    def up_down_sound(self):
        self.up_down_audio.play()

    def background_sound(self):
        pygame.mixer.music.load(self.background_sound_file)
        pygame.mixer.music.play(-1)  # 반복 재생

    def win_sound(self):
        self.win_audio.play()

    def draw_sound(self):
        self.draw_audio.play()

    def fail_sound(self):
        self.fail_audio.play()

    def hit_sound(self):
        self.hit_audio.play()

    def stand_sound(self):
        self.stand_audio.play()
