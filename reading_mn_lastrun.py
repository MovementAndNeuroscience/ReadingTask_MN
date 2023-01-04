#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on december 02, 2022, at 11:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'reading_mn'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\neurolab\\Desktop\\Reading Task MN\\reading_mn_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Velkommen til   \n  \nLæseopgaven\n\nTryk på mellemrumstasten.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "words2_trials" ---
# Run 'Begin Experiment' code from code
count = 0

correct = [1, 1, 1, 1]


words2_screen = visual.TextStim(win=win, name='words2_screen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
words2_resp = keyboard.Keyboard()

# --- Initialize components for Routine "words3_trials" ---
words3_screen = visual.TextStim(win=win, name='words3_screen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
words3_resp = keyboard.Keyboard()

# --- Initialize components for Routine "words4_trials" ---
words4_screen = visual.TextStim(win=win, name='words4_screen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
words4_resp = keyboard.Keyboard()

# --- Initialize components for Routine "words5_trials" ---
words5_screen = visual.TextStim(win=win, name='words5_screen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
words5_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Finished" ---
finished_text = visual.TextStim(win=win, name='finished_text',
    text='Godt klaret! \n\nOpgaven er afsluttet.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome_text, key_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_text.started')
        welcome_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['enter','space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words2_trials" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    count = count + 1
    
    if sum(correct[-4:]) == 0:
        continueRoutine = False
        trials_2.finished = True
    words2_screen.setText(words2)
    words2_resp.keys = []
    words2_resp.rt = []
    _words2_resp_allKeys = []
    # keep track of which components have finished
    words2_trialsComponents = [words2_screen, words2_resp]
    for thisComponent in words2_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "words2_trials" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *words2_screen* updates
        if words2_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words2_screen.frameNStart = frameN  # exact frame index
            words2_screen.tStart = t  # local t and not account for scr refresh
            words2_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words2_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words2_screen.started')
            words2_screen.setAutoDraw(True)
        
        # *words2_resp* updates
        waitOnFlip = False
        if words2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words2_resp.frameNStart = frameN  # exact frame index
            words2_resp.tStart = t  # local t and not account for scr refresh
            words2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words2_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words2_resp.started')
            words2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(words2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(words2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if words2_resp.status == STARTED and not waitOnFlip:
            theseKeys = words2_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _words2_resp_allKeys.extend(theseKeys)
            if len(_words2_resp_allKeys):
                words2_resp.keys = _words2_resp_allKeys[-1].name  # just the last key pressed
                words2_resp.rt = _words2_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in words2_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "words2_trials" ---
    for thisComponent in words2_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    if words2_resp.keys == 'right':
        correct.append(1)
    else:
        correct.append(0)
    
        
    
    print(correct)
    print(sum(correct[-4:]))
    # check responses
    if words2_resp.keys in ['', [], None]:  # No response was made
        words2_resp.keys = None
    trials_2.addData('words2_resp.keys',words2_resp.keys)
    if words2_resp.keys != None:  # we had a response
        trials_2.addData('words2_resp.rt', words2_resp.rt)
    # the Routine "words2_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words3_trials" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    count = count + 1
    
    if sum(correct[-4:]) == 0:
        continueRoutine = False
        trials_3.finished = True
    
    
    words3_screen.setText(words3)
    words3_resp.keys = []
    words3_resp.rt = []
    _words3_resp_allKeys = []
    # keep track of which components have finished
    words3_trialsComponents = [words3_screen, words3_resp]
    for thisComponent in words3_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "words3_trials" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *words3_screen* updates
        if words3_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words3_screen.frameNStart = frameN  # exact frame index
            words3_screen.tStart = t  # local t and not account for scr refresh
            words3_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words3_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words3_screen.started')
            words3_screen.setAutoDraw(True)
        
        # *words3_resp* updates
        waitOnFlip = False
        if words3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words3_resp.frameNStart = frameN  # exact frame index
            words3_resp.tStart = t  # local t and not account for scr refresh
            words3_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words3_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words3_resp.started')
            words3_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(words3_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(words3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if words3_resp.status == STARTED and not waitOnFlip:
            theseKeys = words3_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _words3_resp_allKeys.extend(theseKeys)
            if len(_words3_resp_allKeys):
                words3_resp.keys = _words3_resp_allKeys[-1].name  # just the last key pressed
                words3_resp.rt = _words3_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in words3_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "words3_trials" ---
    for thisComponent in words3_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    if words3_resp.keys == 'right':
        correct.append(1)
    else:
        correct.append(0)
    
    
    
    print(correct)
    print(sum(correct[-4:]))
    # check responses
    if words3_resp.keys in ['', [], None]:  # No response was made
        words3_resp.keys = None
    trials_3.addData('words3_resp.keys',words3_resp.keys)
    if words3_resp.keys != None:  # we had a response
        trials_3.addData('words3_resp.rt', words3_resp.rt)
    # the Routine "words3_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words4_trials" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    count = count + 1
    
    if sum(correct[-4:]) == 0:
        continueRoutine = False
        trials_4.finished = True
    
    
    words4_screen.setText(words4)
    words4_resp.keys = []
    words4_resp.rt = []
    _words4_resp_allKeys = []
    # keep track of which components have finished
    words4_trialsComponents = [words4_screen, words4_resp]
    for thisComponent in words4_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "words4_trials" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *words4_screen* updates
        if words4_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words4_screen.frameNStart = frameN  # exact frame index
            words4_screen.tStart = t  # local t and not account for scr refresh
            words4_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words4_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words4_screen.started')
            words4_screen.setAutoDraw(True)
        
        # *words4_resp* updates
        waitOnFlip = False
        if words4_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words4_resp.frameNStart = frameN  # exact frame index
            words4_resp.tStart = t  # local t and not account for scr refresh
            words4_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words4_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words4_resp.started')
            words4_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(words4_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(words4_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if words4_resp.status == STARTED and not waitOnFlip:
            theseKeys = words4_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _words4_resp_allKeys.extend(theseKeys)
            if len(_words4_resp_allKeys):
                words4_resp.keys = _words4_resp_allKeys[-1].name  # just the last key pressed
                words4_resp.rt = _words4_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in words4_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "words4_trials" ---
    for thisComponent in words4_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    if words4_resp.keys == 'right':
        correct.append(1)
    else:
        correct.append(0)
    
    
    
    
    
    
    
    
    print(correct)
    print(sum(correct[-4:]))
    # check responses
    if words4_resp.keys in ['', [], None]:  # No response was made
        words4_resp.keys = None
    trials_4.addData('words4_resp.keys',words4_resp.keys)
    if words4_resp.keys != None:  # we had a response
        trials_4.addData('words4_resp.rt', words4_resp.rt)
    # the Routine "words4_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words5_trials" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    count = count + 1
    
    if sum(correct[-4:]) == 0:
        continueRoutine = False
        trials_5.finished = True
    
    words5_screen.setText(words5)
    words5_resp.keys = []
    words5_resp.rt = []
    _words5_resp_allKeys = []
    # keep track of which components have finished
    words5_trialsComponents = [words5_screen, words5_resp]
    for thisComponent in words5_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "words5_trials" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *words5_screen* updates
        if words5_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words5_screen.frameNStart = frameN  # exact frame index
            words5_screen.tStart = t  # local t and not account for scr refresh
            words5_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words5_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words5_screen.started')
            words5_screen.setAutoDraw(True)
        
        # *words5_resp* updates
        waitOnFlip = False
        if words5_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            words5_resp.frameNStart = frameN  # exact frame index
            words5_resp.tStart = t  # local t and not account for scr refresh
            words5_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words5_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'words5_resp.started')
            words5_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(words5_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(words5_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if words5_resp.status == STARTED and not waitOnFlip:
            theseKeys = words5_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _words5_resp_allKeys.extend(theseKeys)
            if len(_words5_resp_allKeys):
                words5_resp.keys = _words5_resp_allKeys[-1].name  # just the last key pressed
                words5_resp.rt = _words5_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in words5_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "words5_trials" ---
    for thisComponent in words5_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_4
    if words5_resp.keys == 'right':
        correct.append(1)
    else:
        correct.append(0)
    
    
    
    print(correct)
    print(sum(correct[-4:]))
    # check responses
    if words5_resp.keys in ['', [], None]:  # No response was made
        words5_resp.keys = None
    trials_5.addData('words5_resp.keys',words5_resp.keys)
    if words5_resp.keys != None:  # we had a response
        trials_5.addData('words5_resp.rt', words5_resp.rt)
    # the Routine "words5_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# --- Prepare to start Routine "Finished" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
FinishedComponents = [finished_text, key_resp_2]
for thisComponent in FinishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Finished" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finished_text* updates
    if finished_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_text.frameNStart = frameN  # exact frame index
        finished_text.tStart = t  # local t and not account for scr refresh
        finished_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finished_text.started')
        finished_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['enter','space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Finished" ---
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
