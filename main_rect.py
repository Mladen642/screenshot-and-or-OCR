import tkinter as tk
import os
from datetime import datetime
import pytesseract
import pyautogui
from rich.prompt import Prompt
from rich import print
from rich.console import Console

#Directory change
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
#Console init
c = Console()
#Tesseract CMD
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

c.rule(title='Welcome')

class DrawRectangle:
    def __init__(self, root):
        self.root = root
        self.start_x = None
        self.start_y = None
        self.canvas = tk.Canvas(root, bg="gray", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.rect = None

    def on_click(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="white", width=2)

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        now = datetime.now()
        self.root.destroy()  # Close the overlay after selection

        img = pyautogui.screenshot(region=(self.start_x,self.start_y,event.x-self.start_x, event.y - self.start_y))
        path = f'img/{now.strftime('%d-%b-%Y,%H-%M-%S')}.png'
        img.save(path)
        print(f'Image saved at location [green]"{path}"[/]\n')

        next=Prompt.ask('Would you like to attempt to read text from image via OCR? [teal][y/n][/]', choices=['y','n'], default="y")

        if next =='y':
            language = Prompt.ask("Choose language: ", default = 'eng', choices = ['eng','srp_latn', 'deu']); print()
            text = pytesseract.image_to_string(path, lang=language)
            print(f'Here is the extracted text:\n[yellow]{text}')
            
            #Write OCR into .txt file
            path = path[3:-4]
            with open(f"output/{path}.txt", "w", encoding='utf-8') as f:
                for i in text:
                    f.write(i)
        else:
            print("BYE!")
        
        c.rule(title='END')



# Create the full-screen overlay
root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.2)  # Semi-transparent effect
app = DrawRectangle(root)
root.mainloop()
