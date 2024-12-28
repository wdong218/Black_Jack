import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action
        self.is_hovered = False

    def draw(self, screen, font):
        # 버튼 색상 설정
        if self.is_hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        # 텍스트 그리기
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)

    def check_click(self, pos, event):
        if self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.action()
