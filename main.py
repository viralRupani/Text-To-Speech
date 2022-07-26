from gtts import gTTS
from window import Window
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filetypes = (
    # ('pdf file', '*.pdf'),
    # ('text files', '*.txt'),
)


def open_file():
    try:
        with open(filedialog.askopenfilename(filetypes=[('text files', '*.txt')])) as file:
            language = 'en'
            try:
                gTTS(text=str(file.readlines()), lang=language, slow=False).save("TTS.mp3")
                messagebox.showinfo(title='Completed', message='Your audio file has been saved as TTS')
            except:
                messagebox.showerror(title="undefined character", message='Please enter file that only contains text')

    except:
        pass

window = Window(height=400, width=600)

label = Label(text='TTS Service', font=('Arial', 20))
label.config(justify='center', pady=20)
label.pack()

open_file_button = Button(text='Open file', command=open_file)
open_file_button.config(justify="center")
open_file_button.pack()

label_text = Label(text='We will make audio file of your text file (txt/pdf)')

window.mainloop()
