import curses
import os
from curses import wrapper
import random
import time

def textloader():
    with open("/home/mad-lab/pytest/speed meter/test.txt","r") as f:
        text = f.readlines()
        return random.choice(text).strip()

def welcomescreen(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome To The TESTTYPE Game, press any key to continue.....")
    stdscr.refresh()
    stdscr.getkey()

def displaytext(stdscr,maintext,currtext,wpm=0):
    grn= curses.color_pair(1)
    rd = curses.color_pair(2)
    stdscr.erase()
    stdscr.addstr(maintext)
    k=0
    for i,val in enumerate(currtext):
        if maintext[i]==currtext[i]:
            try:
                stdscr.addstr(0,i,val,grn)
            except:
                stdscr.addstr(1,k,val,grn)
                k+=1
        else:
            try:
                stdscr.addstr(0,i,maintext[i],rd)
            except:
                stdscr.addstr(1,k,maintext[i],rd)
                k+=1
        stdscr.addstr(5,0,f"WPM = {wpm}",wpm)
                


def usertype(stdscr):
    currtext = []   
    maintext = textloader() 
    
    stime = time.time()
    stdscr.nodelay(True)
    
    while True:
        timegone = max(time.time()-stime,1)
        wpm = round((len(currtext)/(timegone/60))/5)
        stdscr.erase()
        
        displaytext(stdscr,maintext,currtext,wpm)
        stdscr.refresh()
        try:
            if "".join(currtext) == maintext:
                stdscr.nodelay(False)
                break
        except:
            pass
        
        try:
            key = stdscr.getkey()
        except:
            continue
        try:
            if ord(key) == 53:
                stdscr.nodelay(False)
                return
        except:
            pass
            
            
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(currtext) > 0:
                currtext.pop() 
            else:
                continue
        elif len(maintext) > len(currtext):
            currtext.append(key)
        
        # if ord(key) == 53:
        #     usertype(stdscr)
        
        # if key == "ESCAPE":
        #     break
    return wpm

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    welcomescreen(stdscr)
    while True:
        stdscr.erase()
        result = usertype(stdscr)
        stdscr.refresh()
        stdscr.addstr(7,0,f"Your score is WPM = {result}\nPress enter to play again or ESC to stop")
        key = stdscr.getkey()
        if ord(key)==27:
            break
    
wrapper(main)
    






