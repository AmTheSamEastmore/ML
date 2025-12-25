#   Main Library
import time
import random
import simpleaudio as sa
from random import randint
from threading import Thread

all = ['Cobra', 'Updates']

class Cobra:
    def __init__(self):
        self.letters = [chr(x) for x in range(97, 123)]
        self.block = chr(0x2586)

    def change(self,variableø,whatø) -> bool:
        """Returns if variableø is ecual to whatø"""
        return (variableø == whatø)

    def between(self,thisø:float,lessø:float,moreø:float) -> bool:
        """Returns if thisø is more than lessø and is less than moreø"""
        return ((lessø<thisø<moreø))

    def sleep(self,timeø:float):
        """Waits in seconds"""
        time.sleep(timeø)

    def delay(self,timeø:float):
        """Waits in miliseconds"""
        timeø = timeø/1000
        time.sleep(timeø)
    
    def fastconfig(self,window:object,background:str = 'grey',title:str = 'tkinter window',size:str = '500x500',icon:str = "logggo.ico"):
        window.config(bg=background)
        window.title(title)
        window.geometry(size)
        window.resizable(False,False)
        window.iconbitmap(icon)

    def color(self) -> str:
        '''Returns a random color in hexadecimal'''
        def hexa(r):
            r = str(hex(r))[2:]
            if (len(r) == 1):
                r = '0' + r
            return r
        return f'#{hexa(randint(0,255))}{hexa(randint(0,255))}{hexa(randint(0,255))}'

    def randnum(self,leastø:int,maximumø:int) -> int:
        '''Returns a random number between leastø and maximumø'''
        return randint(leastø,maximumø)

    def choose(self,fwhatø:list) -> any:
        '''Chooses a random thing from fwhatø'''
        return random.choice(fwhatø)

    def on(self,conditionø:bool,functionø,parameterø=None):
        '''if conditionø is true, does functionø with parameterø as parameter'''
        if (conditionø):
            functionø(parameterø)

    def rans(self,charactersø:int = 5) -> str:
        '''Returns a random string with determinate characters(determined by charactersø)'''
        tore = ''
        for _ in range(charactersø):
            tore = tore + self.choose(self.letters)
        return tore
    
    def ranl(self,qcharactersø:int = 5,qiø:int = 4):
        tore = []
        for _ in range(qiø):
            tore.append(self.rans(qcharactersø))
        return tore

    def sound(self,soundø):
        ''' Can only use .wav '''
        wave = sa.WaveObject.from_wave_file(soundø)
        play = wave.play()
        play.wait_done()
    
    def slowPrint(self,messageø : str,upperø:bool = True,intervalø=0.5):
        '''It\'s a print that waits to put each letter, and if you set upperø to True it leaves spaces between letters'''
        if (upperø):
            for letter in messageø:
                print(letter.capitalize(),end=' ')
                self.sec(intervalø)
            print('')
        elif (not(upperø)):
            for letter in messageø:
                print(letter,end='')
                self.sec(intervalø)
            print('')
    
    def amap(self,x,in_min,in_max,out_min,out_max) -> int:
        """Arduino\'s map"""
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        
    def randflo(self,leastø:int,maximumø:int) -> float:
        '''Returns a random number between leastø and maximumø(including floats)'''
        tore = str(randint(leastø,maximumø))
        return float(tore + '.' + str(self.number(0,9)))
    
class Updates:
    def __init__(self, delay):
        self.funcList = []
        self.delay = delay

    def funcs(self):
        for func in self.funcList:
            func()

    def addFunc(self, func):
        self.funcList.append(func)

    def updateStart(self):
        while True:
            self.funcs()
            time.sleep(self.delay)

    def __call__(self):
        thrd = Thread(target=self.updating, daemon=False)
        thrd.start()