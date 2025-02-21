from tkinter import*
root=Tk()
canvas=Canvas(root,width=400,height=400,bg="black")
canvas.pack()
canvas.create_line(0,0,400,400,fill="white")
canvas.create_rectangle(40,50,300,200,fill="yellow")
canvas.create_oval(69,79,250,25,fill="red")
canvas.create_polygon(40,50,68,79,68,89)
root.mainloop()
