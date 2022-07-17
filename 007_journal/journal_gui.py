from cgitb import text
import tkinter as tk
import datetime
import os

# To Add: Previous Entry Button, Next Entry Button
# A retrieve button to edit previous Entries

currdir=os.path.dirname(__file__)

journal_window=tk.Tk()
journal_window.title('Journal')
rv=0
todaydate=datetime.date.today()
# print(todaydate)
dateold_lab=tk.Label(text='Date of Entry').grid(row=rv,column=0)
dateold_ent=tk.Entry()
dateold_ent.grid(row=rv,column=1)

def previous_entry():
    textbox_old.delete('1.0',tk.END)
    dateold=dateold_ent.get()
    lastdate=dateold-datetime.timedelta(days=1)
    dateold_ent.delete('0',tk.END)
    dateold_ent.insert('0',lastdate)
    path2old=currdir+'\\'+dateold+'_log.txt'
    if os.path.exists(path2old):
        pass
    else:
        print('No Previous Entry Exists')
        textbox_new.insert('1.0','No Entry Exists for this date')
def next_entry():
    pass

def del_entry():
    pass

previous_butt=tk.Button(text='Previous Entry',command=previous_entry).grid(row=rv,column=2)
next_butt=tk.Button(text='Next Entry').grid(row=rv,column=3)
del_butt=tk.Button(text='Delete Entry').grid(row=rv,column=4)
rv+=1
textbox_new=tk.Text(bg='black',fg='cyan')
textbox_new.grid(row=rv,columnspan=5)
rv+=1
datenew_lab=tk.Label(text='Current Date:').grid(row=rv,column=0)
datenew_ent=tk.Entry()
datenew_ent.grid(row=rv,column=1)

datenew_ent.delete('0',tk.END)
datenew_ent.insert('0',str(todaydate))
def add_entry():
    pass

add_butt=tk.Button(text='Add').grid(row=rv,column=2)
rv+=1


textbox_old=tk.Text(bg='black',fg='orange')
textbox_old.grid(row=rv,columnspan=6)
rv+=1


journal_window.mainloop()
