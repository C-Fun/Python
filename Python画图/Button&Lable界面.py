# -*- coding: cp936 -*-
from Tkinter import *
def Start():
    global x
    y = x.get()
    print y

window = Tk()
window.title('The weather of the city in China searching')
lblTag = Label(window, text='City')
lblTag.grid(row=0,column=0,padx=25,pady=5)

x = StringVar()
entCity = Entry(window, width=20,textvariable=x)
entCity.grid(row=0,column=1,padx=25,pady=5)


btnPost = Button(window, text='Post',bg='white',command=Start)
btnPost.grid(row=1, column=0,columnspan=2,sticky=EW)
window.mainloop()
