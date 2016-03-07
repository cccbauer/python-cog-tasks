#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Wed Jul 31 11:55:59 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'RVIP'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'train'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data/train'):
    os.makedirs('data/train')  # if this fails (e.g. permissions) we will get error
filename = 'data/train' + os.path.sep + '%s_%s_%s' %(expName,expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instruct_text = visual.TextStim(win=win, ori=0, name='instruct_text',
    text="Practice session: \n\nYou will see numbers being presented in rapid succession on the screen. You will be asked to indicate when specific target sequences are presented. These target sequences are 2,4,6 and 3,5,7 and 4,6,8. Please concentrate, and detect as many target sequences as quickly as possible by pressing the space bar when you see a target sequence. In the present practice session target sequences will be presented in green. Please also press the space bar as quickly as possible when you see a target sequence. \n\nThe practice session will take 1 minute.\n\n Press the space bar whenever you are ready to start!",    
    wrapWidth=1.6,
    font=u'Arial',
    pos=[0, 0], height=0.1,
    color=u'white', 
    colorSpace=u'rgb', 
    opacity=1,
    depth=0.0)


# Initialize components for Routine "trial"
trialClock = core.Clock()
stim_text = visual.TextStim(win=win, ori=0, name='stim_text',
    text='nonsense',    font=u'Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color=1.0, colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thanks = visual.TextStim(win=win, ori=0, name='thanks',
    text='Thanks!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ready = event.BuilderKeyResponse()  # create an object of type KeyResponse
ready.status = NOT_STARTED
# keep track of which components have finished
instructComponents = []
instructComponents.append(instruct_text)
instructComponents.append(ready)
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text* updates
    if t >= 0.0 and instruct_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_text.tStart = t  # underestimates by a little under one frame
        instruct_text.frameNStart = frameN  # exact frame index
        instruct_text.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0.0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t  # underestimates by a little under one frame
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents()
    if ready.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'train_file.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.600000)
    sqrVertices = [ [0.2,-0.2], [-0.2,-0.2], [-0.2,0.2], [0.2,0.2] ]
    sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] 
    correct = visual.TextStim(win,
                        text = u"hit spacebar",#you can find the unicode character value from MS Word 'insert symbol'
                        color='red',  
                        font=sans,
                        pos=(0,0.4),
                        height = 0.1)
                        
    square = visual.ShapeStim(win, 
                 lineColor='white',
                 lineWidth=2.0, #in pixels
                 fillColor=[0,0,0], #beware, with convex shapes this won't work
                 fillColorSpace='rgb',
                 vertices=sqrVertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 autoLog=False)
    hintLine= visual.Line(win, 
                lineColor='green',
                start=(-0.2, -0.4), 
                end=(0.2, -0.4),
                lineWidth=4.0,)
    #hintLine.setLineColor(hint)
    
    correct.setAutoDraw(True)
    correct.setColor(spacebar, colorSpace=u'rgb')
    #square.setLineColor(u'white', colorSpace=None, operation='')
    square.setAutoDraw(True)
    stim_text.setColor(hint, colorSpace=u'rgb')
    # update component parameters for each repeat
    stim_text.setColor(hint, colorSpace=u'rgb')
    stim_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    stim_response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(stim_text)
    trialComponents.append(stim_response)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_text* updates
        if t >= 0.0 and stim_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_text.tStart = t  # underestimates by a little under one frame
            stim_text.frameNStart = frameN  # exact frame index
            stim_text.setAutoDraw(True)
        elif stim_text.status == STARTED and t >= (0.0 + .6):
            stim_text.setAutoDraw(False)
        if stim_text.status == STARTED:  # only update if being drawn
            stim_text.setText(stim, log=False)
        
        # *stim_response* updates
        if t >= 0 and stim_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_response.tStart = t  # underestimates by a little under one frame
            stim_response.frameNStart = frameN  # exact frame index
            stim_response.status = STARTED
            # keyboard checking is just starting
            stim_response.clock.reset()  # now t=0
            event.clearEvents()
        elif stim_response.status == STARTED and t >= (0 + 0.6):
            stim_response.status = STOPPED
        if stim_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if len(theseKeys) > 0:  # at least one key was pressed
                stim_response.keys = theseKeys[-1]  # just the last key pressed
                stim_response.rt = stim_response.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(stim_response.keys) == 0:  # No response was made
       stim_response.keys=None
    # store data for trials (TrialHandler)
    trials.addData('stim_response.keys',stim_response.keys)
    if stim_response.keys != None:  # we had a response
        trials.addData('stim_response.rt', stim_response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = []
ThanksComponents.append(thanks)
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t  # underestimates by a little under one frame
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    elif thanks.status == STARTED and t >= (0.0 + 2.0):
        thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
