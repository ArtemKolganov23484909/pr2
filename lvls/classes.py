import pygame
import json

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Заливка экрана черным цветом
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, self.width - 100, self.height - 100), 5) #(50, 50, 450, 1150)
        # Нарисуйте здесь кнопки "Настройки" и "Счёт" в нужных позициях


    def update(self):
        pygame.display.update()

class SettingsButton:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen.screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
        # Нарисуйте здесь текст "Настройки" внутри кнопки

class ScoreButton:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen.screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
        # Нарисуйте здесь текст "Счёт" внутри кнопки

class Rocket:
    def __init__(self, x, y, image_path, screen, speed=1):
        self.x = x
        self.y = y
        self.width = 150
        self.height = 10
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed = speed
        self.direction = 0
        self.screen = screen
        self.border_x = 50
        self.border_width = self.screen.width - 103 - self.width

    def draw(self):
        self.screen.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.direction = -self.speed

    def move_right(self):
        self.direction = self.speed

    def stop(self):
        self.direction = 0

    def update(self):
        self.x += self.direction
        if self.x < self.border_x:
            self.x = self.border_x
        elif self.x > self.border_x + self.border_width:
            self.x = self.border_x + self.border_width



class Square:
    def __init__(self, x, y, k=1, color=(0, 255, 0), border_color='white'):
        self.x = x
        self.y = y
        self.k = k
        self.width = 50
        self.height = 50
        self.color = color
        self.border_color = border_color

    def draw(self, screen):
        pygame.draw.rect(screen.screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen.screen, self.border_color, (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.k), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.screen.blit(text, text_rect)
