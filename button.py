import pygame
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = pygame.Color(color)  # 기본 색상
        self.hover_color = pygame.Color(hover_color)  # 호버링 색상
        self.text_color = pygame.Color(text_color)  # 텍스트 색상
        self.action = action

    def draw(self, screen, font):
        # 마우스 위치 가져오기
        mouse_pos = pygame.mouse.get_pos()

        # 버튼 색상 변경 (hover 효과)
        current_color = self.hover_color if self.is_hovered(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, (self.x, self.y, self.width, self.height), border_radius=10)

        # 테두리 추가
        border_color = (self.color.r - 20, self.color.g - 20, self.color.b - 20)
        pygame.draw.rect(screen, border_color, (self.x, self.y, self.width, self.height), 2, border_radius=10)

        # 텍스트 렌더링
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        """마우스가 버튼 위에 있는지 확인"""
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def check_click(self, mouse_pos, event):
        """버튼 클릭 이벤트 처리"""
        if self.is_hovered(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            self.action()
