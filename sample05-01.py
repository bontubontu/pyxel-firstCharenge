import pyxel

Width = 128
Height = 128
IMG_NO = 0

class App:
    my_x = 0
    my_y = 0
    interval = 30
    cnt = 0

    def __init__(self):
        pyxel.init(Width,Height)
        pyxel.load('mychara.pyxres')
        pyxel.run(self.update,self.draw) #update関数:1秒間に30回実行される
    
    def makeEnemy(self):
        print('Crate Enemy')

    def checkTimer(self):
        bRet = False
        self.cnt = (self.cnt + 1) % self.interval #カウントアップしつつ余剰計算でself.intervalより大きい場合はカウントを0にリセット
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
        pyxel.blt(self.my_x,self.my_y,IMG_NO,0,0,16,16,1)

App()