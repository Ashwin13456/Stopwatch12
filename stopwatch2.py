#This is a simple python pgm which will run a stopwatch when we give the 'Start' option and stops after pressing Ctrl C 
import time
import select
class Stopwatch:
    def __init__(self):
        self.startTime=None
        self.elapsedTime=0
        self.isRunning=False
    def startWatch(self):
        if not self.isRunning:
            self.startTime=time.time()
            self.isRunning=True
            print("stopwatch has started")
    def stopWatch(self):
        if self.isRunning:
            self.elapsedTime=time.time()-self.startTime
            self.isRunning=False
            print("stopwatch has stopped")
    def resetWatch(self):
        self.elapsedTime=0
        self.isRunning=False
        print("stopwatch has been reset")
    def logWatchTime(self):
        totalTime=self.elapsedTime
        if self.isRunning:
            totalTime+=time.time()-self.startTime
            print(f"Time:{totalTime:.2f}seconds")

stopwatch=Stopwatch()
try:
    while True:
        command=input("please enter one of the following commands...\nStart\nStop\nReset\nQuit\n\n>")
        if(command=="Start"):
            stopwatch.startWatch()
        elif(command=="Stop"):
            stopwatch.stopWatch()
        elif(command=="Reset"):
            stopwatch.resetWatch()
        elif(command=="Quit"):
            break
        else:
            print("invalid command. please try again")
        while stopwatch.isRunning:
            stopwatch.logWatchTime()
            time.sleep(0)
        pass
except KeyboardInterrupt:
    stopwatch.logWatchTime()
    time.sleep(0)
    
   

    
   
