import datetime
import time
import tkinter as tk
from tkinter import messagebox
from playsound import playsound

root = tk.Tk()
root.title("Alarm Clock")


def set_alarm():
    
    alarm_time = alarm_entry.get()
    
    
    if not alarm_time:
        messagebox.showerror("Error", "Please enter a time for the alarm.")
        return
    
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    except ValueError:
        messagebox.showerror("Error", "Please enter a time in the format HH:MM.")
        return
    
    if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
        messagebox.showerror("Error", "Please enter a valid time in the format HH:MM.")
        return
    
    
    alarm_time_str = datetime.time(alarm_hour, alarm_minute).strftime("%I:%M %p")
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}.")
    
    
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        
        if current_hour == alarm_hour and current_minute == alarm_minute:
            
            playsound("sound.mp3")
            
            
            alarm_message = messagebox.showinfo("Alarm", "Time to wake up!", parent=root)
            
            
            if alarm_message == "ok":
                break
        
        root.update()
        time.sleep(1) 


alarm_label = tk.Label(root, text="Enter alarm time (HH:MM):")
alarm_label.pack()

alarm_entry = tk.Entry(root)
alarm_entry.pack()

alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
alarm_button.pack()

root.mainloop()
