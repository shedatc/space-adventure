import pyxel
from random import randrange

class Collidable:

    def collide_with_point(self, point):
        (px, py) = point
        return self.x <= px and px <= self.x + self.width \
           and self.y <= py and py <= self.y + self.height

    
    def collide_with_rect(self, rect):
        p1 = (rect.x, rect.y)
        p2 = (rect.x + rect.width, rect.y)
        p3 = (rect.x, rect.y + rect.height)
        p4 = (rect.x + rect.width, rect.y + rect.height)
        for p in [p1, p2, p3, p4]:
            if self.collide_with_point(p):
                return True
        return False

class Center:

    def center(self):
        centerx = self.x + self.width/2
        centery = self.y + self.height/2
        return (centerx, centery)

class Blackhole(Collidable, Center):

    def __init__(self):

        self.width   = 40
        self.height  = 32
        self.x       = randrange(0, pyxel.width - self.width)
        self.y       = 0  - self.height
        self.speed   = 2
        self.types   = randrange(0, 2)

    def update(self):

         if pyxel.frame_count % 1 == 0:
                self.y = self.y + self.speed   

    def draw(self):

         pyxel.blt(self.x, self.y,                    # (x, y) destination
                  0,                                  # numero image source
                  self.types*self.width, 192,         # (x, y) source
                  self.width, self.height,             # (largeur, hauteur) source et destination)
                  0)                                 # couleur transparente

    def is_visible(self):
        return self.y < pyxel.height

   
class Star:

    def __init__(self):
        self.width  = 16
        self.height = 16
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = 0
        self.speed  = randrange(2, 7)
        self.types  = randrange(0, 13)

    def update(self):
        if pyxel.frame_count % 1 == 0:
                self.y = self.y + self.speed        
    
    def draw(self):
        pyxel.blt(self.x, self.y,          # (x, y) destination
                  0,                       # numero image source
                  self.types*self.width, 160,         # (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination
                  0)                       # Couleur transparente

    def is_visible(self):
        return self.y < pyxel.height
    
class Planet(Collidable, Center):

    def __init__ (self):
        self.height = 16
        self.width  = 16
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = - self.height
        self.speed  = randrange(1, 3)
        self.types  = randrange(0, 15)
        

    def update(self):
         if pyxel.frame_count % 1 == 0:
                self.y = self.y + self.speed

    def draw(self):
        pyxel.blt(self.x,self.y,           # (x, y) destination
                  0,                       # numero image source
                  self.types*self.width, 128,         # (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination
                  0)                       # Couleur transparente
        
    def is_visible(self):
        return self.y < pyxel.height

        return False
    
class Compression:

    def __init__(self, x, y):
        self.x      = x
        self.y      = y
        self.height = 16
        self.width  = 16
        self.framex = 0
        self.framey = 112

    def update(self):
        if pyxel.frame_count % 5 == 0:
            if self.framex == 0:
                self.framex = 1            
            elif self.framex == 1:
                self.framex = 2
            elif self.framex == 2:
                self.framex = 3
            elif self.framex == 3:
                self.framex = 4
            elif self.framex == 4:
                self.framex = 5
            elif self.framex == 5:
                self.framex = 6
            elif self.framex == 6:
                self.framex = 7
            elif self.framex == 7:
                self.framex = 8            
            elif self.framex == 8:
                self.framex = 9
            elif self.framex == 9:
                self.framex = 10
            elif self.framex == 10:
                self.framex = 11
            elif self.framex == 11:
                self.framex = 12
            elif self.framex == 12:
                self.framex = 13
            elif self.framex == 13:
                self.framex = 14
            else:
                self.framex = 15 # DONE

    def is_done(self):
        return self.framex == 15

    def draw(self):
        pyxel.blt(self.x, self.y,          # (x, y) destination
                  0,                       # numero image source
                  self.framex*self.width, self.framey*self.height,# (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination)
                  0)                       # couleur transparente
         
class Explosion:

    def __init__(self, x, y):
        self.x      = x
        self.y      = y
        self.height = 16
        self.width  = 16
        self.framex = 0
        self.framey = randrange (3, 6)

    def update(self):
        if pyxel.frame_count % 5 == 0:
            if self.framex == 0:
                self.framex = 1            
            elif self.framex == 1:
                self.framex = 2
            elif self.framex == 2:
                self.framex = 3
            elif self.framex == 3:
                self.framex = 4
            elif self.framex == 4:
                self.framex = 5
            elif self.framex == 5:
                self.framex = 6
            elif self.framex == 6:
                self.framex = 7
            else:
                self.framex = 8 # DONE

    def is_done(self):
        return self.framex == 8

    def draw(self):
        pyxel.blt(self.x, self.y,          # (x, y) destination
                  0,                       # numero image source
                  self.framex*self.width, self.framey*self.height,# (x, y) source
                  self.width, self.height, # (largeur, hauteur) source et destination)
                  0)                       # couleur transparente
         
    
