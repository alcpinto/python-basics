from tkinter import *
from PIL import Image

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Fake")
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text='Quit', command=self.client_exit)
        # quitButton.place(x=0, y=0)
        # menubar
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)

        fileMenu = Menu(menuBar)

        fileNewMenu = Menu(fileMenu)
        fileNewMenu.add_command(label='Project')
        fileNewMenu.add_command(label='Folder')
        fileMenu.add_cascade(label='New', menu=fileNewMenu)

        fileMenu.add_command(label='Exit', command=self.client_exit)
        menuBar.add_cascade(label='File', menu=fileMenu)

        editMenu = Menu(menuBar)
        editMenu.add_command(label='Show Image', command=self.showImg)
        editMenu.add_command(label='Show Text', command=self.showTxt)
        menuBar.add_cascade(label='Edit', menu=editMenu)

    def client_exit(self):
        exit()

    def showImg(self):
        photo = PhotoImage(file='pic.png')
        img = Label(self, image=photo)
        img.image = photo
        img.place(x=0, y=0)


    def showTxt(self):
        txt = Label(self, text='Hey there good looking!')
        txt.pack()


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
