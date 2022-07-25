from tkinter import *


class Window(Tk):
    def __init__(self, height, width):
        super().__init__()
        self.title("Text to Speech")
        self.minsize(width=width, height=height)
