#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:16:57 2022
SudoRoomIntercomMain.py
A constantly running program that turns on a kiosk-style looping slideshow in the browser on startup and waits for button input.
@author: andrew
"""
##############################################################################
### - 0 - Libraries
import pygame
import time
import cv2
import RPi.GPIO as GPIO
#import glob
#import numpy as np
#import io,sys,os,subprocess
#global process



##############################################################################
### - 1 - Functions



##############################################################################
### - 2 - Variables

##################################
## - 2.1 - Assets
## Images
menucontrol = pygame.image.load('/home/pi/menu-control.png')

## Sounds
beep1 = pygame.mixer.Sound('/home/pi/beep.wav')

##################################
## - 2.1 - Pins

## Pins
button1 = 2
button2 = 3
button3 = 25

## Pin Modes
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN, pull_up_down=GPIO.PUD_UP)

##############################################################################
### - 3 - Startup commands

### Open browser to slideshow

##############################################################################
### - 4 - Main loop
