import psychopy.visual
from psychopy import monitors
import psychopy.event
from psychopy.visual import DotStim
import psychopy.gui
import psychopy.core
import random
import numpy as np
import pprint

mon = monitors.Monitor('Dell')
data = []
rtdata = []

#Entry through dialog box
gui = psychopy.gui.Dlg()
gui.addField("Subject ID:")
gui.addField("Name:")
gui.addField("Age:")

gui.show()

subj_id = gui.data[0]
name = gui.data[1]
age = int(gui.data[2])

#Running the loop from c=0.1 to c=0.4 and again to c = 0.10 or 20 times
cr = 0
incr = 0
score = 10
fscore = 0
flag = 0
coh1 = [0.100, 0.175, 0.250, 0.325, 0.400, 0.325, 0.250, 0.175]
coh2 = [0.100]
dir_list = [0.0, 180.0]
cr_rt = 0
incr_rt = 0

#Introduction window
win = psychopy.visual.Window(
                size=[1080, 720],
                units="pix",
                fullscr=True,
                color=[1, 1, 1],
                monitor=mon
                )
text = psychopy.visual.TextStim(
                    win=win,
                    text="Welcome to the experiment.\n You will be presented some random moving dots on the screen. \n You have to repond in which direction the dots are moving.\n You can end the experiment any time by pressing the Escape key. Press space for further instructions and continue.",
                    color=[-1, -1, -1]
                )
text.draw()
win.flip()
k = psychopy.event.waitKeys(keyList=["space","escape"])
if k == ["escape"]:
    psychopy.core.quit()


for i in range(1, 2):                      #Change 2 to increase the number of trials
    for c in coh1:
        direction = random.choice(dir_list)

        win1 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        text = psychopy.visual.TextStim(
        win=win1,
        text="You have to press 'Z' for left and 'M' for right. Press spacebar to continue.",
        color=[-1, -1, -1]
        )

        text.draw()

        win1.flip()

        k = psychopy.event.waitKeys(keyList=["space", "escape"])
        if k == ["escape"]:
            psychopy.core.quit()

        win2 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )


        ds = DotStim(
                 win2,
                 units='',
                 nDots=500,
                 coherence= c,
                 fieldPos=(0.0, 0.0),
                 fieldSize=(480.0, 480.0),
                 fieldShape='circle',
                 dotSize=5.0,
                 dotLife=-1,
                 dir=direction,
                 speed=8.0,
                 rgb=None,
                 color=(-1.0, -1.0, -1.0),
                 colorSpace='rgb',
                 opacity=1.0,
                 contrast=1.0,
                 depth=0,
                 element=None,
                 signalDots='same',
                 noiseDots='direction',
                 name=None,
                 autoLog=None)


        for frame in range(120):       #Change 120 if refresh rate of your monitor is not 60hz
            ds.draw()
            win2.flip()

        #Window 3 for taking input
        win3 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        text = psychopy.visual.TextStim(
        win=win3,
        text="Enter your response to continue.",
        color=[-1, -1, -1]
        )

        text.draw()

        win3.flip()
        clock = psychopy.core.Clock()
        ks = psychopy.event.waitKeys(keyList=["z", "m", "escape"],timeStamped=clock)
        for keys,rt in ks:
            rtdata.append([rt])
            print(keys,rt)
        win0 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        if keys == ["escape"]:
            psychopy.core.quit()

        if (direction == 0.0 and keys == "m") or (direction == 180.0 and keys == "z"):
            message1 = psychopy.visual.TextStim(win=win0, text="Correct!", color=[1,-1,-1])
            for frame in range(30):
                message1.draw()
                win0.flip()
            cr_rt = cr_rt + rt
            cr+=1
            flag+= 1
            fscore = fscore + score
            if flag % 3 == 0:
                score = score * 2
        else:
            message2 = psychopy.visual.TextStim(win=win0, text="Incorrect!", color=[1,-1,-1])
            for frame in range(30):
                message2.draw()
                win0.flip()
            incr_rt = incr_rt + rt
            incr+=1
            flag = 0
            score = 10
#Loop to complete the phase cycle
for c in coh2:
        direction = random.choice(dir_list)

        win1 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        text = psychopy.visual.TextStim(
        win=win1,
        text="You have to press 'Z' for left and 'M' for right. Press spacebar to continue.",
        color=[-1, -1, -1]
        )

        text.draw()

        win1.flip()

        k = psychopy.event.waitKeys(keyList=["space", "escape"])
        if k == ["escape"]:
            psychopy.core.quit()

        win2 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )


        ds = DotStim(
                 win2,
                 units='',
                 nDots=500,
                 coherence= c,
                 fieldPos=(0.0, 0.0),
                 fieldSize=(480.0, 480.0),
                 fieldShape='circle',
                 dotSize=5.0,
                 dotLife=-1,
                 dir=direction,
                 speed=8.0,
                 rgb=None,
                 color=(-1.0, -1.0, -1.0),
                 colorSpace='rgb',
                 opacity=1.0,
                 contrast=1.0,
                 depth=0,
                 element=None,
                 signalDots='same',
                 noiseDots='direction',
                 name=None,
                 autoLog=None)


        for frame in range(120):
            ds.draw()
            win2.flip()

        #Window 3 for taking input
        win3 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        text = psychopy.visual.TextStim(
        win=win3,
        text="Enter your response to continue.",
        color=[-1, -1, -1]
        )

        text.draw()

        win3.flip()
        clock = psychopy.core.Clock()
        ks = psychopy.event.waitKeys(keyList=["z", "m", "escape"],timeStamped=clock)
        for keys,rt in ks:
            rtdata.append([rt])
            print(keys,rt)
        win0 = psychopy.visual.Window(
        size=[1366, 768],
        units="pix",
        fullscr=True,
        color=[1, 1, 1],
        monitor=mon
        )

        if keys == ["escape"]:
            psychopy.core.quit()

        if (direction == 0.0 and keys == "m") or (direction == 180.0 and keys == "z"):
            message1 = psychopy.visual.TextStim(win=win0, text="Correct!", color=[1,-1,-1])
            for frame in range(30):
                message1.draw()
                win0.flip()
            cr_rt = cr_rt + rt
            cr+=1
            flag+= 1
            fscore = fscore + score
            if flag % 3 == 0:
                score = score * 2
        else:
            message2 = psychopy.visual.TextStim(win=win0, text="Incorrect!", color=[1,-1,-1])
            for frame in range(30):
                message2.draw()
                win0.flip()
            incr_rt = incr_rt + rt
            incr+=1
            flag = 0
            score = 10
#Thanking window
win4 = psychopy.visual.Window(
                size=[1080, 720],
                units="pix",
                fullscr=True,
                color=[1, 1, 1],
                monitor=mon
                )
text = psychopy.visual.TextStim(
                    win=win4,
                    text="End of the experiment \n Thank You for participating!",
                    color=[-1, -1, -1]
                )
text.draw()
win4.flip()
psychopy.core.wait(1.0)

win.close()
win0.close()
win1.close()
win2.close()
win3.close()
win4.close()

data.append(
    [
        subj_id,
        name,
        age,
        cr,
        incr,
        fscore,
        cr_rt,
        incr_rt
    ]
)

pprint.pprint(data)
pprint.pprint(rtdata)

np.savetxt(
    "C:/Users/Kumar Abhijeet/Desktop/exp1_data2.tsv",
    rtdata,
    delimiter="\t"
    )
