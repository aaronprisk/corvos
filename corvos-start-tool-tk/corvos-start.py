# corvos first start tool
# Aaron J. Prisk - 2017
# Multi window boilerplate adapted from loctv

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import subprocess

LARGE_FONT = ("Verdana", 14) # font's family is Verdana, font's size is 12 
MED_FONT = ("Verdana", 12) # font's family is Verdana, font's size is 12 

# ----------------------MAIN CLASS--------------------------------------------------------

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Corvos Startup") # set the title of the main window
        self.geometry("500x400") # set size of the main window to 300x300 pixels
        self.resizable(False, False)
 
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)   # make the cell in grid cover the entire window
        container.grid_columnconfigure(0,weight=1) # make the cell in grid cover the entire window
        self.frames = {} # these are pages we want to navigate to
 
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky="nsew") # grid it to container
 
        self.show_frame(StartPage) # let the first page is StartPage
 
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
 
# ----------------------FUNCTIONS--------------------------------------------------------

def cleanscript():
        os.system('~/corvos-start-tool/cleansetup.sh')

def lockscript():
        os.system('~/corvos-start-tool/locksetup.sh')

def linkscript(self,linkurl):
        print (linkurl.get())
        self.controller.show_frame(PageSix)

def browsefunc(self):
        filename =  filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        os.system("cp " + filename + " /home/aaron/wall.jpg")
        self.controller.show_frame(PageTwo)

# --------------------------START FRAME----------------------------------------------------

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo

        label = tk.Label(self, text="Welcome to Corvos! Let's get started!", font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment

        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text="Let's go", anchor= S, command=lambda : controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)
 
# --------------------------WALLPAPER FRAME----------------------------------------------------

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text="How about that wallpaper?", font=LARGE_FONT)
        hintlabel = tk.Label(self, text="*Don't worry, you can always change this later.")
        label.pack()
        hintlabel.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Keep the corvos one', command=lambda : controller.show_frame(PageTwo))
        browsebutton = tk.Button(self, font=MED_FONT, text='Use another wallpaper', command=lambda : browsefunc(self))   
        button1.pack()
        browsebutton.pack()     

# --------------------------WALLPAPER CONFIRM----------------------------------------------------

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text="Wallpaper look good?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Yes', command=lambda : controller.show_frame(PageThree))
        button2 = tk.Button(self, bg="#f0413c", fg="white", activebackground="#f09390", activeforeground="white", font=MED_FONT, text='No', command=lambda : controller.show_frame(PageOne))
        button1.pack()
        button2.pack()

# ----------------------------CLEANER FRAME--------------------------------------------------

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text='Enable the Student Profile Cleaner?', font=LARGE_FONT)
        label.pack(pady=5, padx=10)
        sub_label = tk.Label(self, text='The Profile cleaner automatically clears to the student profile every login.')
        sub_label.pack(pady=5, padx=10)
        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Yes', command=cleanscript)
        button2 = tk.Button(self, bg="#f0413c", fg="white", activebackground="#f09390", activeforeground="white", font=MED_FONT, text='No', command=lambda : controller.show_frame(PageFour))
        button1.pack()
        button2.pack()

# -----------------------------LOCKDOWN FRAME-------------------------------------------------

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text="Lock down student profile?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Yes', command=lockscript)
        button2 = tk.Button(self, bg="#f0413c", fg="white", activebackground="#f09390", activeforeground="white", font=MED_FONT, text='No', command=lambda : controller.show_frame(PageFive))
        button1.pack()
        button2.pack()

# -----------------------------LINK FRAME-------------------------------------------------

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text="Let's add your school link", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        linkurl = tk.Entry(self)
        linkurl.pack()
        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Create Link', command=lambda : linkscript(self,linkurl))
        button2 = tk.Button(self, bg="#f0413c", fg="white", activebackground="#f09390", activeforeground="white", font=MED_FONT, text='Skip', command=lambda : controller.show_frame(PageSix))
        button1.pack()
        button2.pack()

# -----------------------------FINAL FRAME-------------------------------------------------

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # corvos Image
        photo = PhotoImage(file="corvos.png")
        photo_label = Label(self,image=photo, anchor = N)
        photo_label.pack(pady=50, padx=10)
        photo_label.image = photo
        label = tk.Label(self, text="You're ready to go!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, bg="#442178", fg="white", activebackground="#5b4878", activeforeground="white", font=MED_FONT, text='Complete', command=self.quit)
        button1.pack()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
