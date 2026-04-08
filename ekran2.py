import pygame
import os
import sys

# Ayarlar
os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ["SDL_VIDEODRIVER"] = "kmsdrm" # HDMI için en kararlısı
kla
pygame.display.init()
pygame.font.init()

# Ekranı aç
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont("Arial", 50)
clock = pygame.time.Clock()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0)) # Siyah ekran
        # Değerleri buraya yazdır (Modbus'tan gelen veriler)
        text = font.render("Sistem Hazir...", True, (255, 255, 255))
        screen.blit(text, (100, 100))
        
        pygame.display.flip()
        clock.tick(10) # Düşük FPS = Mutlu Pi Zero
except KeyboardInterrupt:
    pygame.quit()
