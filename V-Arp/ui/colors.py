#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Steam Tarzı Renk Teması ve Stil Sabitleri
Bu modül, Steam benzeri UI için kullanılan renk ve stil sabitlerini içerir.
"""

# Steam benzeri renk şeması
THEME = {
    # Ana renkler
    "background": "#171a21",         # Steam koyu lacivert arka plan
    "card_background": "#1b2838",    # Steam panel arkaplanı
    "sidebar_background": "#1f3141", # Steam sidebar arkaplanı
    
    # Vurgu renkleri
    "primary": "#66c0f4",            # Steam mavi vurgu
    "secondary": "#2a475e",          # Steam koyu mavi
    "tertiary": "#c7d5e0",           # Steam açık gri
    
    # Durum renkleri
    "success": "#5ba32b",            # Yeşil (başarı)
    "warning": "#e5ac00",            # Sarı (uyarı)
    "error": "#d94126",              # Kırmızı (hata)
    "info": "#417a9b",               # Mavi (bilgi)
    
    # Metin renkleri
    "text_primary": "#ffffff",       # Beyaz
    "text_secondary": "#a3c2d7",     # Açık mavi
    "text_tertiary": "#66c0f4",      # Steam mavi
    "text_disabled": "#4b5d67",      # Pasif metin
    
    # Etkileşim durumları
    "hover_primary": "#a4d8ff",      # Mavi hover durumu
    "active_primary": "#1f78b4",     # Koyu mavi aktif durumu
    "hover_secondary": "#3c5977",    # Açık mavi hover durumu
    "active_secondary": "#214559",   # Koyu mavi aktif durumu
    
    # Kenar çizgisi
    "border": "#2e4756",             # Kenar çizgisi
    
    # Yarıçap değerleri
    "radius_small": 2,               # Daha küçük köşe yuvarlaklığı
    "radius_medium": 3,              # Orta köşe yuvarlaklığı  
    "radius_large": 4,               # Büyük köşe yuvarlaklığı
    
    # Animasyon süreleri (ms)
    "animation_fast": 150,           # Hızlı animasyon
    "animation_medium": 300,         # Orta hızda animasyon
    "animation_slow": 600,           # Yavaş animasyon
    
    # Gölge efektleri
    "shadow": "0 1px 3px rgba(0, 0, 0, 0.25)",  # Standart gölge
    "shadow_large": "0 3px 6px rgba(0, 0, 0, 0.3)",  # Büyük gölge
    
    # Özel renkler (uygulamaya özgü)
    "network_secure": "#5ba32b",     # Güvenli ağ
    "network_warning": "#e5ac00",    # Şüpheli ağ
    "network_danger": "#d94126",     # Tehlikeli ağ
    "network_unknown": "#4b5d67",    # Bilinmeyen/taranmamış ağ
    
    # Buton gradyanları
    "button_gradient_start": "#1f779b",  # Buton gradyan başlangıç
    "button_gradient_end": "#295f85",    # Buton gradyan bitiş
    "button_hover_gradient_start": "#2b94c4", # Buton hover gradyan başlangıç
    "button_hover_gradient_end": "#346d9b",   # Buton hover gradyan bitiş
    
    # Sidebar özel renkleri
    "sidebar_active": "#1f3141",        # Aktif menü item bg
    "sidebar_hover": "#254761",         # Hover menü item bg
    "sidebar_text_active": "#66c0f4",   # Aktif menü metin
    "sidebar_text_normal": "#c7d5e0",   # Normal menü metin
}

# Renk temaları (koyu/açık) - Steam sadece koyu temayı destekler, ama ihtiyaç olursa açık tema da eklenebilir
THEMES = {
    "dark": THEME,
    "light": {
        # Ana renkler (daha açık tonlar)
        "background": "#f2f5f8",         # Açık mavi/gri arka plan
        "card_background": "#ffffff",    # Beyaz kart arka planı
        "sidebar_background": "#f0f5fa", # Açık mavi sidebar
        
        # Vurgu renkleri (aynı)
        "primary": "#1f78b4",            # Koyu mavi vurgu
        "secondary": "#a3c2d7",          # Açık mavi
        "tertiary": "#4e749a",           # Orta mavi
        
        # Durum renkleri (aynı)
        "success": "#5ba32b",            # Yeşil
        "warning": "#e5ac00",            # Sarı
        "error": "#d94126",              # Kırmızı
        "info": "#417a9b",               # Mavi
        
        # Metin renkleri (ters)
        "text_primary": "#171a21",       # Koyu lacivert
        "text_secondary": "#2a475e",     # Koyu mavi
        "text_tertiary": "#1f78b4",      # Koyu mavi
        "text_disabled": "#8fa3af",      # Gri
        
        # Etkileşim durumları
        "hover_primary": "#339be0",      # Açık mavi hover durumu
        "active_primary": "#0f5e99",     # Koyu mavi aktif durumu
        "hover_secondary": "#c7d5e0",    # Açık gri hover durumu
        "active_secondary": "#9ab5c7",   # Gri aktif durumu
        
        # Kenar çizgisi
        "border": "#c7d5e0",             # Kenar çizgisi
        
        # Yuvarlaklık değerleri (aynı)
        "radius_small": 2,
        "radius_medium": 3,
        "radius_large": 4,
        
        # Animasyon süreleri (aynı)
        "animation_fast": 150,
        "animation_medium": 300,
        "animation_slow": 600,
        
        # Gölge efektleri (daha hafif)
        "shadow": "0 1px 2px rgba(0, 0, 0, 0.1)",
        "shadow_large": "0 2px 4px rgba(0, 0, 0, 0.15)",
        
        # Özel renkler (aynı)
        "network_secure": "#5ba32b",
        "network_warning": "#e5ac00",
        "network_danger": "#d94126",
        "network_unknown": "#8fa3af",
        
        # Buton gradyanları
        "button_gradient_start": "#1f78b4",
        "button_gradient_end": "#226595",
        "button_hover_gradient_start": "#2b94c4",
        "button_hover_gradient_end": "#346d9b",
        
        # Sidebar özel renkleri
        "sidebar_active": "#e3f0f9",
        "sidebar_hover": "#d1e5f5",
        "sidebar_text_active": "#1f78b4",
        "sidebar_text_normal": "#2a475e",
    }
}

def get_status_color(status):
    """
    Durum bilgisine göre uygun rengi döndürür.
    
    Args:
        status (str): Durum metni (success, warning, error, info, vb.)
        
    Returns:
        str: Renk kodu
    """
    status_map = {
        "success": THEME["success"],
        "warning": THEME["warning"],
        "error": THEME["error"],
        "info": THEME["info"],
        "none": THEME["text_secondary"],
        "high": THEME["error"],
        "medium": THEME["warning"],
        "low": THEME["info"],
        "secure": THEME["success"],
        "unknown": THEME["text_tertiary"]
    }
    
    return status_map.get(status.lower(), THEME["text_primary"])
