from tkinter import*
import customtkinter
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    b_root.title("Untitled-Notepad")
    file=NONE
    textArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("ALL Files","*.*"),
                                                            ("Text Documents","*.txt")])
    if file == "":
        file=NONE
    else:
        b_root.title(os.path.basename(file)+ "-Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == NONE:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("ALL Files","*.*"),
                                                            ("Text Documents","*.txt")])
        if file== "":
            file=NONE
        else:
            #save as new file
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            b_root.title(os.path.basename(file)+"-Notepad")
            print("file saved sucsessfully")
    else:
       f=open(file,"w")
       f.write(textArea.get(1.0,END))
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
    showinfo("GUI Notepad ","Notepad by Harshit ")
def Font_szie():
    pass
if __name__ == '__main__':
   customtkinter.set_appearance_mode("dark")
   customtkinter.set_default_color_theme("green")
   b_root=Tk()
   b_root.title("Untitled - WordPlay")
   b_root.wm_iconbitmap("60747.ico")
   b_root.geometry("644x788")
   textArea=Text(b_root,font="TimesNowRoman")
   textArea.pack(expand=TRUE,fill=BOTH)
   file=NONE
   MenuBar=Menu(b_root)
   #File menue starts from here
   FileMenue=Menu(MenuBar,tearoff=0)
   #to open a new file
   FileMenue.add_command(label="New",background="black",foreground="white",command=newFile)
   #to open already existing file
   FileMenue.add_command(label="open",background="black",foreground="white",command=openFile)
   #to save the current file
   FileMenue.add_command(label="Save",background="black",foreground="white",command=saveFile)
   FileMenue.add_separator()
   FileMenue.add_command(label="Exit",background="black",foreground="white",command=quitApp)
   MenuBar.add_cascade(label="File",background="black",foreground="white",menu=FileMenue)
   #File menue ends here
   #edit menue starts from here
   EditMenue=Menu(MenuBar,tearoff=0)
   #featue of cut,copy,paste
   EditMenue.add_command(label="Cut",background="black",foreground="white",command=cut)
   EditMenue.add_command(label="Copy",background="black",foreground="white", command=copy)
   EditMenue.add_command(label="Paste",background="black",foreground="white", command=paste)
   MenuBar.add_cascade(label="Edit",background="white",foreground="black",menu=EditMenue)
   #edit menue ends here
   #help menu starts from here
   HelpMenu=Menu(MenuBar,tearoff=0)
   HelpMenu.add_command(label="About",background="black",foreground="white",command=about)
   MenuBar.add_cascade(label="Help",background="black",foreground="white",menu=HelpMenu)
   #help menu ends here
   #
   FontMenu=Menu(MenuBar,tearoff=0)
   FontMenu.add_command(label="FontSize",background="black",foreground="white",command=Font_szie)
   MenuBar.add_cascade(label="Font",menu=FontMenu)
   #
   b_root.config(menu=MenuBar)
   #adding scrollbar
   Scroll=Scrollbar(textArea)
   Scroll.pack(side=RIGHT,fill=Y)
   Scroll.config(command=textArea.yview)
   textArea.config(yscrollcommand=Scroll.set)
   b_root.mainloop()
