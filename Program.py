from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

def Textrunner(App):
    def __init__(self):
        Txt = TextAsset
        super().__init__()
        self.listenKeyEvent("keydown", "enter", self.nxt)
        
    def nxt:
        for x in prompts:
            print(x)
            x = x+1
