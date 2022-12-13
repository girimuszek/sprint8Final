import time

def addRebarToInventory(rebar):
    rebar += 1
    return rebar

def officeScene3():
    directions = ["continue hiding","run out from cover and flee"]
    start3Inputs= {
        'officeScene3Msg1' : "It'll only be a matter of time until they find you",
        'officeScene3Actions' : "Actions: continue hiding | run out from cover and flee =>",
        'officeScene3Hide1' : "As you continue to hide, the footsteps just keep getting closer and closer, until eventually, two boots stand directly in front of you,",
        'officeScene3Hide2' : "and the person who the boots belong to, crouch down and immediatly retreat a few steps as they notice you, gun pointed.",
        'officeScene3Hide3' : "To be continued (Hopefully)",
        'officeScene3Run1' : "Flight seemed to be your only choice left, so regardless of whether or not your ",
        'officeScene3Run2' : "odds of survival were high or low, you took the chance and ran.",
        'officeScene3Run3' : "To be continued (Hopefully)"
    }

    for c in start3Inputs['officeScene3Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['officeScene3Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "continue hiding":
            for c in start3Inputs['officeScene3Hide1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene3Hide2']:
                print(c,end="")
                time.sleep(0.025)
            print()
            print()
            for c in start3Inputs['officeScene3Hide3']:
                print(c,end="")
                time.sleep(0.025)
            print()
            print()
            start(0)
            
        elif userInput == "run out from cover and flee":
        
            for c in start3Inputs['officeScene3Run1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene3Run2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene3Run3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(0)
        else: 
            print("Please enter a valid action.")  

def officeScene2():
    directions = ["hide under desk","show your hands when they come in"]
    start3Inputs= {
        'officeScene2Msg1' : "Because you peered out the window, you were able to get a good warning about things to come, so you have an advantage about what to do!",
        'officeScene2Actions' : "Actions: hide under desk | show your hands when they come in =>",
        'officeScene2Hide1' : "You quickly slide under a desk, and moments later, they come into the room.",
        'officeScene2Hide2' : "1: *There shouldn't be any prisoners here, they've been taken a while ago, we're just wasting our time!*",
        'officeScene2Hide3' : "2: *Alright in that case, just grab anything that looks imporant and lets, leave immediatly!",
        'officeScene2Hide4' : "As the footsteps die down, you come out from under the desk with a look of relief on your face.",
        'officeScene2Hide5' : "The conflict is over, but there is so much more left to do to get out of here. ",
        'officeScene2Hide6' : "TO BE CONTINUED (HOPEFULLY)",
        'officeScene2Show1' : "You take a massive gamble and with a lot of hesitation, instead of hiding, you stand still and quickly raise your hands ",
        'officeScene2Show2' : "as high as they physically. A minute later, the door to the office opens up, and you're suddenly face to face ",
        'officeScene2Show3' : "with three armed individuals.",
        'officeScene2Show4' : "To be continued (Hopefully)",
    }

    for c in start3Inputs['officeScene2Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['officeScene2Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "hide under desk":
            for c in start3Inputs['']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene2Hide1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene2Hide2']:
                print(c,end="")
                time.sleep(0.025)
            print()
            print()
            for c in start3Inputs['officeScene2Hide3']:
                print(c,end="")
                time.sleep(0.025)
            print()
            print()
            for c in start3Inputs['officeScene2Hide4']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene2Hide5']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene2Hide6']:
                print(c,end="")
                time.sleep(0.035)
            start(0)
            
        elif userInput == "show your hands when they come in":
        
            for c in start3Inputs['officeScene2Show1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene2Show2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene2Show3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(0)
        else: 
            print("Please enter a valid action.")  

def officeScene1():
    directions = ["hide under desk","show your hands when they come in"]
    start3Inputs= {
        'officeScene1Actions' : "Actions: hide under desk | show your hands when they come in =>",
        'officeScene1Hide1' : "You chose to hide, and in doing so, you accidentally knock over a box with manilla folders inside, spilling the contents out on the floors as you go ",
        'officeScene1Hide2' : "under one of the desks.",
        'officeScene1Hide3' : "When the boots step into the office, they immediatly notice the spilled manilla folders in the otherwise tidy office.",
        'officeScene1Hide4' : "They immediatly approach the location and start looking under the desks one by one.",
        'officeScene1Show1' : "Because you didn't expect the guards to arrive, when you put your hands up, ",
        'officeScene1Show2' : "you were immediatly fired upon what was assumed to be an enemy combatant",
        'officeScene1Show3' : "In your final moments, you felt as if time was going backwards...",
    }

    for c in start3Inputs['officeScene1Actions']:
            print(c,end="")
            time.sleep(0.05)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "hide under desk":
            print()
            print()
            for c in start3Inputs['officeScene1Hide1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene1Hide2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene1Hide3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene1Hide4']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            officeScene3()
            
        elif userInput == "show your hands when they come in":
        
            for c in start3Inputs['officeScene1Show1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['officeScene1Show2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['officeScene1Show3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(0)
        else: 
            print("Please enter a valid action.")  

def office1():
    directions = ["explore inside","look outside of window"]
    start3Inputs= {
        'office1Msg1' : "The cellroom directly connects to some sort of office. Still doesn't explain why you're here in the first place.",
        'office1Msg2' : "The office area doesn't look abandoned, which is both a relief and a worry since you still don't understand why you were imnprisoned in the first place.",
        'office1Actions' : "Actions: explore inside | look outside of window =>",
        'office1Explore1' : "As you're looking around for any useful information about the location, you start to hear people coming to you, and as ",
        'office1Explore2' : "the footsteps approaching closer and closer. You think what to do next.",
        'office1Window1' : "As you peer outside another window, you quickly notice that you're on the second story of the building, and that just below you,",
        'office1Window2' : "various people with firearms, likely guards or other officials are quickly going through the enterance. You only have mere moments to decide on what",
        'office1Window3' : "to do next!"
    }

    for c in start3Inputs['office1Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['office1Msg2']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['office1Actions']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "explore inside":
            for c in start3Inputs['office1Explore1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['office1Explore2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            officeScene1()
            
        elif userInput == "look outside of window":
        
            for c in start3Inputs['office1Window1']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['office1Window2']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['office1Window3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            officeScene2()
        else: 
            print("Please enter a valid action.")  

def conflict1(rebar):
    directions = ["fight back normally","use rebar as a weapon"]
    start3Inputs= {
        'conflict1Msg1' : "As he's attacking, you realise quickly that he is stronger and that it's only a matter of time until he overpowers you! ",
        'conflict1Actions' : "Actions: fight back | use rebar as a weapon =>",
        'conflict1Normal' : "With only your fists and feet and without a weapon, you stand no chance as the man overpowers you.",
        'conflict1Normal2' : "As you start to lose consciousness, you start to feel as if you're going back in time...",
        'conflict1Rebar1' : "As the mysterious man is grabbing to tackle you to the ground, you remember about the rebar and use it to hit the man once in the head",
        'conflict1Rebar2' : "After standing up and recovering from the attack, you wonder whether the man is unconscious or dead. But at this point,",
        'conflict1Rebar3' : "it doesn't even matter anymore. You run as fast as you can out of the hallway and into the next room."
    }

    for c in start3Inputs['conflict1Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['conflict1Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "fight back normally":
            for c in start3Inputs['conflict1Normal']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['conflict1Normal2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            rebar = 0
            start(rebar)
        elif userInput == "use rebar as a weapon":
        
            for c in start3Inputs['conflict1Rebar1']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['conflict1Rebar2']:
                print(c,end="")
                time.sleep(0.035)
            for c in start3Inputs['conflict1Rebar3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            office1()
        else: 
            print("Please enter a valid action.")  

def conflict2(rebar):
    directions = ["fight back","try to reason"]
    start3Inputs= {
        'conflict2Msg1' : "As he's attacking, you realise quickly that he is stronger and that it's only a matter of time until he overpowers you!",
        'conflict2Actions' : "Actions: fight back | try to reason =>",
        'conflict2FightBack' : "With only your fists and feet and without a weapon, you stand no chance as the man overpowers you.",
        'conflict2FightBack2' : "As you start to lose consciousness, you start to feel as if you're going back in time",
        'conflict2Reason1' : "As the mysterious man is doing his best to kill you, you attempt to reason with him",
        'conflict2Reason2' : "Unfortunately, although you tried to be a pacifist, there was nothing behind the eyes of the man as he",
        'conflict2Reason3' : "overpowers you. You feel as though you're going back in time..."
    }

    for c in start3Inputs['conflict2Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['conflict2Actions']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "fight back":
            for c in start3Inputs['conflict2FightBack']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['conflict2FightBack2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(rebar)
        elif userInput == "try to reason":
        
            for c in start3Inputs['conflict2Reason1']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['conflict2Reason2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['conflict2Reason3']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(rebar)
        else: 
            print("Please enter a valid action.")            
            
def rebarPossibility(rebar):
    rebar = addRebarToInventory(rebar)
    if rebar >= 1:
        conflict1(rebar)
    else: 
        conflict2(rebar)

def hallway1(rebar):
    directions = ["ignore","open cell"]
    start3Inputs= {
        'hallway1Msg1' : "The long hallway ends with an open door at the end, and as you aproach the door, ",
        'hallway1Msg2' : "a mans voice from one of the cells to your right calls out to you: 'There are keys to the cells in the room next to you! Please get me out of here! I've been here for far too long!",
        'hallway1Actions' : "Actions: ignore | open cell =>",
        'hallway1Ignore' : "Deep down in your gut, you feel something off about this as you stare him in the eyes, so you do your best to ignore his yells and go through the open door. ",
        'hallway1OpenCell' : "You retrieve the key from the room, which likely belonged to the guards that ran this facility.",
        'hallway1OpenCell2' : "The moment you use the key to open the cell door an inch, you immediatly get tackled by the man ",
    }

    for c in start3Inputs['hallway1Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['hallway1Msg2']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['hallway1Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "ignore":
            for c in start3Inputs['hallway1Ignore']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            office1()
        elif userInput == "open cell":
        
            for c in start3Inputs['hallway1OpenCell']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            for c in start3Inputs['hallway1OpenCell2']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            rebarPossibility(0)
            
        else: 
            print("Please enter a valid action.")

def start7():

    directions = ["give up"]
    start3Inputs= {
        'start7Msg1' : "No doors, no windows, no mattress, no story. Congratulations, you deserved it!",
        'start7Actions' : "Actions: give up =>",
        'start7GiveUp' : "With no where left to go, you collapse on the cold concrete and idle around for all of eternity.",
    }

    for c in start3Inputs['start7Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['start7Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "give up":
            for c in start3Inputs['start7GiveUp']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start(0)
        else: 
            print("Please enter a valid action.")

def start6(rebar):
    directions = ["door","sleep"]
    start3Inputs= {
        'start6Msg1' : "See? Now that there's no more window to look through, you now have no way to defy me :)",
        'start6Actions' : "Actions: door | sleep =>",
        'start6Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'start6Sleep' : "*Sigh*, you know what? This is the final straw for you... I'm genuinley sick of you. You must be sick of me too if you don't want to play this game that I spent so much time working on. So have fun now. "

    }

    for c in start3Inputs['start6Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['start6Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "door":
            for c in start3Inputs['start6Door']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        elif userInput == "sleep":
        
            for c in start3Inputs['start6Sleep']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start7(rebar)
        else: 
            print("Please enter a valid action.")
            
def start5(rebar):
    directions = ["door","window"]
    start3Inputs= {
        'start5Msg1' : "As the narrator and creator of this story, I ORDER YOU TO ENTER THROUGH THE DOOR.",
        'start5Actions' : "Actions: door | window =>",
        'start5Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'start5Window' : "Ok you know what? You want to play this game with me? I'll tell you what, how about from this point on, there won't be any more windows for you! "

    }

    for c in start3Inputs['start5Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['start5Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "door":
            for c in start3Inputs['start5Door']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        elif userInput == "window":
        
            for c in start3Inputs['start5Window']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start6(rebar)
        else: 
            print("Please enter a valid action.")

def start4(rebar):
    directions = ["door","window"]
    start3Inputs= {
        'start4Msg1' : "You should really look beyond that door. Seriously, there's nothing out beyond the window!",
        'start4Actions' : "Actions: door | window =>",
        'start4Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'start4Window' : "Ok please, I'm begging you. Stop looking out that window!"

    }

    for c in start3Inputs['start4Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['start4Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "door":
            for c in start3Inputs['start4Door']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        elif userInput == "window":
        
            for c in start3Inputs['start4Window']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start5(rebar)
        else: 
            print("Please enter a valid action.")

def start3(rebar):
    directions = ["door","window"]
    start3Inputs= {
        'start3Msg1' : "You can go out to stare out the window again, or you could see what's beyond the door. ",
        'start3Actions' : "Actions: door | window =>",
        'start3Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'start3Window' : "You stare out the window again. Nothing has changed. Standing and staring outside won't tell you why you are where you are"
     }

    for c in start3Inputs['start3Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in start3Inputs['start3Actions']:
            print(c,end="")
            time.sleep(0.035)

    userInput = ""
    while userInput not in directions:
        
        userInput = input()
        if userInput == "door":
            for c in start3Inputs['start3Door']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        elif userInput == "window":
        
            for c in start3Inputs['start3Window']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start4(rebar)
        else: 
            print("Please enter a valid action.")

def start2Win(rebar):
    rebar = 0
    directions = ["door","window","sleep"]
    startInputs = {
        'startMsg1' :"You finish looking out of the window and go back to the middle of the room.",
        'start1Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'Actions' : "Actions: door | window | sleep =>",
        'windowOutput' : "The window in of itself is not that interesting. You feel a need to leave the window, but for some reason, it attracts you further and further.",
        'sleep1' : "You decide to go back to sleep on your mattress.",
        'sleep2' : "You wake up again. Nothing changes, however as you look up, you notice a loose piece of iron rebar sticking out of the concrete.",
        'sleep3' : "You pull on the rebar, and as it is released from the wall, so does a lot of dust and small pebbles, which cover you. ",
        'uGotRebar' : "[] You got rebar! []",
        'haveRebar' : "Now is not the time to sleep. Get up!",
        'start1Actions' : "Actions: door | window | sleep =>"
    }
    
    
    for c in startInputs['startMsg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in startInputs['start1Actions']:
            print(c, end="")
            time.sleep(0.035)
    
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
    
        if userInput == "door":
            for c in startInputs['start1Door']:
                print(c, end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        
        elif userInput == "window":
            for c in startInputs['windowOutput']:
                print(c, end="")
                time.sleep(0.035)
            print()
            print()
            start3(rebar)

        elif userInput == "sleep":
            if rebar == 0:
                for c in startInputs['sleep1']:
                    print(c, end="")
                    time.sleep(0.1)
                print()
                time.sleep(5)
                print()
                for c in startInputs['sleep2']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                for c in startInputs['sleep3']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                for c in startInputs['uGotRebar']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                rebar = addRebarToInventory(rebar)
                print(rebar)
                start2(rebar)

            else: 
                for c in startInputs['haveRebar']:
                    print(c, end="")
                    time.sleep(0.035)
        else: 
            print("Please enter a valid action.")

def start2(rebar):
    directions = ["door","window"]
    rebar = addRebarToInventory(rebar)
    start2Inputs={
        'start2Msg1' : "After getting the stick of rebar, you now only have two places left to go",
        'start2Actions' : "Actions: door | window =>",
        'start2Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'start2Window' : "The window in of itself is not that interesting. You feel a need to leave the window, but for some reason, it attracts you further and further."

    }

    for c in start2Inputs['start2Msg1']:
            print(c,end="")
            time.sleep(0.035)
    print()   
    print()
    for c in start2Inputs['start2Actions']:
            print(c,end="")
            time.sleep(0.035)
    userInput = ""
    while userInput not in directions:
     
        userInput = input()
        if userInput == "door":
            for c in start2Inputs['start2Door']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        elif userInput == "window":
        
            for c in start2Inputs['start2Window']:
                print(c,end="")
                time.sleep(0.035)
            print()
            print()
            start3(rebar)
        else: 
            print("Please enter a valid action.")

def start(rebar):
    rebar = 0
    directions = ["door","window","sleep"]
    startInputs = {
        'startMsg1' :"You suddenly wake up in an empty humid room on a cold mattress. The walls are made of concrete.",
        'startMsg2' : "In front of you, you notice a closed metal door, and to your right you see an open window. ",
        'start1Door' : "You open the door and are greeted with a hallway some hundred feet or so long. Cell doors identical to yours line up both walls all the way to the end. ",
        'Actions' : "Actions: door | window | sleep =>",
        'windowOutput' : "The window is blocked off by glass and metal bars, however you can see the outside world being completely white from the neverending snowfall.",
        'sleep1' : "You decide to go back to sleep on your mattress.",
        'sleep2' : "You wake up again. Nothing changes, however as you look up, you notice a loose piece of iron rebar sticking out of the concrete.",
        'sleep3' : "You pull on the rebar, and as it is released from the wall, so does a lot of dust and small pebbles, which cover you. ",
        'uGotRebar' : "[] You got rebar! []",
        'haveRebar' : "Now is not the time to sleep. Get up!",
        'start1Actions' : "Actions: door | window | sleep =>"
    }
    
    
    for c in startInputs['startMsg1']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    
    for c in startInputs['startMsg2']:
            print(c,end="")
            time.sleep(0.035)
    print()
    print()
    for c in startInputs['start1Actions']:
            print(c, end="")
            time.sleep(0.035)
    
    userInput = ""
    while userInput not in directions:
        
        userInput = input()
    
        if userInput == "door":
            for c in startInputs['start1Door']:
                print(c, end="")
                time.sleep(0.035)
            print()
            print()
            hallway1(rebar)
        
        elif userInput == "window":
            for c in startInputs['windowOutput']:
                print(c, end="")
                time.sleep(0.035)
            print()
            print()
            start2Win(rebar)

        elif userInput == "sleep":
            if rebar == 0:
                for c in startInputs['sleep1']:
                    print(c, end="")
                    time.sleep(0.1)
                print()
                time.sleep(5)
                print()
                for c in startInputs['sleep2']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                for c in startInputs['sleep3']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                for c in startInputs['uGotRebar']:
                    print(c, end="")
                    time.sleep(0.035)
                print()
                print()
                rebar = addRebarToInventory(rebar)
                start2(rebar)

            else: 
                for c in startInputs['haveRebar']:
                    print(c, end="")
                    time.sleep(0.035)
        else: 
            print("Please enter a valid action.")

start(0)
