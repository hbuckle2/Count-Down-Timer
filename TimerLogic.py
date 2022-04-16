from threading import Timer
from tkinter import *
import time
from winsound import PlaySound

app_window = Tk()
app_window.geometry('400x300')
app_window.resizable(0,0)
app_window.config(bg = 'blanched almod')
app_window.title('Horace Countdown Clock And Timer')
Label(app_window, text= 'Countdown Clock and Timer', font = 'arial 20 bold', bg = 'papaya whip').pack()

Label(app_window, font = 'arial 15 bold', text = 'current time :', bg = 'papaya whip').place(x=40, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

curr_time =Label(app_window, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()

sec = StringVar()
Entry(app_window, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')
mins= StringVar()
Entry(app_window, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')
hrs= StringVar()
Entry(app_window, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')

def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        app_window.update()
        time.sleep(1)
        if(times == 0):
            #playsound('Loud_Alarm_Clock_Buzzer.mp3')
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1