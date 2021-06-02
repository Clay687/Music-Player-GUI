from tkinter import *
from playsound import playsound
from tkinter.filedialog import askopenfilename
import win32gui , win32con

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

root.geometry('500x500')
root.minsize(500,500)
root.maxsize(500,500)
root.title('Music Player')
root.wm_iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Music.ico")

Label(root,text="Music Player",fg="red",font="lucida 30 bold underline").place(x=130,y=10)

Label(root,text="Select Song : ",font="luicda 15").place(x=50,y=150)

lbx = Listbox(root,width=30,height=5)
lbx.place(x=200,y=150)

with open('C:\\Users\\prince\\Desktop\\GUI\\Required files\\Music Player.txt', 'r') as a:
    lst = a.readlines()
    if len(lst)>0:
        for i in lst:
            string = str(i)
            string1 = string.split('.mp3')
            
        for s in string1:
            text = str(s)
            text_lst = text.split('/')
            if len(text_lst)>1:
                song_name = text_lst[5]
                song = song_name.replace('.mp3', '')
                lbx.insert(END, song)


def add():
    try:
        file = askopenfilename(defaultextension = ".mp3")
        text = str(file)
        text_lst = text.split('/')
        song_name = text_lst[5]
        song = song_name.replace('.mp3','')
        lbx.insert(END,song)
        with open('C:\\Users\\prince\\Desktop\\GUI\\Required files\\Music Player.txt','a') as f:
            f.write(file)
            f.write('-')
            f.close()

    except Exception as e:
        pass

add_btn = Button(root,text="Add",fg="blue",font="luicda 15",command=add)
add_btn.place(x=120,y=300)

def delete():
    selected_checkboxs = lbx.curselection()
    for selected_checkbox in selected_checkboxs[::-1]:
        lbx.delete(selected_checkbox)

delete_btn = Button(root,text="Delete",fg="blue",font="luicda 15",command=delete)
delete_btn.place(x=330,y=300)

def play():
    song_to_play = lbx.get(ANCHOR)
    with open('C:\\Users\\prince\\Desktop\\GUI\\Required files\\Music Player.txt','r') as y:
        a = y.readlines()
        a1 = a[0].split('-')

        for i in a1:
            ind = a1.index(i)
            a2 = i.split('/')
            try:
                a3 = a2[5]
                a4 = a3.replace('.mp3','')
                if song_to_play==a4:
                    root.wm_state('iconic')
                    playsound(a1[int(ind)])
                    root.state("zoomed") 

            except Exception as e:
                pass

play_btn = Button(root,text="Play",fg="red",font="luicda 15",width=10,command=play)
play_btn.place(x=200,y=400)

root.mainloop()
