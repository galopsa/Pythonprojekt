from tkinter import *
import time
vikno = Tk()
vikno.title('Значення полінома в точці [x]')



polinomL=Label(vikno, text ='Введіть довільний поліном:')
polinomL.grid(row=0,column=2)
polinom=Entry(vikno)
polinom.grid(row=1,column=2)
polinom.get()


xL=Label(vikno, text ='Введіть значення [x]:')
xL.grid(row=2,column=2)
xL=Entry(vikno)
xL.grid(row=3,column=2)
xL.get()



vikno.mainloop()
