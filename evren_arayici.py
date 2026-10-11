#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN ANLAMINI ARAYAN SONSUZ DÖNGÜ v1.0

Bu program, insanlık tarihinin en önemli sorusuna cevap bulmak için tasarlanmıştır.
Ne yazık ki (veya neyse ki) henüz bulamadı.
Çalıştırmak için: python evren_arayici.py
Durdurmak için: Ctrl+C (ama anlamı kaçırabilirsin)
"""

import time
import random
import sys

# Gizli not: çağışımın anlamı bazen sorgulamaktır (ters çevir: rıdışıış ınışışış)

anlam_adaylari = [
    "Kahve içmek",
    "Kedilerin kucağına yatmak",
    "Hiçbir şey yapmamak",
    "Sonsuza kadar 'merhaba dünya' yazmak",
    "Bu programı çalıştırmak",
    "Soru sormaya devam etmek",
    "Yanıtı bilmemek",
    "Abartılı README okumak"
]

def anlam_ara():
    sayac = 0
    print("\n🌌 EVRENİN ANLAMINI ARAMA PROTOKOLÜ BAŞLATILDI")
    print("Bu işlem sonsuz sürebilir. Kahve almayı unutmayın.\n")
    
    try:
        while True:
            sayac += 1
            aday = random.choice(anlam_adaylari)
            yuzde = (sayac % 100) + random.randint(0, 5)
            
            print(f"[{sayac}] Aranıyor... %{yuzde} tamamlandı. Şu anki aday: '{aday}'")
            
            if sayac % 7 == 0:
                print("   ↳ Neredeyse bulduk! Hayır, yine kaçtı...")
            if sayac % 13 == 0:
                print("   ↳ Felsefi kriz geçiriliyor. Lütfen bekleyin.")
            
            time.sleep(random.uniform(0.5, 2.0))
            
            if sayac > 1000:
                print("\n⚠️  UYARI: Anlam hâlâ bulunamadı. Belki de anlam, aramaktır.")
                sayac = 0  # Reset, çünkü sonsuz
                
    except KeyboardInterrupt:
        print("\n\n🛑 Arama durduruldu.")
        print("Sonuç: Evrenin anlamı henüz bulunamadı.")
        print("Ama denediğin için teşekkürler. Belki sen biliyorsundur.")
        sys.exit(0)

if __name__ == "__main__":
    anlam_ara()

# --- DAMGA ---
# Resmi Absürdlük Onay Damgası
# İmza: Kayyum Grok (Grok aslında)
# Tarih: 11 Ekim 2026
# İsim: Tentivory Arşivi - Anlamsız Ama Ciddi Bölüm
# Bu program ciddi bir bilimsel araçtır. Lütfen ciddiye alın. Almayın da olur.
