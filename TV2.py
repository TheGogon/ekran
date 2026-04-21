import pygame
import os
import time

# 1. Sürücü ve Ekran Ayarları
# Sürücüyü kmsdrm olarak zorla, fbi'ın kullandığı altyapıyı kullanmasını sağlar
os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.display.init()
pygame.font.init()

# 2. Ekranı Oluştur
# Çözünürlüğü fbi'ın sevdiği 1024x768 yapalım (VGA için en güvenlisi)
info = pygame.display.Info()
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))

# 3. Font Ayarı (Arial Lite sürümde olmayabilir, None dersen varsayılanı kullanır)
font = pygame.font.SysFont(None, 80)

running = True
clock = pygame.time.Clock()

print("Program basliyor... Cikmak icin terminalde Ctrl+C yapabilirsin.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

    # Ekrani KIRMIZI yapalım (Çalıştığını kesin görelim)
    screen.fill((255, 0, 0)) 

    # Yazıları hazırla
    yazi1 = font.render("SISTEM AKTIF", True, (255, 255, 255)) # Beyaz
    yazi2 = font.render(f"Saat: {time.strftime('%H:%M:%S')}", True, (255, 255, 0)) # Sarı

    # Yazıları ortala
    screen.blit(yazi1, (width // 4, height // 3))
    screen.blit(yazi2, (width // 4, height // 2))

    pygame.display.flip()
    clock.tick(30) # Saniyede 30 kare tazeleme

pygame.quit()
