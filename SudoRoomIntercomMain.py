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
import RPi.GPIO as GPIO
from time import sleep
#import io,sys,os,subprocess
#global process

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options    

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--start-fullscreen");
chrome_opt.add_argument("use-fake-ui-for-media-stream")
#chrome_options.add_argument("--kiosk");

##############################################################################
### - 1 - Functions


##############################################################################
### - 2 - Variables

slideshowURL = 'https://docs.google.com/presentation/d/e/2PACX-1vRsIRyslE2K0WIiMawiZuHpU2KHexuSipMXPQTy4ABqsh5MjzRhRz2C5WwdRni3bB_1Ial2Dm0mObrL/pub?start=true&loop=true&delayms=5000'
sudoroomURL = 'http://meet.waag.org/turtlesturtlesturtles'

driver = webdriver.Chrome(chrome_options=chrome_options)

##################################
## - 2.1 - Assets
## Images
menucontrol = pygame.image.load('./Assets/menu-control.png')

## Sounds
#beep1 = pygame.mixer.Sound('./Assets/beep1.wav')


##################################
## - 2.1 - Pins

## Pins
button1 = 26
button2 = 19
button3 = 13

## Pin Modes
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN, pull_up_down=GPIO.PUD_UP)

##################################
## - 2.1 - States

state = 0   # 0: slideshow; 1: Menu;  2: Sudo Room intercom

##############################################################################
### - 3 - Startup commands

### Open browser to slideshow

driver.get(slideshowURL)
# Remove notification
# Make full screen
sleep(8)

driver.get(sudoroomURL)
# Agree to provide mic and camera support
sleep(15)
driver.get(slideshowURL)

print('Beginning loop')

"""

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
# Draw a solid blue circle in the center
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

font = pygame.font.SysFont(None, 66)
font2 = pygame.font.SysFont(None, 50)


screen.blit(menucontrol, (0,0))
pygame.display.update()


"""

##############################################################################
### - 4 - Main loop

while True:
    if state == 0:      # Slideshow mode
        if GPIO.input(button1) == False:
            # Display loading message
            driver.get(sudoroomURL)
            # Clear loading message
            # Agree to provide mic and camera support
            
            sleep(20)
            #timerVal = 15
            driver.get(slideshowURL)
            
        if GPIO.input(button2) == False:
            break
            #Make this go to

    if state == 1:
        pass
    
# Close browser window
print('Done')
    
    




