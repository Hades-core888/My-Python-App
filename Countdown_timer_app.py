import time 
from playsound import playsound

x = int(50*60)
y = int(10*60)

def Countdown_timer_study (x):
    for i in reversed(range(0, x)):
        time_left = i
        print(f'{ time_left }')
        time.sleep(1)
    print('Countdown End!')
    playsound('F:\VS Code\Python_Products\Python_Apps\Alarm_sound.mp3')    

def Countdown_timer_rest (x):
    while x :
        print(x)
        time.sleep(1)
        x -= 1
    print('Countdown End!')
    playsound('F:\VS Code\Python_Products\Python_Apps\Alarm_sound.mp3')    
    
Countdown_timer_study(x)
Countdown_timer_rest(y)
