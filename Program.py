from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Score(Sprite):

    def __init__(self, app, position):
        asset = TextAsset(app.score, style="30pt Comic Sans", width=250, fill=Color(0x660033, 1.0))
        super().__init__(asset, position)
        

class Lives(Sprite):

    def __init__(self, app, position):
        asset = TextAsset(app.lives, style="30pt Comic Sans", width=250, fill=Color(0x660033, 1.0))
        super().__init__(asset, position)
    
class End(Sprite):

    def __init__(self, app, position):
        asset = TextAsset('Game Over!', style="53pt Comic Sans", width=400, fill=Color(0x800000, 1.0))
        super().__init__(asset, position)

class Game(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        pic_asset = ImageAsset("images/backgroundexperiment.png", Frame(0, 0, 960, 672), 1, 'horizontal')
        linpic_asset = ImageAsset("images/Game_Background_701.jpg", Frame(0, 0, 1280, 640), 1, 'horizontal')
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        self.bg1 = Sprite(linpic_asset, (0,-60))
        self.bg2 = Sprite(linpic_asset, (1152,-60))
        self.bg1.scale = 0.9
        self.bg2.scale = 0.9
        Game.os = ObstacleS((0,369))
        Game.Pal = Person((Game.width/2,400))
        self.x = 0
        self.score = "Score: "+str(self.x)
        self.l = 5
        self.lives = "Lives: "+str(self.l)
        self.livprint = Lives(self, (Game.width-260,10))
        self.scorprint = Score(self, (10,10))
        self.steprun = 0
        self.sc = 0

    def step(self):
        if self.l > 0:
            for player in self.getSpritesbyClass(Person):
                player.step()
            if self.Pal.collidingWith(self.os) == False:
                self.sc += 1
            if self.Pal.collidingWith(self.os) == True:
                self.sc = 0
            if self.sc == 160:
                self.x += 1
                self.score = "Score: "+str(self.x)
                self.scorprint.destroy()
                self.scorprint = Score(self, (10,10))
                self.sc = 0
            if self.steprun == 0:
                if self.Pal.collidingWith(self.os) == True:
                    self.l -= 1
                    self.lives = "Lives: "+str(self.l)
                    self.livprint.destroy()
                    self.livprint = Lives(self, (Game.width-260,10))
                    self.steprun +=1
            else:
                self.steprun += 1
            if self.steprun == 16:
                self.steprun = 0
            self.bg1.x -= player.tv
            self.bg2.x -= player.tv
            if self.bg2.x >= 0:
                self.bg1.x = self.bg2.x-1152
            if self.bg1.x >= 0:
                self.bg2.x = self.bg1.x-1152
            if self.bg2.x <= 0:
                self.bg1.x = self.bg2.x+1152
            if self.bg1.x <= 0:
                self.bg2.x = self.bg1.x+1152
            for obs in self.getSpritesbyClass(ObstacleS):
                obs.step()
            if self.os.x and self.os.x > 2*Game.width:
                self.os.destroy()
                self.oss = ObstacleS((0,369))
            if self.os.x and self.os.x > 1.25*Game.width or self.os.x and self.os.x < -3*Game.width/4:
                self.os.destroy()
                self.os = ObstacleS((-3*Game.width/4+1,369))
        else:
            self.gameprint = End(self, (Game.width/2-200,Game.height/2))

Game().run()
'''class Textrunner(App):
    def __init__(self):
        super().__init__()
        Txt = TextAsset(Textrunner.prompts, style="30pt Times New Roman", width=400, fill=Color(0x000000, 1.0))
        self.listenKeyEvent("keydown", "enter", self.nxt)
        self.x = 0


    def nxt(self, event):
        for x in self.prompts:
            print(x)
            x = x+1

    def step(self):
        if self.x == 0:
            self.prompts = ("In car, gates in front block way forward. C to investigate car, G to investigate gate.")
            self.listenKeyEvent("keydown", "c", self.x=1)
            self.listenKeyEvent("keydown", "g", self.x=2)

        if self.x == 1:
            self.prompts = ("")
            self.x == 2:
        if self.x == 2:
            self.prompts = ("")
            self.x == 3:
        if self.x == 3:
            self.prompts = ("")
            self.x == 4:
        if self.x == 4:
            self.prompts = ("")
            self.x == 5:
        if self.x == 5:
            self.prompts = ("")
            self.x == 6:'''