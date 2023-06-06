from playsound import playsound
import time
def alarm(seconds):
    CLEAR="\033[2J"
    CLEAR_AND_RETURN="\033[H"
    time_elapsed=0
    print(CLEAR)
    while(time_elapsed<seconds):
        time.sleep(1)
        time_elapsed+=1
        timeleft=seconds-time_elapsed
        miniutes=timeleft//60
        second=timeleft%60
        print(f"{CLEAR_AND_RETURN}TIME REMAINING TILL ALARM IS {miniutes:02d}:{second:02d}")
    playsound("Danger Alarm.mp3")
miniutes = int(input("enter for how many miniutes you want to set the alarm "))
seconds  = int(input("enter for how many seconds you want to set the alarm "))
totalsecond=miniutes*60+seconds
alarm(totalsecond)
