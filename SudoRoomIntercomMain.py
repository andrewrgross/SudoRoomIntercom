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
from datetime import datetime
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
chrome_options.add_argument("use-fake-ui-for-media-stream")
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
menucontrol = pygame.image.load('/home/pi/Desktop/SudoRoomIntercom/Assets/menu-control.png')

## Sounds
#beep1 = pygame.mixer.Sound('~/Desktop/SudoRoomIntercom/Assets/beep1.wav')


##################################
## - 2.1 - Pins

## Pins
button1 = 6
button2 = 13
button3 = 19
button4 = 26

## Pin Modes
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4,GPIO.IN, pull_up_down=GPIO.PUD_UP)

## Define pygame fonts
font = pygame.font.SysFont(None, 66)
font2 = pygame.font.SysFont(None, 50)

##################################
## - 2.1 - States

state = 0   # 0: slideshow; 1: Menu;  2: Sudo Room intercom
selectionPos = 0
selectionList = ['Sudo Room', 'Test 1', 'Test 2', 'Test 3']

##############################################################################
### - 3 - Startup commands

### Open browser to video chat

driver.get(sudoroomURL)
sleep(4)
### Set the quality
driver.find_element_by_tag_name('body').send_keys('a')
driver.find_element_by_tag_name('body').send_keys('\t')
driver.find_element_by_tag_name('body').send_keys('\t')
ActionChains(driver).key_down(Keys.LEFT).key_up(Keys.LEFT).key_down(Keys.LEFT).key_up(Keys.LEFT).perform()

driver.get(slideshowURL)
sleep(3)

print('Testing pygame')

color_list = ((255,0,255), (255,0,127), (255,0,0), (255,127,0))
text1 = font.render('Sudo Room', True, color_list[0])
text2 = font2.render('Test', True, color_list[1])
text3 = font2.render('Test 2', True, color_list[2])
text4 = font2.render('TEST 3', True, color_list[3])
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screen.blit(text1, (30, 50))
screen.blit(text2, (60, 160))
screen.blit(text3, (60, 260))
screen.blit(text4, (60, 360))

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
# Draw a solid blue circle in the center
pygame.draw.circle(screen, (0, 0, 100), (250, 250), 75)
#screen.blit(menucontrol, (0,0))
pygame.display.update()
sleep(1)
pygame.quit()

##############################################################################
### - 4 - Main loop

while True:
    if state == 0:      # Slideshow mode
        if GPIO.input(button1) == False:
            ActionChains(driver).key_down(Keys.LEFT).key_up(Keys.LEFT).perform()
            
        if GPIO.input(button2) == False:
            print('Button 2 pressed in state 0: activate pygame menu')
            state = 1
            timeStamp = datetime.now()
            pygame.init()
            screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            screen.fill((255, 255, 255))
            # Draw a solid blue circle in the center
            screen.blit(text1, (30, 50))
            screen.blit(text2, (60, 160))
            screen.blit(text3, (60, 260))
            screen.blit(text4, (60, 360))            
            #screen.blit(menucontrol, (0,0))
            pygame.display.update()
            
        if GPIO.input(button3) == False:
            ActionChains(driver).key_down(Keys.RIGHT).key_up(Keys.RIGHT).perform()

        if GPIO.input(button4) == False:
            print('Button 1 pressed in state 0: activate intercom')
            state = 1
            timeStamp = datetime.now()
            # Display loading message
            driver.get(sudoroomURL)
            # Clear loading message
            sleep(1)
            
            
    if state == 1:      # Menu
        if (datetime.now() - timeStamp).total_seconds() > 10:
            print('State 1 timeout')
            state = 0
            print('Switching to state 0 after timeout')
            pygame.quit()
            sleep(1)
            
        if GPIO.input(button1) == False:
            # Scroll or update
            state = 0
            print('Button 1 pressed in state 1: Switching to state 0')
            pygame.quit()
            driver.get(slideshowURL)
            sleep(1)
            
        if GPIO.input(button2) == False:
            print('Button 2 pressed in state 1')
            selectionPos = selectionPos - 1
                if selectionPos == -1:
                    selectionPos = len(selectionList)
            sleep(0.5)
            
        if GPIO.input(button3) == False:
            print('Button 3 pressed in state 1: Activate Intercom')
            state = 1
            timeStamp = datetime.now()
            # Display loading message
            driver.get(sudoroomURL)
            # Clear loading message
            sleep(1)
            
        if GPIO.input(button4) == False:
            print('Button 2 pressed in state 1')
            selectionPos = selectionPos - 1
                if selectionPos == -1:
                    selectionPos = len(selectionList)
            sleep(0.5)
            
            
    if state == 2:      # Intercom            
        if (datetime.now() - timeStamp).total_seconds() > 60:
            print(datetime.now())
            state = 0
            driver.get(slideshowURL)
            
        if GPIO.input(button1) == False:
            print('Button 1 pressed in state 1: end call')
            state = 0
            driver.get(slideshowURL)    
            sleep(1)
            
        if GPIO.input(button3) == False:
            print('Button 3 pressed in state 1: extend call')
            timeStamp = datetime.now()   
            sleep(0.5)
            



sleep(1)



        
    
# Close browser window
print('Done')
    
    




