import os
import sys
import pygame
import time

# 1. Önce her şeyi temizleyelim
os.environ.pop("SDL_VIDEODRIVER", None)

# 2. Pi Zero W / Lite için en garantili sürücü sıralaması
drivers = ['kmsdrm', 'fbcon', 'directfb']

found_driver = False
for driver in drivers:
    try:
        os.environ["SDL_VIDEODRIVER"] = driver
        pygame.display.init()
        print(f"Basarili surucu: {driver}")
        found_driver = True
        break
    except pygame.error:
        continue

if not found_driver:
    print("Hicbir video surucusu calismadi!")
    sys.exit()

# 3. Ekranı oluştur (VGA dostu 1024x768)
screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 80)

# 4. Döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

    # PARLAK MAVİ yapalım (Siyah ve Kırmızıdan farklı olsun, çalıştığını anlayalım)
    screen.fill((0, 0, 255)) 
    
    yazi = font.render("EKRAN CALISIYOR!", True, (255, 255, 255))
    screen.blit(yazi, (200, 300))
    
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()
