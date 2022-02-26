import pyxel
from random import randrange

class Collidable:

    def collide_with_point(self, px, py):
        return self.x <= px and px <= self.x + self.width \
           and self.y <= py and py <= self.y + self.height

    
    def collide_with_rect(self, rx, ry, rwidth, rheight):
        pass

    def collide_with_drawable(self, d):
        return self.collide_with_point(d.x, d.y)

    def drawCollisionData(self, obj, col):
        pyxel.rectb(self.x, self.y, self.width, self.height, col)
        pyxel.line(self.x, self.y, obj.x, obj.y, col)
        pyxel.rect(obj.x-1, obj.y-1, 3, 3, col)
        
class Center:

    def center(self):
        centerx = self.x + self.width/2
        centery = self.y + self.height/2
        return (centerx, centery)

class Drawable:

    def __init__(self, depth):
        self.depth = depth

    def update_frame(self):
        pass

    def update(self):
        self.update_frame()
        self.y = self.y + self.speed # Update position   

    def draw(self):
        pyxel.blt(self.x, self.y,                                        # (x, y) destination
                  0,                                                     # numero image source
                  self.framex * self.width, self.framey * self.height,   # (x, y) source
                  self.width, self.height,                               # (largeur, hauteur) source et destination)
                  0)                                                     # couleur transparente

    def is_visible(self):
        return self.y < pyxel.height

class Blackhole(Collidable, Center, Drawable):

    def __init__(self):
        self.depth   = 1
        self.width   = 32
        self.height  = 32
        self.x       = randrange(0, pyxel.width - self.width)
        self.y       = 0  - self.height
        self.speed   = randrange(2,6)
        self.framex  = randrange(0, 6)
        self.framey  = 6
   
class Star(Drawable):

    def __init__(self):
        self.depth  = 0
        self.width  = 8
        self.height = 8
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = 0
        self.speed  = randrange(2, 5)
        self.framex = randrange(0, 16)
        self.framey = 22

class OtherObject(Drawable):
    
   def __init__ (self):
        self.height = 16
        self.width  = 16
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = -self.height
        self.speed  = randrange(1, 2)
        self.framex = randrange(0, 6)
        self.framey = 14

        
    
class Planet(Collidable, Center, Drawable):

    def __init__ (self):
        self.depth  = 1
        self.height = 16
        self.width  = 16
        self.x      = randrange(0, pyxel.width - self.width)
        self.y      = -self.height
        self.speed  = randrange(1, 5)
        self.framex = randrange(0, 15)
        self.framey = 8
    
class Implosion(Drawable, Center):

    def __init__(self, blackhole):
        self.depth  = 2
        self.x      = blackhole.x
        self.y      = blackhole.y
        self.height = 16
        self.width  = 16
        self.speed  = blackhole.speed
        self.framex = 0
        self.framey = 7

    def update_frame(self):
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
            elif self.framex == 14:
                self.framex = 15
            else:
                self.framex = 16 # DONE

    def is_done(self):
        return self.framex == 16

class PlanetExplosion(Drawable):

    def __init__(self, planet):
        self.depth  = 1
        self.x      = planet.x
        self.y      = planet.y
        self.height = 16
        self.width  = 16
        self.speed  = planet.speed
        self.framex = 0
        self.framey = randrange (3, 6)

    def update_frame(self):
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
    
class Life(Drawable):

    def __init__(self):
        self.depth  = 3
        self.height = 16
        self.width  = 32
        self.x      = 0
        self.y      = pyxel.height - self.height
        self.speed  = 0
        self.framex = 0
        self.framey = 9
        self.life   = 18
        
    def draw(self):
        Drawable.draw(self)

        x = self.x + 8
        y = self.y + 6
        w = self.life
        h = 4
        color = 11
        pyxel.rect(x, y, w, h, color)

    def dec(self):
        self.life = max(0, self.life - 3)

    def inc(self):
        self.life = min(18, self.life + 3)

    def die_immediatly(self):
        self.life = 0

    def is_dead(self):
        return self.life == 0

class Rocket(Collidable, Center):

    def __init__(self):
        self.depth  = 2
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
        pyxel.blt(self.x, self.y,                                     # (x, y) destination
                  0,                                                  # numero image source
                  self.framex * self.width,self.framey * self.height, # (x, y) source
                  self.width, self.height,                            # (largeur, hauteur) source et destination
                  0)                                                  # Couleur transparente
            
