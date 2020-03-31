#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        self.window = Window()
        self.rect = MoveRect()
        pyxel.run(self.update, self.draw)
    def update(self):
        self.rect.update()
    def draw(self):
        self.window.draw()
        self.rect.draw()

class Window:
    def __init__(self, width=128, height=96, border_width=0):
        pyxel.init(width, height, border_width=border_width)
    def draw(self): pyxel.cls(0)

class MoveRect:
    def __init__(self, x=0, y=0, width=16, height=16, color=8):
        self.w = width
        self.h = height
        self.x = (pyxel.width / 2) - (self.w / 2)
        self.y = (pyxel.height/ 2) - (self.h / 2)
        self.c = color
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0: self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < pyxel.width - self.w: self.x += 1
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0: self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height - self.h: self.y += 1
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.c)


App()
