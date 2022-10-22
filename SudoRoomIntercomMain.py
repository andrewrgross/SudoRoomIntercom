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
#import cv2
import RPi.GPIO as GPIO
#import glob
#import numpy as np
#import io,sys,os,subprocess
#global process

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

##############################################################################
### - 1 - Functions


##############################################################################
### - 2 - Variables

slideshowURL = 'https://docs.google.com/presentation/d/e/2PACX-1vRsIRyslE2K0WIiMawiZuHpU2KHexuSipMXPQTy4ABqsh5MjzRhRz2C5WwdRni3bB_1Ial2Dm0mObrL/pub?start=true&loop=true&delayms=2000'
sudoroomURL = 'http://meet.waag.org/turtlesturtlesturtles'

chromedriver_location = "/home/andrew/Programs/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

##################################
## - 2.1 - Assets
## Images
menucontrol = pygame.image.load('./Assets/menu-control.png')

## Sounds
beep1 = pygame.mixer.Sound('./Assets/beep1.wav')


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
#driver.get(slideshowURL)
webbrowser.open(slideshowURL)
webbrowser.open(sudoroomURL)

driver.get(slideshowURL)
driver.get(sudoroomURL)

##############################################################################
### - 4 - Main loop
