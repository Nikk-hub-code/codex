import datetime
import time
from playsound import playsound # type: ignore

try:
    while True:
        user_alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        try:
            alarm_hr, alarm_min, alarm_sec = map(int, user_alarm_time.split(':'))
            print(f"Alarm set for {user_alarm_time}.\nWaiting...")
            break
        except ValueError:
            print("Invalid format. Use HH:MM:SS.")

    while True:
        current_time = datetime.datetime.now()
        if (current_time.hour == alarm_hr and 
            current_time.minute == alarm_min and 
            current_time.second == alarm_sec):
            print("It's Time..........")
            try:
                playsound('taqdeer_violin_bgm.mp3')  # Try full path if needed
            except Exception as e:
                print(f"Error playing sound: {e}")
            break
        time.sleep(1)
except KeyboardInterrupt:
    print("\nAlarm stopped by user.")