# from distutils import text_file
import tkinter as tk
import os
import glob
from tkinter import messagebox

booknotes_window=tk.Tk()
booknotes_window.title('Book Notes')
rv=0
#Define Componenets
book_lab=tk.Label(text='Book Name:').grid(row=rv,column=0)
book_ent=tk.Entry()
book_ent.grid(row=rv,column=1)

chnum_lab=tk.Label(text='Chp #:').grid(row=rv,column=2)
chnum_ent=tk.Entry()
chnum_ent.grid(row=rv,column=3)

chtit_lab=tk.Label(text='Chp Title:').grid(row=rv,column=4)
chtit_ent=tk.Entry()
chtit_ent.grid(row=rv,column=5)

rv+=1
textbox=tk.Text(bg='black',fg='cyan',insertbackground='green')
textbox.grid(row=rv,columnspan=6)

#Define any variables/Necessary resources
currdir=os.path.dirname(__file__)
local_data=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\Local_Data'

#Define functions

def save_entry():
    book=book_ent.get()
    chnum=chnum_ent.get()
    chtit=chtit_ent.get()
    data=textbox.get('1.0',tk.END)
    notename="bn_{}_{}_{}.txt".format(book,chnum,chtit)
    notepath=local_data+'\\'+notename
    with open(notepath,"w") as notetxt:
        notetxt.write(data)
    print('File successfully writteh to:',notename)
    return book,chnum,chtit

def get_attributes(notepath):
    notename=os.path.basename(notepath)
    notename=notename[:-4]
    namelist=notename.split('_')
    book=namelist[1]
    chnum=namelist[2]
    chtit=namelist[3]
    return book,chnum,chtit

def read_entry(book,chnum):
    nameguess='bn_{}_{}_*.txt'.format(book,chnum)
    list1=glob.glob(local_data+'\\'+nameguess)
    if len(list1)==1:
        notepath=list1[0]
        with open(notepath,"r") as notetxt:
            data=notetxt.read()
        textbox.delete('1.0',tk.END)
        textbox.insert('1.0',data)
        book,chnum,chtit=get_attributes(notepath)
        book_ent.delete('0',tk.END)
        book_ent.insert('0',book)
        chnum_ent.delete('0',tk.END)
        chnum_ent.insert('0',chnum)
        chtit_ent.delete('0',tk.END)
        chtit_ent.insert('0',chtit)
        return notepath
    else:
        print('Something went wrong trying to find the notefile,probably doesnt exist yet')

def previous_entry():
    book,chnum,chtit=save_entry()
    chnum2=str(int(chnum)-1)
    notepath=read_entry(book,chnum2)

def next_entry():
    book,chnum,chtit=save_entry()
    chnum2=str(int(chnum)+1)
    notepath=read_entry(book,chnum2)

def create_chp():
    pass

def select_fn():
    pass

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        save_entry()
        booknotes_window.destroy()

#So now read the most recent entry
notesdir=glob.glob(local_data+'\\bn*.txt')
if len(notesdir)==0:
    print("There are no book notes")
else:
    notesdir=sorted(notesdir,key=os.path.getmtime)
    notesdir.reverse()
    mostrecent=notesdir[0]
    book,chnum,chtit=get_attributes(mostrecent)
    read_entry(book,chnum)

booknotes_window.protocol("WM_DELETE_WINDOW", on_close)

rv+=1
last_chp_button=tk.Button(text='Last Chapter',command=previous_entry).grid(row=rv,column=0)
next_chp_button=tk.Button(text='Next Chapter',command=next_entry).grid(row=rv,column=1)
create_new_chp_button=tk.Button(text='Create New',command=create_chp).grid(row=rv,column=2)
select_book_button=tk.Button(text='Select Book',command=select_fn).grid(row=rv,column=3)
booknotes_window.mainloop()