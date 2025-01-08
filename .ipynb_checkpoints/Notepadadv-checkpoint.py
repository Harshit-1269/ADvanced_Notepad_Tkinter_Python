from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    b_root.title("Untitled-Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("ALL Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        b_root.title(os.path.basename(file) + "-Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("ALL Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save as new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            b_root.title(os.path.basename(file) + "-Notepad")
            print("file saved successfully")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    b_root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    showinfo("GUI Notepad", "Notepad by Harshit")

def toggle_theme():
    current_theme = b_root.cget("bg")
    if current_theme == "white":
        b_root.configure(background="black")
        textArea.configure(background="black", foreground="white")
    else:
        b_root.configure(background="white")
        textArea.configure(background="white", foreground="black")

def change_font_type(font_type):
    textArea.config(font=(font_type, current_font_size.get()))

def change_font_size(font_size):
    textArea.config(font=(current_font_type.get(), font_size))

if __name__ == '__main__':
    b_root = Tk()
    b_root.title("Untitled - WordPlay")
    b_root.wm_iconbitmap("60747.ico")
    b_root.geometry("644x788")

    textArea = Text(b_root, font=("TimesNowRoman", 12))
    textArea.pack(expand=TRUE, fill=BOTH)

    file = None

    MenuBar = Menu(b_root)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", background="black", foreground="white", command=newFile)
    FileMenu.add_command(label="Open", background="black", foreground="white", command=openFile)
    FileMenu.add_command(label="Save", background="black", foreground="white", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", background="black", foreground="white", command=quitApp)
    MenuBar.add_cascade(label="File", background="black", foreground="white", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", background="black", foreground="white", command=cut)
    EditMenu.add_command(label="Copy", background="black", foreground="white", command=copy)
    EditMenu.add_command(label="Paste", background="black", foreground="white", command=paste)
    MenuBar.add_cascade(label="Edit", background="white", foreground="black", menu=EditMenu)

    ModeMenu = Menu(MenuBar, tearoff=0)
    ModeMenu.add_command(label="Switch Mode", background="black", foreground="white", command=toggle_theme)
    MenuBar.add_cascade(label="Mode", menu=ModeMenu)

    FontMenu = Menu(MenuBar, tearoff=0)
    current_font_type = StringVar(b_root)
    current_font_type.set("TimesNowRoman")
    FontMenu.add_radiobutton(label="TimesNewRoman",background="black", foreground="white", variable=current_font_type, value="TimesNowRoman", command=lambda: change_font_type("TimesNowRoman"))
    FontMenu.add_radiobutton(label="Algerian",background="black", foreground="white", variable=current_font_type, value="Algerian", command=lambda: change_font_type("Algerian"))
    FontMenu.add_radiobutton(label="Calibri", background="black", foreground="white", variable=current_font_type,
                             value="Calibri", command=lambda: change_font_type("Calibri"))
    FontMenu.add_radiobutton(label="Elephant", background="black", foreground="white", variable=current_font_type,
                             value="Elephant", command=lambda: change_font_type("Elephant"))
    MenuBar.add_cascade(label="Font", menu=FontMenu)

    SizeMenu = Menu(MenuBar, tearoff=0)
    current_font_size = IntVar(b_root)
    current_font_size.set(12)
    SizeMenu.add_radiobutton(label="12",background="black", foreground="white", variable=current_font_size, value=12, command=lambda: change_font_size(12))
    SizeMenu.add_radiobutton(label="14",background="black", foreground="white", variable=current_font_size, value=14, command=lambda: change_font_size(14))
    SizeMenu.add_radiobutton(label="16",background="black", foreground="white", variable=current_font_size, value=16, command=lambda: change_font_size(16))
    SizeMenu.add_radiobutton(label="18",background="black", foreground="white", variable=current_font_size, value=18, command=lambda: change_font_size(18))
    SizeMenu.add_radiobutton(label="32", background="black", foreground="white", variable=current_font_size, value=32,command=lambda: change_font_size(32))
    MenuBar.add_cascade(label="Size", menu=SizeMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", background="black", foreground="white", command=about)
    MenuBar.add_cascade(label="Help", background="black", foreground="white", menu=HelpMenu)

    b_root.config(menu=MenuBar)

    Scroll = Scrollbar(textArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=Scroll.set)

    b_root.mainloop()
