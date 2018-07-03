import pygame
import random
#------------------------------------------------------------------------------------------------------------------
#main
def main():
    #globals
    global fps, enemyProjectileList, currentLocation, clock, playing, sprites, stoneGroup, player, playerProjectileList, enemiesList, screen
    #game loop
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            player.firing()    
        for p in playerProjectileList:
            for e in enemiesList:
                if p.collisionDetect(e):
                    e.drop()
                    enemiesList.remove(e)
                    sprites.remove(e)
                    playerProjectileList.remove(p)
                    sprites.remove(p)
            if p.rect.x < -100 or p.rect.x > 900 or p.rect.y < -100 or p.rect.y > 900:
                playerProjectileList.remove(p)
                sprites.remove(p)
        for p in enemyProjectileList:
            if p.collisionDetect(player):
                    reset()
            if p.rect.x < -100 or p.rect.x > 900 or p.rect.y < -100 or p.rect.y > 900:
                enemyProjectileList.remove(p)
                sprites.remove(p)
        transition()
        screen.fill(currentLocation)
        sprites.update()
        sprites.draw(screen)
        stoneGroup.update()
        stoneGroup.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    #quit
    pygame.quit()
#------------------------------------------------------------------------------------------------------------------
#player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.size = 50
        self.image = pygame.Surface((self.size,self.size))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (screenWidth/2, screenHeight/2)
    def update(self):
        global enemiesList
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.rect.x -= self.speed
        if keystate[pygame.K_d]:
             self.rect.x += self.speed
        if keystate[pygame.K_w]:
             self.rect.y -= self.speed
        if keystate[pygame.K_s]:
            self.rect.y += self.speed
        for e in enemiesList:
            if self.collisionDetect(e):
                reset()
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def firing(self):
        global sprites, playerProjectileList
        offset = self.size*.2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            projectile = PlayerProjectileLeft()
            projectile.rect.x = self.rect.x - offset
            projectile.rect.y = self.rect.y + self.size/2
            sprites.add(projectile)
            playerProjectileList.add(projectile)
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            projectile = PlayerProjectileRight()
            projectile.rect.x = self.rect.x + self.size + offset
            projectile.rect.y = self.rect.y + self.size/2
            sprites.add(projectile)
            playerProjectileList.add(projectile)
        if keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
            projectile = PlayerProjectileUp()
            projectile.rect.x = self.rect.x + self.size/2
            projectile.rect.y = self.rect.y - offset
            sprites.add(projectile)
            playerProjectileList.add(projectile)
        if keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            projectile = PlayerProjectileDown()
            projectile.rect.x = self.rect.x + self.size/2
            projectile.rect.y = self.rect.y + self.size + offset
            sprites.add(projectile)
            playerProjectileList.add(projectile)
#------------------------------------------------------------------------------------------------------------------
#player projectile sprites
class PlayerProjectileLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size,self.size/2))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class PlayerProjectileRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size,self.size/2))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect() 
    def update(self):
        self.rect.x += self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class PlayerProjectileUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size/2,self.size))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class PlayerProjectileDown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size/2,self.size))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)
#------------------------------------------------------------------------------------------------------------------
#enemy projectile sprites
class EnemyProjectileLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size,self.size/2))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class EnemyProjectileRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size,self.size/2))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect() 
    def update(self):
        self.rect.x += self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class EnemyProjectileUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size/2,self.size))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class EnemyProjectileDown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.size = 10
        self.image = pygame.Surface((self.size/2,self.size))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += self.speed
    def collisionDetect(self, sprite):
        return self.rect.colliderect(sprite.rect)
