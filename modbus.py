import minimalmodbus
import serial
import time

# USB-RS485 Yapılandırması
try:
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.baudrate = 9600
    instrument.serial.timeout = 0.2
    print("Program başlatıldı. Çıkmak için 'Ctrl+C' tuşuna basın.")
except Exception as e:
    print(f"Bağlantı hatası: {e}")
    exit()

try:
    while True:
        # MPR-63 Register Tablosuna göre adresler
        # read_float(register_adresi, functioncode, number_of_registers)
        v1 = instrument.read_float(0, 3, 2)  # L1 Gerilimi
        i1 = instrument.read_float(12, 3, 2) # L1 Akımı
        p_top = instrument.read_float(30, 3, 2) # Toplam Aktif Güç

        print(f"\rV1: {v1:6.2f}V | I1: {i1:6.2f}A | P: {p_top:8.2f}W", end="")
        
        time.sleep(1) # 1 saniye bekle (Cihazı yormamak için)

except KeyboardInterrupt:
    print("\n\nKullanıcı isteğiyle çıkış yapılıyor...")
    instrument.serial.close()
    print("Haberleşme kapatıldı. Hoşça kal!")
