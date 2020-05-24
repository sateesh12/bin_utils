#Author : Sateesh
#Purpose: Based on a keyboard combination take a snap of screen and store at pre-defined spot
#Date   : 24/May/2020
#License: Apache 2.0

from pynput.keyboard import Key, Listener

def on_press(key):
        print("Key press received");
        print('{0} pressed'.format(key))

def on_release(key):
    print("Key release received")
    print('{0} release'.format(key))
    if key == Key.esc:
# Stop listener
        return False
# Collect events until released
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
