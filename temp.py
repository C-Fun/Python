from Tkinter import *

def submit():
    print(u.get())
    p.set(u.get())
    
root = Tk()
root.title("����")
frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)
lab1 = Label(frame, text="��ȡ:")
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

#�󶨶���Entry
u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=0, column=1, sticky='ew', columnspan=2)
lab2 = Label(frame, text="��ʾ:")
lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
p = StringVar()
ent2 = Entry(frame, textvariable=p)
ent2.grid(row=1, column=1, sticky='ew', columnspan=2)
button = Button(frame, text="��¼", command=submit, default='active')
button.grid(row=2, column=1)
lab3 = Label(frame, text="")
lab3.grid(row=2, column=0, sticky=W)
button2 = Button(frame, text="�˳�", command=quit)
button2.grid(row=2, column=2, padx=5, pady=5)

#���´��������ʾ����
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
