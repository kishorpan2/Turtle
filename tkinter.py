from tkinter import*
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(100,100,300,50)
tk.mainloop()