class SpaceAdventure:
    
    def __init__(self):
        pyxel.init(160, 120, caption="Space-Adventure.py", fps=30)
        pyxel.load("space-adventure.pyxres")

        self.blackholes          = []
        self.stars               = []
        self.planets             = []
        self.rocket              = Rocket()
        self.life                = Life()
        self.planet_explosions   = []
        self.implosion           = None

        # Drawables sorted by depth:
        # [0] Stars
        # [1] Blackholes, planets, planet explosions
        # [2] Rocket, implosion
        # [3] HUD
        #
        # FIXME Find a better name for this tree of drawables.
        self.drawables = [[], [], [], []]
        self.add_drawable(self.rocket)
        self.add_drawable(self.life)
        
        pyxel.run(self.update, self.draw)

    def add_drawable(self, drawable):
        self.drawables[drawable.depth].append(drawable)

    def remove_drawable(self, drawable):
        self.drawables[drawable.depth].remove(drawable)

    def remove_rocket(self):
        self.remove_drawable(self.rocket)
        self.rocket = None     

    def rocket_destroyed_by_planet(self, planet):
        self.remove_rocket()
        self.add_planet_explosion( PlanetExplosion(planet) )

    def rocket_implosion(self, blackhole):
        self.remove_rocket()
        blackhole.speed = 0
        self.implosion  = Implosion(blackhole)
        self.add_drawable(self.implosion)
        self.remove_blackhole(blackhole)

    def update_blackholes(self):
        for blackhole in self.blackholes:
            self.apply_blackhole_gravity(blackhole)    
            if not blackhole.is_visible():
                self.remove_blackhole(blackhole)
                
        if pyxel.frame_count % 200 == 0:
            blackhole = Blackhole()
            self.add_blackhole(blackhole)
            
    def add_blackhole(self, blackhole):
        self.add_drawable(blackhole)
        self.blackholes.append(blackhole)
        
    def remove_blackhole(self, blackhole):
        self.remove_drawable(blackhole)
        self.blackholes.remove(blackhole)
        
    def apply_blackhole_gravity(self, blackhole):
        if self.rocket is None:
            return
        
        (rx, ry) = self.rocket.center()
        (bx, by) = blackhole.center()
        if bx > rx:
            self.rocket.x = self.rocket.x + 1
        elif bx < rx:
            self.rocket.x = self.rocket.x - 1
        if by > ry:
            self.rocket.y = self.rocket.y + 1
        elif by < ry:
            self.rocket.y = self.rocket.y - 1

        if blackhole.collide_with_drawable(self.rocket):
            self.rocket_implosion(blackhole)
            
    def add_star(self, star):
        self.add_drawable(star)
        self.stars.append(star)

    def remove_star(self, star):
        self.remove_drawable(star)
        self.stars.remove(star)

    def update_stars(self):
        for star in self.stars:
            if not star.is_visible():
                self.remove_star(star)
        if pyxel.frame_count % 1 == 0:
            star = Star()
            self.add_star(star)

    def update_implosion(self):
        if self.implosion is None:
            return
        if self.implosion.is_done():
            self.life.die_immediatly()

    def add_planet(self, planet):
        self.add_drawable(planet)
        self.planets.append(planet)

    def remove_planet(self, planet):
        self.remove_drawable(planet)
        self.planets.remove(planet)

    def add_planet_explosion(self, planet_explosion):
        self.add_drawable(planet_explosion)
        self.planet_explosions.append(planet_explosion)

    def remove_planet_explosion(self, planet_explosion):
        self.remove_drawable(planet_explosion)
        self.planet_explosions.remove(planet_explosion)

    def update_planets(self):
        for planet in self.planets:
            if not planet.is_visible():
                self.remove_planet(planet)
                continue
            
            if self.rocket is not None and planet.collide_with_drawable(self.rocket):
                    self.remove_planet(planet)
                    self.life.dec()
                    self.add_planet_explosion(PlanetExplosion(planet))
                    if self.life.is_dead():
                        self.rocket_destroyed_by_planet(planet)     
        if pyxel.frame_count % 50 == 0:
            planet = Planet()
            self.add_planet(planet)

        for planet_explosion in self.planet_explosions:
            if planet_explosion.is_done():
                self.remove_planet_explosion(planet_explosion)

    def is_game_over(self):
        if self.implosion is not None:
            return self.implosion.is_done()
        else:
            return self.life.is_dead()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for depth in range(0, len(self.drawables)):
            drawables = self.drawables[depth]
            for drawable in drawables:
                drawable.update()
            
        self.update_stars()
        self.update_implosion()
        self.update_planets()
        if self.is_game_over():
            return

        self.update_blackholes()
                
    def draw_planet_collision_data(self):
        col = 0
        for planet in self.planets:
            if self.rocket is not None:
                planet.drawCollisionData(self.rocket, 2+col)
                col += 1
                col %= 14

    def draw_game_over(self):
        if self.is_game_over():
            pyxel.text(pyxel.width / 2 - 30, pyxel.height / 2, "GAME OVER ! ", 7)
            
    def draw(self):
        pyxel.cls(0)
        for drawables in self.drawables:
            for drawable in drawables:
                drawable.draw()
        self.draw_planet_collision_data() # XXX
        self.draw_game_over()      

SpaceAdventure()
