import pygame
import time
import os

os.environ["SDL_VIDEODRIVER"] = 'kmsdrm'

# Pygame Başlat
pygame.init()

# TV ekranını tam ekran aç
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont("Arial", 100) # Dev yazı boyutu
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Bir tuşa basarsan çıkar
            running = False

    # Buraya Modbus okuma kodunu ekleyeceksin
    gerilim = "220V" # Örnektir, instrument.read_register ile değiştir
    guc = "1500W"

    screen.fill((0, 0, 0)) # Ekranı temizle (Siyah)

    # Yazıları ekrana yerleştir
    yazi1 = font.render(f"Gerilim: {gerilim}", True, (0, 255, 0)) # Yeşil
    yazi2 = font.render(f"Guc: {guc}", True, (255, 255, 0))      # Sarı

    screen.blit(yazi1, (100, 100))
    screen.blit(yazi2, (100, 300))

    clock.tick(20)

    pygame.display.flip()
    time.sleep(1)

pygame.quit()
