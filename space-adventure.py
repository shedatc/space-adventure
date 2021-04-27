import pyxel
from random import randrange

class Star:

    def __init__(self):
        self.width  = 16
        self.height = 16
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = 0
        self.speed  = randrange(2, 7)
        self.types  = randrange(0, 3)

    def update(self):
        if pyxel.frame_count % 0.5 == 0:
                self.y = self.y + self.speed        
    
    def draw(self):
        pyxel.blt(self.x, self.y,          # (x, y) destination
                  0,                       # numero image source
                  self.types*self.width, 112,         # (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination
                  0)                       # Couleur transparente

    def isVisible(self):
        return self.y < pyxel.height

    
class Planet:

    def __init__ (self):
        self.height = 16
        self.width  = 16
        self.x      = randrange(1, 5)
        self.y      = 0
        

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x,self.y,         # (x, y) destination
                  0,                       # numero image source
                  self.types*self.width, 112,         # (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination
                  0)                       # Couleur transparente
        
class Rocket:

    def __init__(self):
        self.width  = 16
        self.height = 16
        self.x      = (pyxel.width / 2) - (self.width / 2)
        self.y      = pyxel.height - self.height
        self.framex = 3
        self.framey = 1
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_RIGHT):
            pass
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.x - 1 >= 0:
                self.x = self.x - 1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.x + 1 <= pyxel.width - self.width:
                self.x = self.x + 1
                
        if pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_DOWN):
            pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.y + 1 <= pyxel.height - self.height:
                self.y = self.y + 1
                self.framey = 2
        elif pyxel.btn(pyxel.KEY_UP):
            if self.y - 1 >= 0:
                self.y = self.y - 1
                self.framey = 0
        else:
                self.framey = 1
        if pyxel.frame_count % 5 == 0:
            if self.framex == 3:
                self.framex = 2            
            elif self.framex == 2:
                self.framex = 1
            elif self.framex == 1:
                self.framex = 0
            elif self.framex == 0:
                self.framex = 3

    def draw(self):
        pyxel.blt(self.x, self.y,         # (x, y) destination
                  0,                      # numero image source
                  self.framex * self.width,self.framey * self.height, # (x, y) source
                  16, 16,                 # (largeur, hauteur) source et destination
                  0)                      # Couleur transparente
        if False:
            pyxel.text(0, 0, f"y = {self.y} y+10 = {self.y+10} y-10 = {self.y-10}", 1)

class SpaceAdventure:
    
    def __init__(self):
        pyxel.init(160, 120, caption="Space-Adventure.py", fps=30)
        pyxel.load("space-adventure.pyxres")
        
        self.stars = []
        
        self.rocket = Rocket()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for star in self.stars:
            star.update()
        if pyxel.frame_count % 5 == 0:
            star  = Star()
            self.stars.append(star)
        
        self.rocket.update()
            
    def draw(self):
        pyxel.cls(0)

        for star in self.stars:
            star.draw()
        
        self.rocket.draw()
       # pyxel.text(0, 10, f"height = {pyxel.height}", 1)
  
SpaceAdventure()
