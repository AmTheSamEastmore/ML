#   Main Library
import time
import random
import simpleaudio as sa
from random import randint
from threading import Thread

all = ['Shortcut', 'Updates']

class Shortcut:
    ''' This class has a wide variety of methods that may help you shorten things  '''
    def __init__(self):
        self.letters = [chr(x) for x in range(97, 123)]
        self.block = chr(0x2586)

    def sleep(self,secs:float):
        """Waits in seconds"""
        time.sleep(secs)

    def delay(self,milis:float):
        """Waits in miliseconds"""
        milis = milis/1000
        time.sleep(milis)
    
    def fastconfig(self,window:object,background:str = 'grey',title:str = 'Window',size:str = '500x500'):
        window.config(bg=background)
        window.title(title)
        window.geometry(size)
        window.resizable(False,False)

    def randColor(self):
        '''Returns a random color in hexadecimal'''
        def randHex():
            tore = str(hex(randint(0,255)))[2:]
            if (len(tore) == 1):
                tore = '0' + tore
            return tore
        return f'#{randHex()}{randHex()}{randHex()}'

    def randNum(self,least:int,maximum:int) -> int:
        '''Returns a random number between least and maximum'''
        return randint(least,maximum)

    def choose(self,list:list) -> any:
        '''Chooses a random thing from list'''
        return random.choice(list)

    def on(self,condition:bool,func):
        '''If condition is true, executes func'''
        if (condition):
            func()

    def ranStr(self,chars:int = 5) -> str:
        '''Returns a random string with chars characters'''
        tore = ''
        for _ in range(chars):
            tore = tore + self.choose(self.letters)
        return tore
    
    def ranList(self,characters:int = 5,indexesNum:int = 4):
        ''' Uses rans(characters) to make a list with indexesNum indexes'''
        tore = []
        for _ in range(indexesNum):
            tore.append(self.rans(characters))
        return tore

    def sound(self,sound):
        ''' Plays a WAW '''
        wave = sa.WaveObject.from_wave_file(sound)
        play = wave.play()
        play.wait_done()
    
    def slowPrint(self, message:str, upper:bool = True, delay:float = 0.5):
        '''It\'s a print that waits in between printing each letter, and if you set upper to True it leaves spaces between letters and makes them uppercase'''
        for letter in message:
            if upper:
                print(letter.capitalize(),end=' ', flush=True)
            else:
                print(letter,end='', flush=True)
            time.sleep(delay)
        print('')
    
    def aMap(self, x, min, max, new_min, new_max) -> int:
        """Arduino\'s map"""
        return (x - min) * (new_max - new_min) / (max - min) + new_min
        
    def randFlo(self, least:int, max:int, decimals:int):
        '''Returns a random number between least and maximum with decimals decimals'''
        tore = f'{str(randint(least,max))}.'
        for _ in range(decimals):
            tore = f'{tore}{randint(0,9)}'
        return tore
    
class Updates:
    ''' Works like an update func, but more organized, do addFunc(func) to add a function and start it with nameOfObj(), delay is the seconds that pass between each execution of funcs '''
    def __init__(self, miliDelay:float = 500):
        self.funcList = []
        self.delay = miliDelay/1000

    def doFuncs(self):
        for func in self.funcList:
            func()

    def addFunc(self, func):
        '''Adds a func to the list of functions that will get executed'''
        self.funcList.append(func)

    def updateStart(self):
        while True:
            self.doFuncs()
            time.sleep(self.delay)

    def __call__(self):
        '''Starts the cicle'''
        thrd = Thread(target=self.updateStart, daemon=False)
        thrd.start()