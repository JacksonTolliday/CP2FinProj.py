from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Textrunner(App):
    def __init__(self):
        super().__init__()
        Txt = TextAsset
        self.listenKeyEvent("keydown", "enter", self.nxt)
        
    def nxt:
        for x in prompts:
            print(x)
            x = x+1
