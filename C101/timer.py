import time
seconds = int(input("Enter the amount of time in seconds: "))

def countdowntimer(seconds):
    while(seconds>0):
        minutes = int(seconds/60)
        secs = int(seconds%60)

        timer =  f'{minutes}:{secs}'
        print(timer, end='\r')
        time.sleep(1)
        
        seconds = seconds -1
    print("Time's Up!")


countdowntimer(seconds)

