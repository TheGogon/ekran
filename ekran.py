import os
import pygame

# Trixie'de Wayland çakışmasını önlemek için KMS/DRM zorla
os.environ["SDL_VIDEODRIVER"] = "kmsdrm"

# EGL kütüphanesinin yerini sisteme tam göster
os.environ["SDL_VIDEO_EGL_DRIVER"] = "/usr/lib/arm-linux-gnueabihf/libEGL.so"

try:
    pygame.display.init()
    # VGA dönüştürücülerin çoğu 1024x768'i sever
    screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
    print("Trixie üzerinde ekran başarıyla başlatıldı!")
except Exception as e:
    print(f"Hata: {e}")
