import tkinter as tk
root=tk.Tk()
root.title("ashish")
root.geometry('400x500')
root.configure(background="#000000")
label=tk.Label(root,text="hi ashish",font="lucida 15 bold",bg="red",fg="blue")
label.pack(side="top")
def check():
    l1=tk.Label(root,text="it is submited",fg="red")
    l1.pack()
button=tk.Button(root,text="submit",bg="yellow",command=check)
button.pack(side="bottom")

root.mainloop()
