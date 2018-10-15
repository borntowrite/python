#import everything from tkinter
from tkinter import*

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk

#creating class, window, and inheriting from Frame class.
#Frame is a class from the tkinter module (Lib/tkinter/__init__)
class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #creation of init_window
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand =1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        
        edit = Menu(menu)
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)
        
        quitButton = Button(self, text="Exit", command=self.client_exit)
        quitButton.place(x=0, y=0)

    def showImg(self):
        load = Image.open("pic.jpg")
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
