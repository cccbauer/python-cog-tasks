#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.77.02), Tue Aug  6 11:30:02 2013
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

# Store info about the experiment pre-post
expName = 'RVIP'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'pre'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s_%s_%s' %(expName,expInfo['participant'],expInfo['session'], expInfo['date'])
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
    text=u'Main session: \n\nHere comes the real task. Again, 2-4-6 and 3-5-7 and 4-6-8 are target sequences. Detect as many target sequences as possible by pressing the space bar as quickly as possible. \n\nPlease wait until the researcher has left the room before starting the task by pressing the space bar. \n\nThis task will take 5 minutes.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
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





import csv
import sys
import numpy as np

print "hello world!"


duration = 1.0;
rateMin = 100.0;
cicles = 5;
targetLen = 3;
minSep = 5;
maxSep = 30;
nTargets = 8;

#targets=[[3,5,7],
       #  [5,7,9],
     #    [2,4,6],
     #    [4,6,8]]
         
         
#targets=[[1,3,5],
 #        [2,4,6],
  #       [3,5,7],
   #      [4,6,8],
    #     [5,7,9]]

targets=[[2,4,6],
         [3,5,7],
         [4,6,8]]

#sm_targets=[[1,3],
            #[2,4],
            #[3,5],
            #[4,6],
            #[5,7]]

sm_targets=[[2,4],
            [3,5],
            [4,6]]

#sm_diffs=[[4],
          #[6],
          #[7],
          #[8],
          #[9]]

sm_diffs=[[6],
          [7],
          [8]]

#kills = [[1,3,5,7],
         #[2,4,6,8],
         #[3,5,7,9]]

kills = [[2,4,6,8]]

allVals = range(2,9)


for this_cicle in range(0,cicles):

    nStim = int(np.ceil((duration*rateMin)/float(targetLen))*float(targetLen))
    # calculate the seperation between targets
    meanSep=float(nStim-maxSep)/float(nTargets)
    stdSep=meanSep/5
    
    print "showing %3.1f stims per min for %3.1f min results in %d stims"%(\
        rateMin,duration,nStim)
    
    stims=np.zeros(nStim).tolist()
    
    #seps=np.random.weibull(5,nTargets)
    #seps=[int(s) for s in np.round(minSep+(meanSep-minSep)*seps/np.mean(seps))]
    seps=[int(s) for s in np.round(np.random.normal(meanSep,stdSep,nTargets))]
    seps[seps<5]=5
    seps[seps>30]=30
    
    ##### now lets generate targets using rubrick
    #start at begining of sequence
    ndx = 0
    t = 0
    response = np.zeros(nStim,dtype=np.int)
    while t < nTargets:
        targetNdx=ndx+seps[t]
        print targetNdx
        if (targetNdx+targetLen) < nStim:
            stims[targetNdx:targetNdx+targetLen]=targets[\
                np.random.random_integers(0,np.shape(targets)[0]-1,size=1)]
            response[targetNdx+targetLen-1]=1
            t=t+1
            ndx=targetNdx
        else:
            break
    
    # now go through and add non-targets 
    for i in range(0,nStim):
        if stims[i] == 0:
            # we will now choose a stim, from those that are acceptable
            if i == 0: 
                possibleVals = allVals
            elif i == 1:
                possibleVals = np.setdiff1d(allVals,[stims[i-1]])
            else:
                pmatch=[j for j in range(0,np.shape(sm_targets)[0]) if sm_targets[j] == stims[i-targetLen+1:i]]
                #print "%d: %s (%s)"%(len(pmatch),\
                    #",".join([str(s) for s in stims[i-targetLen+1:i]]),\
                    #",".join([str(p) for p in pmatch]))
                if len(pmatch) > 0:
                    possibleVals = np.setdiff1d(allVals,[stims[i-1],sm_diffs[pmatch[0]][0]])
                else:
                    possibleVals = np.setdiff1d(allVals,[stims[i-1]])
    
            # assume for now that if post is nonzero it is a target, 
            # so we avoid it
            if i <  nStim-1:
                possibleVals=np.setdiff1d(possibleVals,[stims[i+1],stims[i+1]-2])
    
            stims[i]=np.random.choice(possibleVals)
    
    # check for issues
    dups=[i for i in range(1,nStim) if stims[i-1] == stims[i]]
    if dups:
        print "found %d duplicates %s"%(len(dups),",".join([str(d) for d in dups]))
    
    killSeqs=[i for i in range(0,nStim-(targetLen+1)) if stims[i:i+targetLen+1] in kills]
    if killSeqs:
        print "found %d kill sequences %s"%(len(killSeqs),",".join([str(k) for k in killSeqs]))
    
    if not os.path.isdir('stims'):
        os.makedirs('stims')
    with open('stims/stim_file_%s_%s_%s_%s.csv' %(expName,expInfo['participant'],expInfo['session'], expInfo['date']), 'a') as csvfile:
        stim_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if this_cicle==0:
            stim_writer.writerow(['stim','response'])
            for i in range(0,nStim):
                stim_writer.writerow([stims[i], response[i]])
        else:
            for i in range(0,nStim):
                stim_writer.writerow([stims[i], response[i]])
        
    print "generated %d targets in cicle %d"%(t,this_cicle+1)
    
# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stims/stim_file_%s_%s_%s_%s.csv' %(expName,expInfo['participant'],expInfo['session'], expInfo['date'])),
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
# update component parameters for each repeat
    stim_text.setColor(u'white', colorSpace=u'rgb')
    stim_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    stim_response.status = NOT_STARTED
    # keep track of which components have finished
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
    trialComponents = []
    trialComponents.append(stim_text)
    trialComponents.append(stim_response)
    square.setAutoDraw(True)
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
        elif stim_text.status == STARTED and t >= (0.0 + 1.8):
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
    
# counting and printing number of hitts. 


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
    #	myWin.saveMovieFrames('stimuli.gif')
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

import csv
print filename
with open(filename+'.csv', 'rb') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',',
                                quotechar='')

#reader1 = csv.reader(open(filename+'.csv', 'rb'), delimiter=',', quotechar='"')



count =0
for row in reader1:
    #print row[1],row[7]
    if row[1] == "1"and row[7]!='':
        print "hit", row[1], row[7]
        count+=1
        print count
    else:
        pass#print "different"
    
print "Number of hits: ", count


