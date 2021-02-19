#Author : Sateesh
#Purpose: Based on a keyboard combination take a snap of screen and store at pre-defined spot
#Date   : 24/May/2020
#License: Apache 2.0
import sys
import pyautogui
import os
import datetime
import uuid
base_dir = r'/Users/sateeshk'
base_dir = base_dir + "/" + str(datetime.date.today())
print(base_dir)
# Collect events until released
count = 1
if(os.path.isdir(base_dir)):
        print("Director exists")
        dir_name = uuid.uuid4().hex
        os.chdir(base_dir)
        os.mkdir(dir_name)
        base_dir = os.path.join(base_dir,dir_name)
else:
    os.mkdir(base_dir)
while True:
    choice = input()
    if choice == 'a':
        print("Now screen capcture")
        print("Simply enter small a and enter key your screen-shot is saved")
        print("Run this program in a small window")
        myScreenshot = pyautogui.screenshot()
        file_name = str(count) + '.png'
        print(file_name)
        full_path = os.path.join(base_dir,file_name)
        print(full_path)
        myScreenshot.save(full_path)
        count = count + 1
        print(count)
    elif choice == 'q':
        print("Your saved .pngs are in" + full_path)
        exit() 
