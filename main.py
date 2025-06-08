import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Звуки
bounce_sound = pygame.mixer.Sound("snd_bounce.wav")
lose_sound = pygame.mixer.Sound("snd_lose.wav")

# Размеры экрана
screen_width = 800
screen_height = 600
screen =pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ball Game")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Параметпы объектов
# Размеры мячика и платформы
ball_radius = 10
platform_width = 100
platform_height = 10

# Скорость мячика
ball_speed_x = 5
ball_speed_y = 5

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Game")

# Позиция и скорость платформы
platform_x = (screen_width - platform_width) // 2
platform_y = screen_height - platform_height - 10
platform_speed = 7

# Позиция и скорость мячика
ball_x = screen_width // 2
ball_y = screen_height // 3
ball_dx = ball_speed_x
ball_dy = ball_speed_y

# Шрифт для счёта
font = pygame.font.Font(None, 36)
score = 0

clock = pygame.time.Clock()

running = True
game_started = False
game_over = False
while running:
    screen.fill(BLACK)

    # Обработка собыний
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True

    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x < screen_width - platform_width:
        platform_x += platform_speed

    # Обновление позиции мячика
    if game_started:
        ball_x += ball_dx
        ball_y += ball_dy

    # Проверка столкновения с бортами экрана
    if ball_x <= 0 or ball_x >= screen_width - ball_radius:
        ball_dx *= -1
        bounce_sound.play()
    if ball_y <= 0:
        ball_dy *= -1
        bounce_sound.play()

    # Проверка столкновения с платформой
    if ball_y >= platform_y - ball_radius and platform_x <= ball_x <= platform_x + platform_width:
        ball_dy *= -1
        score += 1
        bounce_sound.play()
    if ball_y > screen_height:
            lose_sound.play()
            game_over = True
        

    

    # Отрисовка мячика
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Отрисовка платформы
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))

    # Отображение счёта
    score_text = font.render(f"Score:{score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Инструкции или надпись Game Over
    font = pygame.font.Font(None, 48)
    if not game_started and not game_over:
        text = font.render("Press SPACE to start", True, WHITE)
        rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, rect)
    elif game_over:
        text = font.render("Game Over", True, RED)
        rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()