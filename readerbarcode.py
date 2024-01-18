from pyzbar.pyzbar import decode
import keyboard
import ctypes
import os
import pyperclip
from PIL import ImageGrab

ctypes.windll.kernel32.SetDllDirectoryW(None)

#os.chdir('C:\\Users\\crist\\OneDrive\\Desktop\\backup\\python\\projetoLeitorexec\\leitorbarcode\\Lib\\site-packages\\pyzbar')
#print(ctypes.CDLL('libvlc.dll'))

comparator = 'test'
while True: 
    try:
        if keyboard.is_pressed('p'):
            break
        img = ImageGrab.grabclipboard()
        if img is None:
            pass
        elif decode(img) == []:
            pyperclip.copy("Leitura não realizada")
        elif img != comparator:
            img = ImageGrab.grabclipboard()
            pyperclip.copy(decode(img)[0].data.decode('utf8'))
            print(decode(img)[0].data.decode('utf-8'))
        
        comparator = img
        
        #keeper = pyperclip.paste()
        #pyperclip.copy(decode(img)[0].data.decode('utf-8'))
    except:
        break