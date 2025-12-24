import time
import datetime
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "music.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        time.sleep(1)
        
        if current_time == alarm_time:
            is_running = False
            print("Wake Up !")
            os.startfile(sound_file)            
    
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)