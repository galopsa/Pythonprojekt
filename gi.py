from tkinter import *

def calc():
    a11 = float(a11E.get())
    a12 = float(a12E.get())
    a13 = float(a13E.get())
    a21 = float(a21E.get())
    a22 = float(a22E.get())
    a23 = float(a23E.get())
    a31 = float(a31E.get())
    a32 = float(a32E.get())
    a33 = float(a33E.get())
    text = ''
    if det.get():
        dete = a11*a22*a33 + a12*a23*a31 + a21*a32*a13 \
               - a31*a22*a13 - a12*a21*a33 - a32*a23*a11
        text += 'Determinant\n' + str(dete) +'\n'
    if mi.get():
        text += 'Minimum\n' + str(min(a11, a12, a13, a21, a22, a23, a31, a32, a33)) + '\n'
    if ma.get():
        text += 'Maximum\n' + str(max(a11, a12, a13, a21, a22, a23, a31, a32, a33)) + '\n'
    if su.get():
        text += 'SumOfElements\n' + str(a11+a12+a13+a21+a22+a23+a31+a32+a33) + '\n'
    if sy.get():
        if a12==a21 and a31==a13 and a32==a23:
            text += 'This matrix is symmetric'
        else: text += 'This matrix is\'nt symmetric'
    res.insert('1.0', text)
    
def clear():
    a11E.delete(0, END)
    a12E.delete(0, END)
    a13E.delete(0, END)
    a21E.delete(0, END)
    a22E.delete(0, END)
    a23E.delete(0, END)
    a31E.delete(0, END)
    a32E.delete(0, END)
    a33E.delete(0, END)
    
w = Tk()
w.title('Дії з матрицею 3 на 3')
matrixL = Label(w, text = 'Ведіть матрицю').grid(row = 0, column = 1)#, columnspan = 3)

a11E = Entry(w)
a11E.grid(row = 1, column = 0)
a11E.get()

a12E = Entry(w)
a12E.grid(row = 1, column = 1)
a12E.get()

a13E = Entry(w)
a13E.grid(row = 1, column = 2)
a13E.get()

a21E = Entry(w)
a21E.grid(row = 2, column = 0)
a21E.get()

a22E = Entry(w)
a22E.grid(row = 2, column = 1)
a22E.get()

a23E = Entry(w)
a23E.grid(row = 2, column = 2)
a23E.get()

a31E = Entry(w)
a31E.grid(row = 3, column = 0)
a31E.get()

a32E = Entry(w)
a32E.grid(row = 3, column = 1)
a32E.get()

a33E = Entry(w)
a33E.grid(row = 3, column = 2)
a33E.get()

detL = Label(w, text = 'Визначник').grid(row = 4, column = 1)
res = Text(w, width = 15, height = 15)
res.grid(row = 5, column = 2, rowspan = 10)

Button(w, text = 'Ok', command = calc).grid(row = 7, column = 1)
Button(w, text = 'Delete', command = clear).grid(row = 8, column = 1)

det = IntVar()
mi = IntVar()
ma = IntVar()
su = IntVar()
sy = IntVar()
Checkbutton(w, text = 'Determinant', var = det).grid(row = 6, column = 0)
Checkbutton(w, text = 'Minimum', var = mi).grid(row = 7, column = 0)
Checkbutton(w, text = 'Maximum', var = ma).grid(row = 8, column = 0)
Checkbutton(w, text = 'SumOfElements', var = su).grid(row = 9, column = 0)
Checkbutton(w, text = 'Symmetric', var = sy).grid(row = 10, column = 0)

w.mainloop()
