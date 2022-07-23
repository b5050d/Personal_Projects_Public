import tkinter as tk
import datetime
import os

currdir=os.path.dirname(__file__)
logloc=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\Local_Data'
if os.path.exists(logloc):
    print('Your Local_Data folder already exists, very nice')
else:
    os.mkdir(logloc)
print("This is where your logs should be stored and kept private",logloc)

journal_window=tk.Tk()
journal_window.title('Journal')
rv=0
todaydate=str(datetime.date.today())
# print(todaydate)
dateold_lab=tk.Label(text='Date of Entry').grid(row=rv,column=0)
dateold_ent=tk.Entry()
dateold_ent.grid(row=rv,column=1)
dateold_ent.delete('0',tk.END)
dateold_ent.insert('0',todaydate)

def previous_entry():
    date1str=dateold_ent.get()
    date1=datetime.datetime.strptime(date1str,'%Y-%m-%d')
    date2=date1-datetime.timedelta(days=1)
    date2=date2.strftime('%Y-%m-%d')
    add_entry()
    dateold_ent.delete('0',tk.END)
    dateold_ent.insert('0',str(date2))
    newlogfile=logloc+'\\'+date2+'_Personal_Log.txt'
    if os.path.exists(newlogfile):
        textbox_new.delete('1.0',tk.END)
        with open(newlogfile,"r") as newlog:
            a=newlog.read()
        textbox_new.insert('1.0',a)
    else:
        textbox_new.delete('1.0',tk.END)
        textbox_new.insert('1.0',"<No entry exists for this date :/ >")

def next_entry():
    date1str=dateold_ent.get()
    date1=datetime.datetime.strptime(date1str,'%Y-%m-%d')
    date2=date1+datetime.timedelta(days=1)
    date2=date2.strftime('%Y-%m-%d')
    add_entry()
    dateold_ent.delete('0',tk.END)
    dateold_ent.insert('0',str(date2))
    newlogfile=logloc+'\\'+date2+'_Personal_Log.txt'
    if os.path.exists(newlogfile):
        textbox_new.delete('1.0',tk.END)
        with open(newlogfile,"r") as newlog:
            a=newlog.read()
        textbox_new.insert('1.0',a)
    else:
        textbox_new.delete('1.0',tk.END)
        textbox_new.insert('1.0',"<No entry exists for this date :/ >")

def clear_entry():
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',"")

previous_butt=tk.Button(text='Previous Entry',command=previous_entry).grid(row=rv,column=2)
next_butt=tk.Button(text='Next Entry',command=next_entry).grid(row=rv,column=3)
del_butt=tk.Button(text='Delete Entry',command=clear_entry).grid(row=rv,column=4)
rv+=1
textbox_new=tk.Text()
textbox_new.grid(row=rv,columnspan=5)
rv+=1
datenew_lab=tk.Label(text='Current Date:').grid(row=rv,column=0)
datenew_ent=tk.Entry()
datenew_ent.grid(row=rv,column=1)

datenew_ent.delete('0',tk.END)
datenew_ent.insert('0',str(todaydate))

def add_entry():
    text_data=textbox_new.get('1.0',tk.END)
    date=dateold_ent.get()
    newlogfile=logloc+'\\'+date+'_Personal_Log.txt'
    if os.path.exists(newlogfile):
        with open(newlogfile,"w") as newtxt:
            newtxt.write(text_data)
        print('File successfully written to :',os.path.basename(newlogfile))
    else:
        if "<No entry exists for this date :/ >" in text_data:
            print('Skipping, no data entered')
        else:
            with open(newlogfile,"w") as newtxt:
                newtxt.write(text_data)
            print('File successfully written to :',os.path.basename(newlogfile))
        
add_butt=tk.Button(text='Add',command=add_entry).grid(row=rv,column=2)
rv+=1

#Attempt to load the data from the previous entry
newlogfile=logloc+'\\'+todaydate+'_Personal_Log.txt'
if os.path.exists(newlogfile):

    with open(newlogfile,"r") as logfile:
        a=logfile.read()
        # print(a)
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',a)
else:
    textbox_new.delete('1.0',tk.END)
    textbox_new.insert('1.0',"<No entry exists for this date :/ >")

from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        text_data=textbox_new.get('1.0',tk.END)
        date=dateold_ent.get()
        newlogfile=logloc+'\\'+date+'_Personal_Log.txt'
        if os.path.exists(newlogfile):
            pass
        else:
            with open(newlogfile,"w") as newtxt:
                pass
        with open(newlogfile,"w") as newtxt:
            newtxt.write(text_data)
        print('File successfully written to :',os.path.basename(newlogfile))
        journal_window.destroy()
journal_window.protocol("WM_DELETE_WINDOW", on_closing)
journal_window.mainloop()
