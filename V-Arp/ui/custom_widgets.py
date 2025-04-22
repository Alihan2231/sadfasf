#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Steam benzeri özel arayüz bileşenleri
Bu modül, uygulamanın Steam tarzı özel arayüz bileşenlerini içerir.
"""

import tkinter as tk
from tkinter import ttk, font
import traceback
import time
import math
from ui.colors import THEME, get_status_color
import random
import os
import logging

# Loglama
logger = logging.getLogger("NetworkShieldPro.custom_widgets")

class SteamFrame(tk.Canvas):
    """Steam tarzı çerçeve"""
    def __init__(self, parent, bg=THEME["card_background"], width=200, height=100, 
                 corner_radius=THEME["radius_small"], border_color=None, **kwargs):
        super().__init__(parent, bg=THEME["background"], highlightthickness=0, 
                          width=width, height=height, **kwargs)
        self.corner_radius = corner_radius
        self.bg = bg
        self.border_color = border_color
        
        # Çerçeveyi çiz
        self._draw_frame()
        
        # Boyut değiştiğinde yeniden çiz
        self.bind("<Configure>", self._on_resize)
    
    def _draw_frame(self):
        """Çerçeveyi çizer"""
        self.delete("all")
        width, height = self.winfo_width(), self.winfo_height()
        
        # Boyutlar çok küçükse çizme
        if width < 1 or height < 1:
            return
        
        # Köşe yarıçapı boyutlara göre ayarla
        radius = min(self.corner_radius, width//2, height//2)
        
        # Steam tarzı az yuvarlatılmış köşeli dikdörtgen
        points = [
            radius, 0,
            width-radius, 0,
            width, radius,
            width, height-radius,
            width-radius, height,
            radius, height,
            0, height-radius,
            0, radius
        ]
        
        # Ana dikdörtgen
        if self.border_color:
            # Kenarlık çiz
            self.create_polygon(points, smooth=True, fill=self.border_color, outline="")
            # İç dolgu (1px daha küçük)
            inner_points = [
                radius, 1,
                width-radius-1, 1,
                width-1, radius,
                width-1, height-radius-1,
                width-radius-1, height-1,
                radius, height-1,
                1, height-radius-1,
                1, radius
            ]
            self.create_polygon(inner_points, smooth=True, fill=self.bg, outline="")
        else:
            self.create_polygon(points, smooth=True, fill=self.bg, outline="")
            
        # Steam tarzı ince üst çizgi (mavi highlight)
        if self.border_color != THEME["primary"]:  # Zaten primary renk kenarlık yoksa
            self.create_line(radius, 0, width-radius, 0, fill=THEME["primary"], width=1)
    
    def _on_resize(self, event):
        """Boyut değiştiğinde yeniden çizer"""
        self._draw_frame()

class SteamButton(tk.Canvas):
    """Steam tarzı buton"""
    def __init__(self, parent, text="Buton", command=None, width=120, height=28, 
                 corner_radius=THEME["radius_small"], icon=None, **kwargs):
        super().__init__(parent, bg=THEME["background"], highlightthickness=0, 
                          width=width, height=height, **kwargs)
        self.text = text
        self.command = command
        self.corner_radius = corner_radius
        self.state = "normal"
        self.icon = icon
        
        # Buton çiz
        self._draw_button()
        
        # Etkileşim için event'leri bağla
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Configure>", self._on_resize)
    
    def _draw_button(self):
        """Butonu çizer"""
        self.delete("all")
        width, height = self.winfo_width(), self.winfo_height()
        
        # Boyutlar çok küçükse çizme
        if width < 1 or height < 1:
            return
        
        # Köşe yarıçapı boyutlara göre ayarla
        radius = min(self.corner_radius, width//2, height//2)
        
        # Buton durumuna göre renkleri belirle
        if self.state == "disabled":
            start_color = THEME["secondary"]
            end_color = THEME["secondary"]
            text_color = THEME["text_disabled"]
            border_color = THEME["border"]
        elif self.state == "active":
            start_color = THEME["button_gradient_end"]
            end_color = THEME["button_gradient_start"]
            text_color = THEME["text_secondary"]
            border_color = THEME["tertiary"]
        elif self.state == "hover":
            start_color = THEME["button_hover_gradient_start"]
            end_color = THEME["button_hover_gradient_end"]
            text_color = THEME["text_primary"]
            border_color = THEME["primary"]
        else:
            start_color = THEME["button_gradient_start"]
            end_color = THEME["button_gradient_end"]
            text_color = THEME["text_secondary"]
            border_color = THEME["border"]
        
        # Steam tarzı az yuvarlatılmış köşeli dikdörtgen
        points = [
            radius, 0,
            width-radius, 0,
            width, radius,
            width, height-radius,
            width-radius, height,
            radius, height,
            0, height-radius,
            0, radius
        ]
        
        # Kenarlık (biraz daha koyu)
        self.create_polygon(points, smooth=True, fill=border_color, outline="")
        
        # İç dolgu (1px daha küçük)
        inner_points = [
            radius, 1,
            width-radius-1, 1,
            width-1, radius,
            width-1, height-radius-1,
            width-radius-1, height-1,
            radius, height-1,
            1, height-radius-1,
            1, radius
        ]
        
        # Steam tarzı gradyan dolgu - çok karmaşık gradyan yapamıyoruz, bu yüzden
        # basit bir üst-alt renk geçişi yapıyoruz
        for i in range(height-2):
            # Doğrusal interpolasyon ile renk geçişi
            ratio = i / float(height-3)
            r1 = int(int(start_color[1:3], 16) * (1-ratio) + int(end_color[1:3], 16) * ratio)
            g1 = int(int(start_color[3:5], 16) * (1-ratio) + int(end_color[3:5], 16) * ratio)
            b1 = int(int(start_color[5:7], 16) * (1-ratio) + int(end_color[5:7], 16) * ratio)
            color = f"#{r1:02x}{g1:02x}{b1:02x}"
            
            # Satır çiz
            self.create_line(1, i+1, width-2, i+1, fill=color)
        
        # İkon varsa çiz
        padding = 8
        icon_width = 0
        if self.icon:
            # İkon için yer hesapla
            icon_width = 16
            self.create_text(padding, height//2, text=self.icon, 
                           fill=text_color, font=("Arial", 10), anchor="w")
        
        # Metin
        text_x = padding + icon_width + (0 if not self.icon else 4)
        self.create_text(text_x, height//2, text=self.text, fill=text_color, 
                       font=("Arial", 9), anchor="w")
        
        # Steam tarzı ince üst highlight çizgisi
        highlight_color = THEME["tertiary"] if self.state == "hover" else THEME["border"]
        self.create_line(radius, 1, width-radius, 1, fill=highlight_color, width=1)
    
    def _on_enter(self, event):
        """Üzerine gelince rengini değiştirir"""
        if self.state != "disabled":
            self.state = "hover"
            self._draw_button()
    
    def _on_leave(self, event):
        """Üzerinden ayrılınca rengini değiştirir"""
        if self.state != "disabled":
            self.state = "normal"
            self._draw_button()
    
    def _on_press(self, event):
        """Tıklandığında aktif duruma geçer"""
        if self.state != "disabled":
            self.state = "active"
            self._draw_button()
    
    def _on_release(self, event):
        """Tıklama bırakılınca fonksiyonu çalıştırır"""
        if self.state != "disabled":
            x, y = event.x, event.y
            if 0 <= x <= self.winfo_width() and 0 <= y <= self.winfo_height():
                if self.command:
                    try:
                        self.command()
                    except Exception as e:
                        logger.error(f"Buton komutu çalıştırılırken hata: {e}")
                        traceback.print_exc()
                self.state = "hover"
            else:
                self.state = "normal"
            self._draw_button()
    
    def _on_resize(self, event):
        """Boyut değiştiğinde yeniden çizer"""
        self._draw_button()
    
    def configure(self, **kwargs):
        """Buton özelliklerini yapılandırır"""
        if "text" in kwargs:
            self.text = kwargs.pop("text")
        if "command" in kwargs:
            self.command = kwargs.pop("command")
        if "state" in kwargs:
            self.state = kwargs.pop("state")
        if "icon" in kwargs:
            self.icon = kwargs.pop("icon")
        
        super().configure(**kwargs)
        self._draw_button()

class SteamProgressBar(tk.Canvas):
    """Steam tarzı ilerleme çubuğu"""
    def __init__(self, parent, width=200, height=16, value=0, max_value=100, **kwargs):
        super().__init__(parent, width=width, height=height, bg=THEME["background"], 
                         highlightthickness=0, **kwargs)
        self.value = value
        self.max_value = max_value
        
        # Çubuğu çiz
        self._draw_progressbar()
        
        # Boyut değiştiğinde yeniden çiz
        self.bind("<Configure>", self._on_resize)
    
    def _draw_progressbar(self):
        """İlerleme çubuğunu çizer"""
        self.delete("all")
        width, height = self.winfo_width(), self.winfo_height()
        
        # Boyutlar çok küçükse çizme
        if width < 1 or height < 1:
            return
        
        # Steam tarzı çok az yuvarlatılmış köşeler
        radius = 2
        
        # Arka plan (koyu)
        bg_color = THEME["secondary"]
        self.create_rounded_rectangle(0, 0, width, height, radius, fill=bg_color)
        
        # İlerleme miktarı
        if self.max_value > 0:
            progress_width = int((self.value / self.max_value) * width)
            if progress_width > 0:
                # Steam tarzı mavi gradyan dolgu
                for i in range(progress_width):
                    # Pozisyona göre renk hesapla (yatay gradyan)
                    ratio = i / float(width)
                    r1 = int(int(THEME["primary"][1:3], 16) * (1-ratio) + int(THEME["tertiary"][1:3], 16) * ratio)
                    g1 = int(int(THEME["primary"][3:5], 16) * (1-ratio) + int(THEME["tertiary"][3:5], 16) * ratio)
                    b1 = int(int(THEME["primary"][5:7], 16) * (1-ratio) + int(THEME["tertiary"][5:7], 16) * ratio)
                    color = f"#{r1:02x}{g1:02x}{b1:02x}"
                    
                    # Dikdörtgen olarak çiz
                    self.create_line(i, 2, i, height-2, fill=color)
                
                # Steam tarzı küçük üst parlaklık çizgisi
                self.create_line(1, 2, progress_width-1, 2, fill=THEME["text_secondary"], width=1)
    
    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        """Yuvarlatılmış dikdörtgen oluşturur"""
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def set_value(self, value):
        """İlerleme değerini ayarlar"""
        self.value = min(max(0, value), self.max_value)
        self._draw_progressbar()
    
    def _on_resize(self, event):
        """Boyut değiştiğinde yeniden çizer"""
        self._draw_progressbar()

class SteamMeter(tk.Canvas):
    """Steam tarzı dairesel gösterge"""
    def __init__(self, parent, width=100, height=100, value=0, **kwargs):
        super().__init__(parent, width=width, height=height, bg=THEME["card_background"], 
                         highlightthickness=0, **kwargs)
        self.value = min(max(value, 0), 100)  # 0-100 arası
        
        # Göstergeyi çiz
        self._draw_meter()
        
        # Boyut değiştiğinde yeniden çiz
        self.bind("<Configure>", self._on_resize)
    
    def _draw_meter(self):
        """Dairesel göstergeyi çizer"""
        self.delete("all")
        width, height = self.winfo_width(), self.winfo_height()
        
        # Boyutlar çok küçükse çizme
        if width < 1 or height < 1:
            return
        
        # Merkez ve yarıçap
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 2 - 10
        
        # Arka plan halkası (koyu gri)
        self.create_arc(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       start=0, extent=360, style="arc",
                       width=4, outline=THEME["secondary"])
        
        # İlerleme halkası (mavi Steam rengi)
        if self.value > 0:
            extent = 360 * (self.value / 100.0)
            self.create_arc(center_x - radius, center_y - radius,
                           center_x + radius, center_y + radius,
                           start=90, extent=-extent, style="arc",
                           width=4, outline=THEME["primary"])
        
        # Değer metni (ortada)
        self.create_text(center_x, center_y, text=f"{int(self.value)}", 
                       font=("Arial", 16, "bold"), fill=THEME["text_primary"])
        
        # Alt açıklama metni
        self.create_text(center_x, center_y + 20, text="GÜVENLİK", 
                       font=("Arial", 8), fill=THEME["text_secondary"])
    
    def set_value(self, value):
        """Gösterge değerini ayarlar"""
        self.value = min(max(0, value), 100)
        self._draw_meter()
    
    def _on_resize(self, event):
        """Boyut değiştiğinde yeniden çizer"""
        self._draw_meter()

class SteamSidebarItem(tk.Canvas):
    """Steam tarzı kenar çubuğu öğesi"""
    def __init__(self, parent, text="Menü", icon=None, command=None, width=200, height=32, **kwargs):
        super().__init__(parent, width=width, height=height, bg=THEME["sidebar_background"], 
                         highlightthickness=0, **kwargs)
        self.text = text
        self.icon = icon
        self.command = command
        self.is_active = False
        
        # Öğeyi çiz
        self._draw_item()
        
        # Etkileşim için event'leri bağla
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.bind("<Configure>", self._on_resize)
    
    def _draw_item(self):
        """Menü öğesini çizer"""
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Arka plan rengi (aktif ise farklı renk)
        if self.is_active:
            bg_color = THEME["sidebar_active"]
            text_color = THEME["sidebar_text_active"]
            # Steam tarzı sol mavi bar
            self.create_rectangle(0, 0, 3, height, fill=THEME["primary"], outline="")
        else:
            # Hover kontrolü
            if self.find_withtag("current"):
                bg_color = THEME["sidebar_hover"]
            else:
                bg_color = THEME["sidebar_background"]
            text_color = THEME["sidebar_text_normal"]
        
        # Arka planı çiz
        self.create_rectangle(0, 0, width, height, fill=bg_color, outline="")
        
        # İkon (varsa)
        padding = 12
        if self.icon:
            self.create_text(padding, height/2, text=self.icon, fill=text_color, 
                           font=("Arial", 9), anchor="w")
            icon_width = 20
        else:
            icon_width = 0
        
        # Metin (sola hizalı)
        self.create_text(padding + icon_width, height/2, text=self.text, fill=text_color, 
                       font=("Arial", 11), anchor="w")
    
    def _on_enter(self, event):
        """Üzerine gelince yeniden çizer"""
        self._draw_item()
    
    def _on_leave(self, event):
        """Üzerinden ayrılınca yeniden çizer"""
        self._draw_item()
    
    def _on_click(self, event):
        """Tıklandığında fonksiyonu çalıştırır"""
        if self.command:
            self.command()
    
    def _on_resize(self, event):
        """Boyut değiştiğinde yeniden çizer"""
        self._draw_item()
    
    def set_active(self, active):
        """Aktif durumunu ayarlar"""
        self.is_active = active
        self._draw_item()

class SteamStatusBadge(tk.Canvas):
    """Steam tarzı durum etiketi"""
    def __init__(self, parent, text="Durum", status="info", width=80, height=20, **kwargs):
        super().__init__(parent, width=width, height=height, highlightthickness=0, 
                         bg=THEME["card_background"], **kwargs)
        self.text = text
        self.status = status
        self.color = get_status_color(status)
        
        # Etiketi çiz
        self._draw_badge()
        
        # Boyut değiştiğinde yeniden çiz
        self.bind("<Configure>", lambda e: self._draw_badge())
    
    def _draw_badge(self):
        """Etiketi çizer"""
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Boyutlar çok küçükse çizme
        if width < 1 or height < 1:
            return
        
        # Düşük opasiteleri taklit etmek için koyu arka plan
        bg_color = self._darker_color(self.color, 0.8)
        
        # Steam tarzı çok hafif yuvarlatılmış dikdörtgen
        radius = 2
        self.create_rounded_rectangle(0, 0, width, height, radius, fill=bg_color, outline="")
        
        # Metni ortala
        self.create_text(width//2, height//2, text=self.text, fill=self.color, 
                       font=("Arial", 8, "bold"))
    
    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        """Yuvarlatılmış dikdörtgen oluşturur"""
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def _darker_color(self, color, factor=0.1):
        """Rengi koyulaştırır"""
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        
        return f"#{r:02x}{g:02x}{b:02x}"
