from cgitb import text
import tkinter as tk
import datetime
import os

# To Add: Previous Entry Button, Next Entry Button
# A retrieve button to edit previous Entries
# Get the current date to show up

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
    pass
    # textbox_old.delete('1.0',tk.END)
    # dateold=dateold_ent.get()
    # lastdate=dateold-datetime.timedelta(days=1)
    # dateold_ent.delete('0',tk.END)
    # dateold_ent.insert('0',lastdate)
    # path2old=currdir+'\\'+dateold+'_log.txt'
    # if os.path.exists(path2old):
    #     pass
    # else:
    #     print('No Previous Entry Exists')
    #     textbox_new.insert('1.0','No Entry Exists for this date')
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
    text_data=textbox_new.get('1.0',tk.END)
    date=datenew_ent.get()
    newlogfile=logloc+'\\'+date+'_Personal_Log.txt'
    if os.path.exists(newlogfile):
        print('Log already Exists, just appending for now')
    else:
        with open(newlogfile,"w") as newtxt:
            pass
    print('text_data:',text_data)
    with open(newlogfile,"a") as newtxt:
        newtxt.write(text_data)
    print('File successfully written to :',os.path.basename(newlogfile))
add_butt=tk.Button(text='Add',command=add_entry).grid(row=rv,column=2)
rv+=1


# textbox_old=tk.Text(bg='black',fg='orange')
# # textbox_old.grid(row=rv,columnspan=6)
# rv+=1


journal_window.mainloop()