class Rocket(Collidable, Center):

    def __init__(self):
        self.width  = 16
        self.height = 16
        self.x      = (pyxel.width / 2) - (self.width / 2)
        self.y      = pyxel.height - self.height
        self.framex = 3
        self.framey = 1
        self.speed  = 2
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_RIGHT):
            pass
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.x - self.speed >= 0:
                self.x = self.x - self.speed
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.x + self.speed <= pyxel.width - self.width:
                self.x = self.x + self.speed
                
        if pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_DOWN):
            pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.y + self.speed <= pyxel.height - self.height:
                self.y = self.y + self.speed
                self.framey = 2
        elif pyxel.btn(pyxel.KEY_UP):
            if self.y - self.speed >= 0:
                self.y = self.y - self.speed
                self.framey = 0
        else:
                self.framey = 1

        # Animate the rocket
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
                  self.width, self.height,                 # (largeur, hauteur) source et destination
                  0)                      # Couleur transparente
        if False:
            pyxel.text(0, 0, f"y = {self.y} y+10 = {self.y+10} y-10 = {self.y-10}", 1)
            
class SpaceAdventure:
    
    def __init__(self):
        pyxel.init(160, 120, caption="Space-Adventure.py", fps=30)
        pyxel.load("space-adventure.pyxres")

        self.blackholes   = []
        self.stars        = []
        self.planets      = []
        self.rocket       = Rocket()
        self.explosion    = None
        self.is_game_over = False
        
        pyxel.run(self.update, self.draw)

    def rocket_destroyed_by_planet(self, planet):

        self.planets.remove(planet)
        self.rocket    = None
        self.explosion = Explosion(planet.x, planet.y)

    def rocket_destroyed_by_blackhole(self, blackhole):
        
        self.compression = Compression(blackhole.x, blackhole.y)
        self.rocket    = None
        

    def update_blackholes(self):
        
        # Update existing blackholes and remove them if needed
        for blackhole in self.blackholes:
            blackhole.update()
            if not blackhole.is_visible():
                self.blackholes.remove(blackhole)

        # Generate new blackholes
        if pyxel.frame_count % 200 == 0:
            blackhole = Blackhole()
            self.blackholes.append(blackhole)

        # Handle blackhole gravity field
        if self.rocket is None:
            return
        
        (rx, ry) = self.rocket.center()
        for blackhole in self.blackholes:
            (bx, by) = blackhole.center()
            if bx > rx:
                self.rocket.x = self.rocket.x + 1
            elif bx < rx:
                self.rocket.x = self.rocket.x - 1
            if by > ry:
                self.rocket.y = self.rocket.y + 1
            elif by < ry:
                self.rocket.y = self.rocket.y - 1
            
            if self.rocket is not None and blackhole.collide_with_rect(self.rocket):
                self.rocket_destroyed_by_blackhole(blackhole)


    def update(self):
                  
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.is_game_over:
           return 

        self.update_blackholes()

        for star in self.stars:
            star.update()
            if not star.is_visible():
                self.stars.remove(star)
        if pyxel.frame_count % 3 == 0:
            star = Star()
            self.stars.append(star)

        # Planets
        for planet in self.planets:
            planet.update()
            
            if not planet.is_visible():
                self.planets.remove(planet)
                continue
            
            if self.rocket is not None and planet.collide_with_rect(self.rocket):
                self.rocket_destroyed_by_planet(planet)
        if pyxel.frame_count % 50 == 0:
            planet = Planet()
            self.planets.append(planet)

        if self.rocket is not None:
            self.rocket.update()

        if self.explosion is not None:
            self.explosion.update()
            if self.explosion.is_done():
                self.is_game_over = True

        if self.compression is not None:
            self.compression.update()
            if self.compression.is_done():
                self.is_game_over = True
            
    def draw(self):
        pyxel.cls(0)

        for blackhole in self.blackholes:
            blackhole.draw()

        for star in self.stars:
            star.draw()

        for planet in self.planets:
            planet.draw()
            
        if self.rocket is not None:
            self.rocket.draw()


        if self.explosion is not None:
            self.explosion.draw()

        if self.compression is not None:
            self.compression.draw()

        if self.is_game_over:
            pyxel.text(pyxel.width / 2, pyxel.height / 2, "GAME OVER ! ", 1)





                  
  
SpaceAdventure()
