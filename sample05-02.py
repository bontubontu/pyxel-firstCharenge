import pyxel
import random

Width = 128
Height = 128
IMG_NO = 0
ENEMY_NO = 1

class Enemy:
    def __init__(self):
        self.x = random.randint(0,Width)
        self.y = random.randint(0,Height)

class App:
    my_x = 0
    my_y = 0
    interval = 30
    cnt = 0
    enemyList = []

    def __init__(self):
        pyxel.init(Width,Height)
        pyxel.load('mychara.pyxres')
        pyxel.run(self.update,self.draw)
    
    def makeEnemy(self):
        self.enemyList.append(Enemy())

    def checkTimer(self):
        bRet = False
        self.cnt = (self.cnt + 1) % self.interval
        if(self.cnt == 0):
            bRet = True
        return bRet
    
    def update(self):
        self.my_x = pyxel.mouse_x
        self.my_y = pyxel.mouse_y
        if(self.checkTimer() == True):
            self.makeEnemy()
        
    def draw(self):
        pyxel.cls(7)
        for i in reversed(range(0,len(self.enemyList))):
            x = self.enemyList[i].x
            y = self.enemyList[i].y
            pyxel.blt(x,y,ENEMY_NO,0,0,16,16,1)

        pyxel.blt(self.my_x,self.my_y,IMG_NO,0,0,16,16,1)

App()