#------------------------------------------------------------------------------------------------------------------
#enemy sprites
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.size = 30
        self.image = pygame.Surface((self.size,self.size))
        self.image.fill((160,160,160))
        self.rect = self.image.get_rect()
        self.ctr = round(fps/2)
        self.currDirect = 5
    def update(self):
        global fps
        #edge
        if self.rect.x <= 10:
            self.ctr = round(fps*(random.randint(30,70)/100))
            self.currDirect = 4
        if self.rect.x >= 760:
            self.ctr = round(fps*(random.randint(30,70)/100))
            self.currDirect = 3
        if self.rect.y <= 10:
            self.ctr = round(fps*(random.randint(30,70)/100))
            self.currDirect = 2
        if self.rect.y >= 760:
            self.ctr = round(fps*(random.randint(30,70)/100))
            self.currDirect = 1
        #movement lock
        if self.ctr == 0:
            path = round(fps*(random.randint(110,200)/100))
            self.ctr = path
            self.currDirect = random.randint(1,5)
        #movement
        if self.currDirect == 1:
            self.rect.y -= self.speed #up
        elif self.currDirect == 2:
            self.rect.y += self.speed #down
        elif self.currDirect == 3:
            self.rect.x -= self.speed #left
        elif self.currDirect == 4:
            self.rect.x += self.speed #right
        self.ctr -= 1
    #chance to drop stone
    def drop(self):
        global stoneGroup, sprites
        if random.randint(1,level) == 1:
            stone = Stone()
            stone.rect.x = self.rect.x
            stone.rect.y = self.rect.y
            stoneGroup.add(stone)
            sprites.add(stone)
class BigEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.size = 70
        self.image = pygame.Surface((self.size,self.size))
        self.image.fill((160,160,160))
        self.rect = self.image.get_rect()
        self.ctr = round(fps/2)
        self.ctr2 = fps*2
        self.currDirect = 5
    def update(self):
        global fps
        #edge
        if self.rect.x <= 10:
            self.ctr = round(fps*(random.randint(70,100)/100))
            self.currDirect = 4
        if self.rect.x >= 720:
            self.ctr = round(fps*(random.randint(70,100)/100))
            self.currDirect = 3
        if self.rect.y <= 10:
            self.ctr = round(fps*(random.randint(70,100)/100))
            self.currDirect = 2
        if self.rect.y >= 720:
            self.ctr = round(fps*(random.randint(70,100)/100))
            self.currDirect = 1
        #movement lock
        if self.ctr == 0:
            path = round(fps*(random.randint(110,300)/100))
            self.ctr = path
            self.currDirect = random.randint(1,5)
        #movement
        if self.currDirect == 1:
            self.rect.y -= self.speed #up
        elif self.currDirect == 2:
            self.rect.y += self.speed #down
        elif self.currDirect == 3:
            self.rect.x -= self.speed #left
        elif self.currDirect == 4:
            self.rect.x += self.speed #right
        self.ctr -= 1
        if self.ctr2 == 0:
            self.firing()
            self.ctr2 = fps*2
        self.ctr2 -= 1
    def firing(self):
        global enemyProjectileList
        offset = self.size*.2
        projectile = EnemyProjectileUp()
        projectile.rect.x = self.rect.x + self.size/2
        projectile.rect.y = self.rect.y - offset
        sprites.add(projectile)
        enemyProjectileList.add(projectile)
        projectile = EnemyProjectileDown()
        projectile.rect.x = self.rect.x + self.size/2
        projectile.rect.y = self.rect.y + self.size + offset
        sprites.add(projectile)
        enemyProjectileList.add(projectile)
        projectile = EnemyProjectileLeft()
        projectile.rect.x = self.rect.x - offset
        projectile.rect.y = self.rect.y + self.size/2
        sprites.add(projectile)
        enemyProjectileList.add(projectile)
        projectile = EnemyProjectileRight()
        projectile.rect.x = self.rect.x + self.size + offset
        projectile.rect.y = self.rect.y + self.size/2
        sprites.add(projectile)
        enemyProjectileList.add(projectile)
    #chance to drop stone
    def drop(self):
        global stoneGroup, sprites
        if random.randint(1,level) == 1:
            stone = Stone()
            stone.rect.x = self.rect.x
            stone.rect.y = self.rect.y
            stoneGroup.add(stone)
            sprites.add(stone)
#------------------------------------------------------------------------------------------------------------------
#hud sprite
class Hud(pygame.sprite.Sprite):
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        global level, screen
        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y= 0
        self.text = ''
    def update(self):
        global screen
        self.text = pygame.font.Font('freesansbold.ttf',20).render('Level: '+str(level), True, (255,255,255))
        screen.blit(self.text, (0,0))
