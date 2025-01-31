import keyboard
import pyautogui
import os
from datetime import datetime
import pytesseract
from rich.prompt import Prompt
from rich import print
from rich.console import Console

#Object init
c = Console()
#Tesseract CMD
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
#Directory change
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
#Coordinates init
coordinates = []

c.rule(title='Welcome')
print('Move mouse to [yellow]top left[/] position and press shift. Repeat for [green]bottom right[/] position\n')

#Top left
keyboard.wait('shift')
x,y = pyautogui.position()
top_left = x,y
coordinates.append(top_left)
print(f'Logged top left position at [red]{x,y}[/]\n')

#Bottom right
keyboard.wait('shift')
i,j = pyautogui.position()
bottom_right = (i,j); coordinates.append(bottom_right)
print(f'Logged bottom right position at [red]{i,j}[/]\n')

x = (coordinates[0][0]); y = (coordinates[0][1])
i = (coordinates[1][0]); j = (coordinates[1][1])

now = datetime.now()

img = pyautogui.screenshot(region=(x,y,i-x,j-y))
path = f'img/{now.strftime('%d-%b-%Y,%H-%M-%S')}.png'
img.save(path)
print(f'Image saved at location [green]"{path}"[/]\n')

next=Prompt.ask('Would you like to attempt to read text from image via OCR? [teal][y/n][/]', choices=['y','n'], default="y")

if next =='y':
    text = pytesseract.image_to_string(path)
    print(f'Here is the extracted text:\n[yellow]{text}')
    
    #Write OCR into .txt file
    path = path[3:-4]
    with open(f"output/{path}.txt", "w") as f:
        for i in text:
            f.write(i)
else:
    print("BYE!")

c.rule(title='END')