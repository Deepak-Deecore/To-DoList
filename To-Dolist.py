#import libs
import tkinter
from tkinter import messagebox


#main window
root=tkinter.Tk()
root.geometry("1000x600")
root.minsize(1000,600)
root.maxsize(1000,600)
root.title("ToDo list")


#creating functions
#to collect task
def submit():
    if not task.get():
        tkinter.messagebox.showerror(title="Error", message="Enter the task....")
        return
    f=tkinter.Frame(root,highlightbackground="grey",highlightthickness=1)
    f.pack(padx=50,fill=tkinter.BOTH)
    txt=task.get()
    tkinter.Label(f,text=txt,font="Arial 20 ").pack(side=tkinter.LEFT)
    tkinter.Button(f,text="Delete",command=lambda: delete_frame(f)).pack(side=tkinter.RIGHT,padx=10,pady=5)
    tkinter.Button(f,text="Edit",command=lambda: edit(txt,f)).pack(side=tkinter.RIGHT,pady=5)
    task_entry.delete(0,tkinter.END)
    if(sub["text"]=="EDIT"):
        sub["text"]="submit"
        tkinter.messagebox.showinfo(title="updated", message="Task is Updated Successfully...")

#to delete the task
def delete_frame(frame):
    frame.destroy()

#to update the task
def edit(t,f):
    sub['text']="EDIT" 
    task.set(t)
    delete_frame(f)


#creating user friendly-GUI
tkinter.Label(root,text="ToDo List",bg="green yellow",font="pacifico  40 bold",anchor="w",padx=50,pady=50).pack(fill="x")

tkinter.Label(root,text="Add Items",font="Arial 20 bold",padx=50,pady=20).pack(anchor="w")

f1=tkinter.Frame(root)
f1.pack(anchor="w",padx=50)
task=tkinter.StringVar()
task_entry=tkinter.Entry(f1,textvariable=task,font="arial 20",width=50,borderwidth=2)
task_entry.pack(side=tkinter.LEFT)
sub=tkinter.Button(f1,text="Submit",command=submit,font="10")
sub.pack(side=tkinter.LEFT,padx=20)

tkinter.Label(root,text="Tasks",font="Arial 20 bold").pack(padx=50,pady=30, anchor="w")

#end the mainloop
root.mainloop() 