from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Score(Sprite):

    def __init__(self, app, position):
        global Game
        asset = TextAsset(app.score, style="15pt Times New Roman", width=Game.width-20, fill=Color(0x000000, 1.0))
        super().__init__(asset, position)
        
    
class End(Sprite):

    def __init__(self, app, position):
        asset = TextAsset('Game Over!', style="53pt Times New Roman", width=400, fill=Color(0x000000, 1.0))
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
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        self.x = ""
        self.score = ""+str(self.x)
        self.strt = 0
        self.scorprint = Score(self, (10,Game.height-150))

    def start(self):
        if self.strt == 0:
            self.x = "c or g?"
            self.listenKeyEvent("keydown", "c", self.c1)
            self.listenKeyEvent("keydown", "g", self.g1)
            self.strt = 1

    def c1(self):
        if self.strt == 1:
            self.x = "c. t or r?"

    def g1(self):
        if self.strt == 1:
            self.x = "g. h or j?"

Game().run()
'''
HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

class Textrunner(App):
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