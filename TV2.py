import pygame
import os
import time

# TÜM SÜRÜCÜ ZORLAMALARINI KALDIRDIK
# Pygame, config.txt'deki ayara göre en uygununu kendisi seçecek.

pygame.display.init()
pygame.font.init()

# Çözünürlüğü VGA için standart yapalım
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont(None, 80)

running = True
clock = pygame.time.Clock()

print("Program basliyor... Ekranda kirmizi gormeyi bekliyoruz.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Test için ekranı KIRMIZI yap
    screen.fill((255, 0, 0))

    yazi1 = font.render("SISTEM AKTIF", True, (255, 255, 255))
    yazi2 = font.render(f"Saat: {time.strftime('%H:%M:%S')}", True, (255, 255, 0))

    screen.blit(yazi1, (width // 6, height // 3))
    screen.blit(yazi2, (width // 6, height // 2))

    pygame.display.flip() 
    clock.tick(20) # Pi Zero için 20 FPS daha az yorucu olur

pygame.quit()
