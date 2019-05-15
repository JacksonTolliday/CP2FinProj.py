from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Textrunner(App):
    def __init__(self):
        super().__init__()
        Txt(x) = TextAsset(x, style="53pt Comic Sans", width=400, fill=Color(0x800000, 1.0))
        self.listenKeyEvent("keydown", "enter", self.nxt)
        

    def nxt:
        for x in prompts:
            print(x)
            x = x+1
