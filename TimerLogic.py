# When setting the time only use two digit inputs

from tkinter import *
import time

app_window = Tk()
app_window.geometry('500x400')
app_window.resizable(0, 0)
app_window.config(bg='black')
app_window.title('Horace Countdown Clock And Timer')
Label(app_window, text='Countdown Clock and Timer', font='arial 20 bold', bg='green').pack()

Label(app_window, font='arial 15 bold', text='Current Time :', bg='green').place(x=59, y=70)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text=clock_time)
    curr_time.after(1000, clock)


curr_time = Label(app_window, font='arial 15 bold', text='', fg='gray25', bg='red')
curr_time.place(x=200, y=70)
clock()

seconds = StringVar()
Entry(app_window, textvariable=seconds, width=2, font='arial 12').place(x=250, y=155)
seconds.set('00')
minutes = StringVar()
Entry(app_window, textvariable=minutes, width=2, font='arial 12').place(x=225, y=155)
minutes.set('00')
hours = StringVar()
Entry(app_window, textvariable=hours, width=2, font='arial 12').place(x=200, y=155)
hours.set('00')


def countdown():
    times = int(hours.get()) * 3600 + int(hours.get()) * 60 + int(seconds.get())
    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        seconds.set(second)
        minutes.set(minute)
        hours.set(hour)

        app_window.update()
        time.sleep(1)
        if times == 0:
            seconds.set('00')
            minutes.set('00')
            hours.set('00')
        times -= 1


Label(app_window, font='arial 15 bold', text='Set Timer', bg='green').place(x=59, y=150)
Button(app_window, text='START TIMER', bd='5', command=countdown, bg='red', font='arial 10 bold').place(x=150,
                                                                                                            y=210)
app_window.mainloop()
