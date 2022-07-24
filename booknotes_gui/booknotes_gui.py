from cgitb import text
import tkinter as tk
import os
from tkinter import messagebox
import glob

currdir=os.path.dirname(__file__)
notesloc=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\Local_Data'
if os.path.exists(notesloc):
    print('Your Local_Data folder already exists, very nice')
else:
    os.mkdir(notesloc)
    print("This application has gone ahead and created the necessary folder")

print("This is where your notesheets should be stored and kept private",notesloc)
booknote_window=tk.Tk()
booknote_window.title('Book Notes')
rv=0
# todaydate=str(datetime.date.today())
# print(todaydate)
book_lab=tk.Label(text='Book Name:').grid(row=rv,column=0)
book_ent=tk.Entry()
book_ent.grid(row=rv,column=1)

chap_num_lab=tk.Label(text='Chapter Number:').grid(row=rv,column=2)
chap_num_ent=tk.Entry()
chap_num_ent.grid(row=rv,column=3)

chap_title_lab=tk.Label(text='Chapter Title:').grid(row=rv,column=4)
chap_title_ent=tk.Entry()
chap_title_ent.grid(row=rv,column=5)

# book_ent.delete('0',tk.END)
# book_ent.insert('0',todaydate)

def get_attributes(filename):
    filename=os.path.basename(filename)
    filename=filename[:-4]
    fileparts=filename.split('_')
    bookname=fileparts[1]
    chap_num=fileparts[2]
    chap_name=fileparts[3]
    return bookname,chap_num,chap_name

def select_book():
    pass

def previous_chapter():
    add_entry()
    chap_num=chap_num_ent.get()
    bookname=book_ent.get()
    chap_num=str(int(chap_num)-1)
    if int(chap_num)<0:
        print('There are no previous files')
    else:
        desfilename='bn_{}_{}_*.txt'.format(bookname,chap_num)
        print('DesFileName:',desfilename)
        desfilelist=glob.glob(notesloc+'\\'+desfilename)
        print(desfilelist)
        if len(desfilelist)!=1:
            print('Something went wrong, we found too many or too little files')
        else:
            desfile=desfilelist[0]
            if os.path.exists(desfile):
                textbox_new.delete('1.0',tk.END)
                with open(desfile,"r") as newtxt:
                    a=newtxt.read()
                textbox_new.insert('1.0',a)
            else:
                textbox_new.delete('1.0',tk.END)
                textbox_new.insert('1.0',"<No data, desfile doesn't exist somehow?>")
            
            bookname,chap_num,chap_title=get_attributes(desf)
            chap_num_ent.delete('0',tk.END)
            chap_num_ent.insert('0',chap_num)
            chap_title_ent.delete('0',tk.END)
            chap_title_ent.insert('0',chap_title)
            book_ent.delete('0',tk.END)
            book_ent.insert('0',bookname)

def next_chapter():
    add_entry()
    chap_num=chap_num_ent.get()
    chap_title=chap_title_ent.get()
    bookname=book_ent.get()
    chap_num_new=str(int(chap_num)+1)
    newnotefile=notesloc+'\\bn_{}_{}_*.txt'.format(bookname,chap_num_new,chap_title)
    newnotelist=glob.glob(newnotefile)
    newnotefile=newnotelist[0]
    with open(newnotefile,"r") as newtxt:
        a=newtxt.read()
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',a)

def clear_entry():
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',"")

rv+=1
textbox_new=tk.Text()
textbox_new.grid(row=rv,columnspan=6)
rv+=1

previous_butt=tk.Button(text='Previous Entry',command=previous_chapter).grid(row=rv,column=2)
next_butt=tk.Button(text='Next Entry',command=next_chapter).grid(row=rv,column=3)
del_butt=tk.Button(text='Delete Entry',command=clear_entry,fg='red').grid(row=rv,column=4)
rv+=1

def add_entry():
    chap_num=chap_num_ent.get()
    chap_title=chap_title_ent.get()
    bookname=book_ent.get()
    text_data=textbox_new.get('1.0',tk.END)

    notefile=notesloc+'\\bn_{}_{}_{}.txt'.format(bookname,chap_num,chap_title)
    with open(notefile,"w") as newtxt:
        newtxt.write(text_data)

#Attempt to load the data from the previous entry, find the highest chap num
newnoteaddy=notesloc+'\\bn*.txt'
notedir=glob.glob(newnoteaddy)
if len(notedir)==0:
    print('There are no book notes')
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',"There are no book notes")
else:
    notedir=sorted(notedir,key = os.path.getmtime)
    notedir.reverse()
    mostrecent=notedir[0]
    recentname=os.path.basename(mostrecent)
    recentname=recentname[:-4]
    recname_list=recentname.split('_')
    bookname=recname_list[1]
    chap_num=recname_list[2]
    chap_title=recname_list[3]
    book_ent.delete('0',tk.END)
    book_ent.insert('0',bookname)
    chap_num_ent.delete('0',tk.END)
    chap_num_ent.insert('0',chap_num)
    chap_title_ent.delete('0',tk.END)
    chap_title_ent.insert('0',chap_title)

    newlogfile=notesloc+'\\bn_{}_{}_{}.txt'.format(bookname,chap_num,chap_title)
    with open(newlogfile,"r") as logfile:
        a=logfile.read()
#         # print(a)
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',a)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        text_data=textbox_new.get('1.0',tk.END)
        newnotefile=notesloc+'\\bn_{}_{}_{}.txt'.format(bookname,chap_num,chap_title)
        if os.path.exists(newnotefile):
            pass
        else:
            with open(newnotefile,"w") as newtxt:
                pass
        with open(newnotefile,"w") as newtxt:
            newtxt.write(text_data)
        print('File successfully written to :',os.path.basename(newnotefile))
        booknote_window.destroy()
booknote_window.protocol("WM_DELETE_WINDOW", on_closing)
booknote_window.mainloop()
