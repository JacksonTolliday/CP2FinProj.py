from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset
import random

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
    def __init__(self):
        super().__init__()
        textbox = Color(0xFAF0E6, 1)
        dark = Color(0x2F4F4F, 1)
        line = LineStyle(2, dark)
        bg_asset = RectangleAsset(self.width-2, self.height/3-2, line, textbox)
        self.bg = Sprite(bg_asset, (0,(self.height/3)*2))
        self.score = "Press Enter to Continue"
        self.scorprint = Start(self, (self.width/2-200, self.height/1.28))
        self.flashlight = False
        self.jacket = False
        self.boxcheck = False
        self.trunkcheck = False
        self.carout = False
        self.carkeys = False
        self.ax = False
        self.keyring = False
        self.alerted = False
        self.randhmm = 0
        self.first()

    def refresh(self, x):
        self.score = x
        self.scorprint.destroy()
        self.scorprint = Score(self, (10,(Game.height/3)*2+5))

    def first(self):
        self.listenKeyEvent("keydown", "enter", self.enter)

    def enter(self, event):
        self.unlistenKeyEvent("keydown", "enter", self.enter)
        self.refresh("As your car limps along the roadway, through your weak, dying headlights you spot what looks like a metal gate on the horizon. It came into view just as your car falters in the chilly fall air, sputtering as it runs out of gas. You could have easily missed it this late at night, as the bushes around it hide it's frame well. It looks like it could possibly lead to a house? Your car creaks to a stop right outside of the gate, almost like it wants you to go looking around the gate for help. What do you do? Press C to look around your car, or G to investigate the gate.")
        self.listenKeyEvent("keydown", "c", self.car)
        self.listenKeyEvent("keydown", "g", self.gate)

    def car(self, event):
        self.unlistenKeyEvent("keydown", "c", self.car)
        self.refresh("You chose to look around your car. As you glance around, you can see some objects that you haphazardly left on the back seat, a jacket and a flashlight. You pick them up; it would probably be a good idea to bring them if you're going to go outside. You also think that you probably have something in the glove box or in the trunk. To look in your glovebox, press B. To look in your trunk, press T. To leave your car and investigate the gate, press G.")
        self.flashlight = True
        self.jacket = True
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "b", self.box)
        self.listenKeyEvent("keydown", "g", self.gate)

    def box(self, event):
        self.unlistenKeyEvent("keydown", "b", self.box)
        self.refresh("You quickly pop open the glovebox, checking to see if you have anything inside. You come back with a cellphone; great news, unless you consider the fact that it's a long dead flip-phone you've never seen before. Someone must've left it in this car before you rented it. Oh well, there's some papers, but nothing else useful. Do you take the flip-phone? Press Y to take it, and N to leave it be.")
        self.boxcheck = True
        self.listenKeyEvent("keydown", "y", self.flipye)
        self.listenKeyEvent("keydown", "n", self.flipno)

    def flipye(self, event):
        self.unlistenKeyEvent("keydown", "y", self.flipye)
        self.refresh("You grab the flip-phone; who knows, it might be useful. Press G to investigate the gate, press T to check the trunk.")
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "g", self.gate)

    def flipno(self, event):
        self.unlistenKeyEvent("keydown", "n", self.flipno)
        self.refresh("You leave the flip-phone; what use is carrying around an old piece of junk, it's just going to be another thing to keep track of. Press G to investigate the gate, press T to check the trunk.")
        self.listenKeyEvent("keydown", "t", self.trunk)
        self.listenKeyEvent("keydown", "g", self.gate)

    def trunk(self, event): #extend... what if they are returning?
        self.unlistenKeyEvent("keydown", "t", self.trunk)
        if self.carout == False:
            self.refresh("You hop out the car, slamming the door behind you. It's bitterly cold out, and you're glad you grabbed your jacket. However, as you walk around to the trunk of your car and pull the handle, the trunk doesn't budge. When you head back around to the door you just got out of, it doesn't budge either. You realize that you left your keys in the car; you're locked out. With only one way left to go, as you don't want to freeze to death out in the middle of nowhere, you head towards the gate. Press Enter to continue.")
            self.carout = True
            self.listenKeyEvent("keydown", "enter", self.gate)
        else:
            self.refresh("You pop open the trunk, glancing around the back of the trunk. You can see a Wood Ax; who knows where that came from... who was the last person who rented this car? You pick it up, noticing what you hope is red paint spattered along it. You also see keyring, with tons of jumbled keys on it; looks like it had an ID tag on it too, but who knows what the name on it was: it looks as if it was worn off long ago. Press A to take the Ax, press K to take the keyring, or press X to take both.")
            self.listenKeyEvent("keydown", "x", self.axkey)
            self.listenKeyEvent("keydown", "a", self.axs)
            self.listenKeyEvent("keydown", "k", self.keyrings)
    def axs(self, event):
        self.unlistenKeyEvent("keydown", "a", self.axs)
        self.ax = True
        self.refresh("You snag the ax, and carry it off towards the gate. Press G to continue to the gate.")
        self.listenKeyEvent("keydown", "g", self.gate)
    def keyrings(self, event):
        self.unlistenKeyEvent("keydown", "k", self.keyrings)
        self.keyring = True
        self.refresh("You snag the keys, stuff them in a pocket, and walk off towards the gate. Press G to continue to the gate.")
        self.listenKeyEvent("keydown", "g", self.gate)
    def axkey(self, event):
        self.unlistenKeyEvent("keydown", "x", self.axkey)
        self.keyring = True
        self.ax = True
        self.refresh("You snag the ax and the keys, stuffing the keys in a pocket and carring off the ax towards the gate. Press G to continue to the gate.")
        self.listenKeyEvent("keydown", "g", self.gate)

    def gate(self, event):
        self.unlistenKeyEvent("keydown", "g", self.gate)
        if self.carout == False:
            if self.jacket == False:
                self.refresh("As you're leaving the car, you quickly grab the keys from the ignition; you don't want to leave these behind. You head up towards the gate, shivering against the bitter Autumn wind. If only you remembered your jacket.. Oh well. Even though the gate's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. You could also head back to your car and check the trunk, maybe you've got something there to help. Press T to check the trunk, B to try the buzzer, or L to look for another way in.")
                self.carkeys = True
                self.carout = True
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
                self.listenKeyEvent("keydown", "t", self.trunk)
            else:
                self.refresh("As you're leaving the car, you quickly grab the keys from the ignition; you don't want to leave these behind. You head up towards the gate, noticing the grass curling ominously against it's dull brass frame. Even though it's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. You could also head back to your car and check the trunk, maybe you've got something there to help. Press T to check the trunk, B to try the buzzer, or L to look for another way in.")
                self.carkeys = True
                self.carout = True
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
                self.listenKeyEvent("keydown", "t", self.trunk)
        else:
            if self.jacket == False:
                self.refresh("You head towards the gate, shivering against the bitter Autumn wind. If only you remembered your jacket.. Oh well. Even though the gate's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. Press B to try the buzzer, or L to look for another way in.")
                self.carkeys = True
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)
            else:
                self.refresh("You head towards the gate, noticing the grass curling ominously against it's dull brass frame. Even though it's old, ornate look looks like something out of an old mansion, you notice a buzzer; maybe to call up to open the gate. You could also look around for another way in; who knows if the buzzer even works. Press B to try the buzzer, or L to look for another way in.")
                self.carkeys = True
                self.listenKeyEvent("keydown", "l", self.c)
                self.listenKeyEvent("keydown", "b", self.buzzer)

    def c(self, event):
        self.unlistenKeyEvent("keydown", "l", self.c)
        if self.ax == True and self.keyring == True:
            self.refresh("You walk around the gate, looking to the right and left. You notice the hinges look brittle; the gate looks old enough that if you hit it hard enough, it might just fall over. There's also a well hidden keyhole under the buzzer; barely visible, but definitely there. I mean, who knows? Maybe you could try one of the keys on the massive keyring you found; it might work... then again, you could keep looking for a way in along the fence extending on either side of the gate. Press K to try a key on the lock, U to try and snap the gate's hinges with your bare hands, A to try and break the gate's hinges with the Ax, and I to keep looking along the fence.")
            self.listenKeyEvent("keydown", "k", self.keytrial) #extend
            self.listenKeyEvent("keydown", "u", self.barebreak)
            self.listenKeyEvent("keydown", "a", self.axbreak) #extend
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend
        if self.ax == True:
            self.refresh("You walk around the gate, looking to the right and left. You notice the hinges look brittle; the gate looks old enough that if you hit it hard enough, it might just fall over. There's also a well hidden keyhole under the buzzer; barely visible, but definitely there. You don't have any keys though... then again, you could keep looking for a way in along the fence extending on either side of the gate. Press U to try and snap the gate's hinges with your bare hands, A to try and break the gate's hinges with the Ax, and I to keep looking along the fence.")
            self.listenKeyEvent("keydown", "u", self.barebreak)
            self.listenKeyEvent("keydown", "a", self.axbreak) #extend
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend
        if self.keyring == True: 
            self.refresh("You walk around the gate, looking to the right and left. You notice the hinges look brittle; the gate looks old enough that if you hit it hard enough, it might just fall over. There's also a well hidden keyhole under the buzzer; barely visible, but definitely there. I mean, who knows? Maybe you could try one of the keys on the massive keyring you found; it might work... then again, you could keep looking for a way in along the fence extending on either side of the gate. Press K to try a key on the lock, U to try and snap the gate's hinges, and I to keep looking along the fence.")
            self.listenKeyEvent("keydown", "k", self.keytrial) #extend
            self.listenKeyEvent("keydown", "u", self.barebreak)
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend
        if self.ax == False and self.keyring == False:
            self.refresh("You walk around the gate, looking to the right and left. You notice the hinges look brittle; the gate looks old enough that if you hit it hard enough, it might just fall over. There's also a well hidden keyhole under the buzzer; barely visible, but definitely there. You don't have any keys though... then again, you could keep looking for a way in along the fence extending on either side of the gate. Press U to try and snap the gate's hinges, and I to keep looking along the fence.")
            self.listenKeyEvent("keydown", "u", self.barebreak)
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend

    def buzzer(self, event):
        self.unlistenKeyEvent("keydown", "b", self.buzzer)
        if self.carkeys == True:
            self.refresh("You hold down the buzzer, leaning forward to what looks like a microphone, but before you can speak, the mic crackles loudly, interrupting you. The crackling continues for a few seconds, but then shuts off. The gate makes a weak whining noise, and it creaks open, just enough for you to push yourself through sideways. I mean it opened, but it did strike you as more than a little ominous... Press T to continue through the gate, press i to look around for another way in, or press C to return to your car.")
            self.alerted = True
            self.listenKeyEvent("keydown", "t", self.throughgate)
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend
            self.listenKeyEvent("keydown", "c", self.carreturn)
        else:
            self.refresh("You hold down the buzzer, leaning forward to what looks like a microphone, but before you can speak, the mic crackles loudly, interrupting you. The crackling continues for a few seconds, but then shuts off. The gate makes a weak whining noise, and it creaks open, just enough for you to push yourself through sideways. I mean it opened, but it did strike you as more than a little ominous... Press T to continue through the gate, press i to look around for another way in.")
            self.alerted = True
            self.listenKeyEvent("keydown", "t", self.throughgate)
            self.listenKeyEvent("keydown", "i", self.moreinvest) #extend

    def throughgate(self, event):
        self.unlistenKeyEvent("keydown", "t", self.throughgate)
        self.refresh("You press against the gate, shoving yourself through it. It's a tight squeeze, but you push yourself through, stumbling out on the other side. However, the pressure you put on the gate must've been too much for it, as it falls closed behind you. END OF CHAPTER 1")

    def carreturn(self, event):
        self.unlistenKeyEvent("keydown", "c", self.carreturn)
        self.refresh("As you turn around to look around your car a bit more - maybe you'll find something else helpful - you realize your car is gone. It doesn't make any sense; it was just there! It couldn't have gone anywhere either, you distinctly remember putting it in park. Even if someone came along and stole it, you would've heard it... Well, now there's nowhere else to go but through the gate. END OF CHAPTER 1")

    def barebreak(self, event):
        self.unlistenKeyEvent("keydown", "u", self.throughgate)
        if self.ax == True and self.keyring == True:
            self.refresh("As you slam you hands against the old gate, the best you can do is get a high squeal from the hinges: they don't look like they're budging anytime soon. Oh well, it did seem unlikely that you'd be able to brute force it that way. Press I to try and find another way in, press K to try one of the keys you have on your keyring, or press A to try and break the gate down with your axe.")
            self.listenKeyEvent("keydown", "k", self.keytrial)
            self.listenKeyEvent("keydown", "a", self.axbreak)
            self.listenKeyEvent("keydown", "i", self.moreinvest)
        if self.ax == True:
            self.refresh("As you slam you hands against the old gate, the best you can do is get a high squeal from the hinges: they don't look like they're budging anytime soon. Oh well,  it did seem unlikely that you'd be able to brute force it that way. Press I to try and find another way in or press A to try and break the gate down with your axe.")
            self.listenKeyEvent("keydown", "a", self.axbreak)
            self.listenKeyEvent("keydown", "i", self.moreinvest)
        if self.keyring == True: 
            self.refresh("As you slam you hands against the old gate, the best you can do is get a high squeal from the hinges: they don't look like they're budging anytime soon. Oh well,  it did seem unlikely that you'd be able to brute force it that way. Press I to try and find another way in or press K to try one of the keys you have on your keyring.")
            self.listenKeyEvent("keydown", "k", self.keytrial)
            self.listenKeyEvent("keydown", "i", self.moreinvest)
        if self.ax == False and self.keyring == False:
            self.refresh("As you slam you hands against the old gate, the best you can do is get a high squeal from the hinges: they don't look like they're budging anytime soon. Oh well, it did seem unlikely that you'd be able to brute force it. Press I to try and find another way in.")
            self.listenKeyEvent("keydown", "i", self.moreinvest)

    def keytrial(self, event):
        self.unlistenKeyEvent("keydown", "k", self.keytrial)
        self.randhmm = random.randint(0,13)
        if self.randhmm == 13:
            self.refresh("You try a key from the keyring you found... miraculously, it fits! Who'd have guessed that you had the key to the gate all along! Apparently you. The Gate creaks open, and you start up the long winding path towards whatever it kept hidden. END OF CHAPTER 1")
        else:
            if self.ax == True:
                self.refresh("You try a key from the keyring you found... and surprising no one, it doesn't work. You turn in a couple times, but the key gains no purchase and you're stuck where you were. You can still try another key by pressing K, Press I to try and find another way in, or press A to try and break the gate down with your axe. ")
                self.listenKeyEvent("keydown", "k", self.keytrial)
                self.listenKeyEvent("keydown", "a", self.axbreak)
                self.listenKeyEvent("keydown", "i", self.moreinvest)
            else:
                self.refresh("You try a key from the keyring you found... and surprising no one, it doesn't work. You turn in a couple times, but the key gains no purchase and you're stuck where you were. You can still try another key by pressing K, or Press I to try and find another way in.")
                self.listenKeyEvent("keydown", "k", self.keytrial)
                self.listenKeyEvent("keydown", "i", self.moreinvest)

    def axbreak(self, event):
        self.unlistenKeyEvent("keydown", "a", self.axbreak)
        self.refresh("The Gate screeches as you bring the axe down onto the gate, rattling encouragingly. After a few more strokes, the gate crashes down. The open path lies ahead of you. END OF CHAPTER 1")

    def moreinvest(self, event):
        self.unlistenKeyEvent("keydown", "i", self.moreinvest)
        if self.ax == True and self.keyring == True:
            self.refresh("As you look around the sides of the gate, you see where the gate turns from ornate steel into rusting chainlink. As it disintegrates, more and more holes appear in the fence, and eventually you find one big enough to fit through. Press O to climb through the hole, press K to try one of the keys you have on your keyring, or press A to try and break the gate down with your axe.")
            self.listenKeyEvent("keydown", "k", self.keytrial)
            self.listenKeyEvent("keydown", "a", self.axbreak)
            self.listenKeyEvent("keydown", "o", self.throughfence)
        if self.ax == True:
            self.refresh("As you look around the sides of the gate, you see where the gate turns from ornate steel into rusting chainlink. As it disintegrates, more and more holes appear in the fence, and eventually you find one big enough to fit through. Press O to climb through the hole or press A to try and break the gate down with your axe.")
            self.listenKeyEvent("keydown", "a", self.axbreak)
            self.listenKeyEvent("keydown", "o", self.throughfence)
        if self.keyring == True:
            self.refresh("As you look around the sides of the gate, you see where the gate turns from ornate steel into rusting chainlink. As it disintegrates, more and more holes appear in the fence, and eventually you find one big enough to fit through. Press O to climb through the hole or press K to try one of the keys you have on your keyring.")
            self.listenKeyEvent("keydown", "k", self.keytrial)
            self.listenKeyEvent("keydown", "o", self.throughfence)
        if self.keyring == True:
            self.refresh("As you look around the sides of the gate, you see where the gate turns from ornate steel into rusting chainlink. As it disintegrates, more and more holes appear in the fence, and eventually you find one big enough to fit through. Press O to climb through the hole or press K to try one of the keys you have on your keyring. You've got nowhere else to go but forward... so you head through the hole in the fence. END OF CHAPTER 1")

    def throughfence(self, event):
        self.unlistenKeyEvent("keydown", "o", self.throughfence)
        self.refresh("You decide you've got nowhere else to go but forward... so you head through the hole in the fence. END OF CHAPTER 1")

Game().run()