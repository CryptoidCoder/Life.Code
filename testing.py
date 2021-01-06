import time
import schedule

import tkinter as tk
import threading

# definitions
living = True

def born():
    global age_seconds
    global age_minutes
    global age_hours
    global age_days
    global age_weeks

    age_seconds = 0
    age_minutes = 0
    age_hours = 0
    age_days = 0
    age_weeks = 0

def currenttime():
    currenttime = (age_seconds, age_minutes, age_hours, age_days, age_weeks)
    return currenttime

def one_second_older():
    global age_seconds
    global age_minutes
    global age_hours
    global age_days
    global age_weeks
    global currenttime

    age_seconds += 1 # add 1 to age_seconds
    #print(currenttime())
    
    
    if age_seconds == 60: #if its been a day make age_minutes = +1 and reset seconds counter
        age_minutes += 1
        age_seconds = 0
        #print(currenttime())

    elif age_minutes == 60: #if its been a hour make age_hours = +1 and reset minutes counter
        age_hours += 1
        age_minutes = 0
        #print(currenttime())

    elif age_hours == 24: #if its been a day make age_days = +1 and reset hours counter
        age_days += 1
        age_hours = 0
        #print(currenttime())

    elif age_days == 7:
        age_weeks += 1
        age_days = 0
        #print(currenttime())

def age():
    global living
    if living == True:
        schedule.every(1).seconds.do(one_second_older)

    else:
        print("Im Dead")
        living = False

born() # you are born
age() # you start aging

while True:
    schedule.run_pending()
    time.sleep(1)