#------------------------------------------------------------------------------------------------------------------
#stone sprite
class Stone(pygame.sprite.Sprite):
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.size = 15
        self.image = pygame.Surface((self.size,self.size))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.colliderect(player.rect):
            updateLevel()
#------------------------------------------------------------------------------------------------------------------
#next level
def updateLevel():
    global level, playerProjectileList, enemiesList, sprites, screenWidth, screenHeight
    level += 1
    clearGroups()
    player.rect.center = (screenWidth/2, screenHeight/2)
    spawnEnemies()
#------------------------------------------------------------------------------------------------------------------
#spawn enemies
def spawnEnemies():
    global level, enemiesList, sprites
    for i in range(1,level+1):
        if random.randint(1,4) == 4:
            while True:
                enemy = BigEnemy()
                enemy.rect.x = random.randint(20,750)
                enemy.rect.y = random.randint(20,750)
                enemiesList.add(enemy)
                sprites.add(enemy)
                if player.collisionDetect(enemy):
                    enemiesList.remove(enemy)
                    sprites.remove(enemy)
                else:
                    break
        else:
            while True:
                enemy = SmallEnemy()
                enemy.rect.x = random.randint(20,750)
                enemy.rect.y = random.randint(20,750)
                enemiesList.add(enemy)
                sprites.add(enemy)
                if player.collisionDetect(enemy):
                    enemiesList.remove(enemy)
                    sprites.remove(enemy)
                else:
                    break
    
#------------------------------------------------------------------------------------------------------------------
#area transition
def transition():
    global currentLocation, player, playerProjectileList, sprites, enemiesList, stoneGroup
    if player.rect.x <= 10:
        player.rect.x = 730
        location = random.randint(0,len(colors)-1)
        currentLocation = colors[location]
        clearGroups()
        spawnEnemies()
    elif player.rect.x >= 730:
        player.rect.x = 20
        location = random.randint(0,len(colors)-1)
        currentLocation = colors[location]
        clearGroups()
        spawnEnemies()
    elif player.rect.y <= 10:
        player.rect.y = 730
        location = random.randint(0,len(colors)-1)
        currentLocation = colors[location]
        clearGroups()
        spawnEnemies()
    elif player.rect.y >= 730:
        player.rect.y = 20
        location = random.randint(0,len(colors)-1)
        currentLocation = colors[location]
        clearGroups()
        spawnEnemies()
#------------------------------------------------------------------------------------------------------------------
#clears all groups
def clearGroups():
    global playerProjectileList, enemyProjectileList, enemiesList, stoneGroup, sprites
    for p in playerProjectileList:
        playerProjectileList.remove(p)
        sprites.remove(p)
    for p in enemyProjectileList:
        enemyProjectileList.remove(p)
        sprites.remove(p)
    for e in enemiesList:
        enemiesList.remove(e)
        sprites.remove(e)
    for s in stoneGroup:
        stoneGroup.remove(s)
        sprites.remove(s)
#------------------------------------------------------------------------------------------------------------------
#reset
def reset():
    global level
    clearGroups()
    level = 1
    player.rect.center = (screenWidth/2, screenHeight/2)
    spawnEnemies()
#------------------------------------------------------------------------------------------------------------------
#initialize
pygame.init()
screenWidth = 800
screenHeight = 800
fps = 144
colors = [(51, 204, 51), (255, 0, 0), (153, 102, 51), (0, 0, 255), (255, 153, 255)]#green, red, brown, blue, pink
currentLocation = colors[0]
level = 1
clock = pygame.time.Clock()
playing = True
sprites = pygame.sprite.Group()
player = Player()
playerProjectileList = pygame.sprite.Group()
enemyProjectileList = pygame.sprite.Group()
enemiesList = pygame.sprite.Group()
hud = Hud()
stoneGroup = pygame.sprite.Group()
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('World\'s Hardest Game, but it\'s not, and it\'s harder :)')
sprites.add(player)
sprites.add(hud)
spawnEnemies()
#------------------------------------------------------------------------------------------------------------------
#run main
if __name__== "__main__":
  main()