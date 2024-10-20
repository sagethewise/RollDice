import os
import random
import time
from PIL import Image, ImageTk
import tkinter as tk

# Zar tiplerini ve her bir zara ait resim dosyalarını tanımlıyoruz
zar_tipleri = {
    'D4': ['d4_1.png', 'd4_2.png', 'd4_3.png', 'd4_4.png'],
    'D10': ['d10_1.png', 'd10_2.png', 'd10_3.png', 'd10_4.png', 'd10_5.png', 'd10_6.png', 'd10_7.png', 'd10_8.png', 'd10_9.png', 'd10_10.png'],
}

# Zar atma fonksiyonu
def zar_at(zar_tipi):
    max_deger = len(zar_tipleri[zar_tipi])
    return random.randint(1, max_deger)

# Zarların sonucunu animasyonla göstermek için fonksiyon
def zar_goster(zar_tipi, zar_sonucu):
    base_dir = os.path.dirname(__file__)  # Bu adım, scriptin bulunduğu dizini alır
    
    # Animasyon sırasında zarın hızlı bir şekilde dönmesini simüle edelim
    for _ in range(10):
        rastgele_zar = random.randint(1, len(zar_tipleri[zar_tipi]))
        
        # Resmin tam yolunu dinamik olarak oluşturuyoruz
        img_path = os.path.join(base_dir, 'images', zar_tipleri[zar_tipi][rastgele_zar - 1])
        
        # Resmi aç ve göster
        img = ImageTk.PhotoImage(Image.open(img_path))
        zar_label.config(image=img)
        zar_label.image = img
        root.update()
        time.sleep(0.1)
    
    # Sonuçtaki zar resmi için de aynı adımı yapıyoruz
    sonuc_img_path = os.path.join(base_dir, 'images', zar_tipleri[zar_tipi][zar_sonucu - 1])
    sonuc_img = ImageTk.PhotoImage(Image.open(sonuc_img_path))
    zar_label.config(image=sonuc_img)
    zar_label.image = sonuc_img

# Zar atma butonuna basıldığında çalışacak fonksiyon
def zar_at_buton():
    zar_secimi = zar_var.get()
    zar_sayisi = int(zar_sayi_var.get())
    
    for _ in range(zar_sayisi):
        zar_sonucu = zar_at(zar_secimi)
        zar_goster(zar_secimi, zar_sonucu)

# GUI oluşturma
root = tk.Tk()
root.title("Zar Atma Oyunu")

# Zar Tipi Seçim Menüsü
zar_var = tk.StringVar(value='D10')
zar_tipi_menu = tk.OptionMenu(root, zar_var, *zar_tipleri.keys())
zar_tipi_menu.pack()

# Zar Sayısı Girişi
zar_sayi_var = tk.StringVar(value='1')
zar_sayi_entry = tk.Entry(root, textvariable=zar_sayi_var)
zar_sayi_entry.pack()

# Zar Sonucunun Görüleceği Label
zar_label = tk.Label(root)
zar_label.pack()

# Zar At Butonu
zar_at_buton = tk.Button(root, text="Zar At", command=zar_at_buton)
zar_at_buton.pack()

# GUI çalıştırma
root.mainloop()