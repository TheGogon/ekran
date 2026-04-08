import minimalmodbus
import serial
import time

# USB-RS485 Yapılandırması
try:
    # Port ismini ls /dev/ttyUSB* ile kontrol ettiğinden emin ol
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) 
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 8
    instrument.serial.parity   = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout  = 0.5  # Zaman aşımını biraz artırdık
    instrument.mode = minimalmodbus.MODE_RTU
    
    print("Program başlatıldı. Veriler okunuyor... (Çıkış için Ctrl+C)")
except Exception as e:
    print(f"Başlatma hatası: {e}")
    exit()

while True:
    try:
        # MPR-63 Register Tablosuna göre okuma
        # Eğer hala 0 geliyorsa adresleri 1 artırarak (1, 13, 31) dene
        v1 = instrument.read_float(0, functioncode=3, number_of_registers=2)
        i1 = instrument.read_float(12, functioncode=3, number_of_registers=2)
        p_top = instrument.read_float(30, functioncode=3, number_of_registers=2)

        print(f"\rV1: {v1:6.2f}V | I1: {i1:6.2f}A | P: {p_top:8.2f}W", end="", flush=True)
        
    except KeyboardInterrupt:
        print("\nKullanıcı çıkışı yapıldı.")
        instrument.serial.close()
        break
    except Exception as e:
        # Hata olsa bile döngüden çıkma, 1 saniye bekle ve tekrar dene
        print(f"\rOkuma hatası: {e}                               ", end="", flush=True)
    
    time.sleep(1)
