from Tkinter import *
def changeColor():
    if btnCalculate["fg"]=="blue":
        btnCalculate["fg"]="red"
    else:
        btnCalculate["fg"]="blue"

window = Tk()
window.title("Button")
btnCalculate=Button(window, text="Calculate",fg="blue",command=changeColor)
btnCalculate.grid(padx=100,pady=15)
window.mainloop()
