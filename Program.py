from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Text(Sprite):

    def __init__(self, app, position):
        global Game
        asset = TextAsset(app.text, style="15pt Times New Roman", width=Game.width-20, fill=Color(0x000000, 1.0))
        super().__init__(asset, position)
        

class Lives(Sprite):

    def __init__(self, app, position):
        asset = TextAsset(app.lives, style="15pt Comic Sans", width=250, fill=Color(0x000000, 1.0))
        super().__init__(asset, position)
    
class End(Sprite):

    def __init__(self, app, position):
        asset = TextAsset('Game Over!', style="53pt Times New Roman", width=400, fill=Color(0x000000, 1.0))
        super().__init__(asset, position)

class Game(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        self.text = ""
        self.livprint = Lives(self, (Game.width-260,10))
        self.textprint = Text(self, (10,Game.height-150))

    def start(self):
        self.text = "c or g?"
        self.listenKeyEvent("keydown", "c", self.c1)
        self.listenKeyEvent("keydown", "g", self.g1)

    def c1(self):
        self.text = "c"
    def g1(self):
        self.text = "g"
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