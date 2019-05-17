from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Start(Sprite):
    def __init__(self, app, position):
        global Game
        asset = TextAsset(app.score, style="30pt Times New Roman", width=Game.width, fill=Color(0x000000, 1.0))
        super().__init__(asset, position)

class Score(Sprite):
    def __init__(self, app, position):
        global Game
        asset = TextAsset(app.score, style="15pt Times New Roman", width=Game.width-10, fill=Color(0x000000, 1.0))
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
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        self.score = "Press Enter to Continue"
        self.scorprint = Start(self, (Game.width/2-200,Game.height/2))
        self.flashlight = False
        self.jacket = False
        self.boxcheck = False
        self.trunkcheck = False
        self.carout = False
        self.carkeys = False
        self.ax = False
        self.keyring = False
        self.first()

    def step(self):
        pass

    def first(self):
        self.listenKeyEvent("keydown", "enter", self.enter)

    def enter(self, event):
        self.score = "As your car sputters in the chilly fall air, sputtering as it runs out of gas without a station for at least the next 20 miles. You spot a old, rusty gate on the horizon through your dying headlights. You could have easily missed it this late at night, as the bushes around it hide it well. It looks like it could possibly lead to a house? Your car creaks to a stop right outside of the gate, almost like it wants you to go looking around the gate for help. What do you do? Press C to look around your car, or G to investigate the gate."
        self.scorprint.destroy()
        self.scorprint = Score(self, (10,Game.height-150))
        self.listenKeyEvent("keydown", "c", self.car)
        self.listenKeyEvent("keydown", "g", self.gate)

    def car(self, event):
        self.score = "You chose to look around your car. As you glance around, you can see some objects that you haphazardly left on the back seat, a jacket and a flashlight. You pick them up; it would probably be a good idea to bring them if you're going to go outside. You also think that you probably have something in the glove box or in the trunk. To look in your glovebox, press B. To look in your trunk, press T. To leave your car and investigate the gate, press G."
        self.flashlight = True
        self.jacket = True
        self.scorprint.destroy()
        self.scorprint = Score(self, (10,Game.height-150))
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "b", self.box)
        self.listenKeyEvent("keydown", "g", self.gate)

    def box(self, event):
        self.score = "You quickly pop open the glovebox, checking to see if you have anything inside. You come back with a cellphone; great news, unless you consider the fact that it's a long dead flip-phone you've never seen before. Someone must've left it in this car before you rented it. Oh well, there's some papers, but nothing else useful. Do you take the flip-phone? Press Y to take it, and N to leave it be."
        self.scorprint.destroy()
        self.boxcheck = True
        self.scorprint = Score(self, (10,Game.height-150))
        self.listenKeyEvent("keydown", "y", self.flipye)
        self.listenKeyEvent("keydown", "n", self.flipno)

    def flipye(self, event):
        self.score = "You grab the flip-phone; who knows, it might be useful. Press G to investigate the gate, press T to check the trunk."
        self.scorprint.destroy()
        self.scorprint = Score(self, (10,Game.height-150))
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "g", self.gate)

    def flipno(self, event):
        self.score = "You leave the flip-phone; what use is carrying around an old hunk of junk, it's just going to be another thing to keep track of. Press G to investigate the gate, press T to check the trunk."
        self.scorprint.destroy()
        self.scorprint = Score(self, (10,Game.height-150))
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "g", self.gate)

    def trunk(self, event):
        if self.carout == False:
            self.score = "You hop out the car, slamming the door behind you. It's bitterly cold out, and you're glad you grabbed your jacket. However, as you walk around to the trunk of your car and pull the handle, the trunk doesn't budge. When you head back around to the door you just got out of, it doesn't budge either. You realize that you left your keys in the car; you're locked out. With only one way left to go, as you don't want to freeze to death out in the middle of nowhere, you head towards the gate. Press Enter to continue."
            self.carout = True
            self.scorprint.destroy()
            self.scorprint = Score(self, (10,Game.height-150))
            self.listenKeyEvent("keydown", "enter", self.gate)
        else:
            self.score = "You pop open the trunk, glancing around the back of the trunk. You can see a Wood Ax; who knows where that came from... who was the last person who rented this car? You pick it up, noticing what you hope is red paint spattered along it. You also see keyring, with tons of jumbled keys on it; looks like it had an ID tag on it too, but who knows what the name on it was: it looks as if it was worn off long ago. Press A to take the Ax, press K to take the keyring, or press B to take both."
            self.scorprint.destroy()
            self.scorprint = Score(self, (10,Game.height-150))
            self.listenKeyEvent("keydown", "b", self.axkey)
            self.listenKeyEvent("keydown", "a", self.axs)
            self.listenKeyEvent("keydown", "k", self.keyrings)
    def axs(self, event):
        self.ax = True
        self.gate()
    def keyrings(self, event):
        self.keyring = True
        self.gate()
    def axkey(self, event):
        self.keyring = True
        self.ax = True
        self.gate()

    def gate(self, event):
        if self.carout == False:
            if self.jacket == False:
                self.score = "As you're leaving the car, you quickly grab the keys from the ignition; you don't want to leave these behind. You head up towards the gate, shivering against the bitter Autumn wind. If only you remembered your jacket.. Oh well. Even though the gate's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. You could also head back to your car and check the trunk, maybe you've got something there to help. Press T to check the trunk, B to try the buzzer, or L to look for another way in."
                self.carkeys = True
                self.carout = True
                self.scorprint.destroy()
                self.scorprint = Score(self, (10,Game.height-150))
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
                self.listenKeyEvent("keydown", "t", self.trunk)
            else:
                self.score = "As you're leaving the car, you quickly grab the keys from the ignition; you don't want to leave these behind. You head up towards the gate, noticing the grass curling ominously against it's dull brass frame. Even though it's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. You could also head back to your car and check the trunk, maybe you've got something there to help. Press T to check the trunk, B to try the buzzer, or L to look for another way in."
                self.carkeys = True
                self.carout = True
                self.scorprint.destroy()
                self.scorprint = Score(self, (10,Game.height-150))
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
                self.listenKeyEvent("keydown", "t", self.trunk)
        else:
            if self.jacket == False:
                self.score = "You head towards the gate, shivering against the bitter Autumn wind. If only you remembered your jacket.. Oh well. Even though the gate's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. Press B to try the buzzer, or L to look for another way in."
                self.carkeys = True
                self.scorprint.destroy()
                self.scorprint = Score(self, (10,Game.height-150))
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
            else:
                self.score = "You head towards the gate, noticing the grass curling ominously against it's dull brass frame. Even though it's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. Press B to try the buzzer, or L to look for another way in."
                self.carkeys = True
                self.scorprint.destroy()
                self.scorprint = Score(self, (10,Game.height-150))
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)

    def c(self, event):
        if self.ax == True or self.keyring == True:
            
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