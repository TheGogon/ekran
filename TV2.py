import os
import sys
import pygame
import time

# Sürücü zaten kmsdrm olarak onaylandı, direkt onu kullanalım
os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
os.environ["SDL_VIDEO_KMSDRM_CRTCID"] = "1"
os.environ["SDL_VIDEO_KMSDRM_CONNECTORID"] = "1"

pygame.init() # SADECE display değil, HER ŞEYİ (font dahil) başlatır
pygame.font.init() # Garantici olalım

# Ekranı oluştur
width, height = 1024, 768
try:
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
except pygame.error:
    # Eğer Fullscreen hata verirse normal modda dene
    screen = pygame.display.set_mode((width, height))

# Font ayarı (None varsayılan fontu kullanır)
font = pygame.font.SysFont(None, 80)

print("KIRMIZI EKRAN GELIYOR...")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

    # Ekranı PARLAK KIRMIZI yap
    screen.fill((255, 0, 0))
    
    yazi = font.render("SISTEM CALISIYOR", True, (255, 255, 255))
    screen.blit(yazi, (width // 6, height // 2))
    
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()
