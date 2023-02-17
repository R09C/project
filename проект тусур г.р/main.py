from tkinter import * 
from tkinter import scrolledtext 
from technical.strToMass import strTOMass
from merge_sort.merge_sort import merge_sort
from sor_v.sort_v import sort_v
from technical.save import save


def clicked_save1():
    res = format(txt1.get())
    res=strTOMass(res)
    res=merge_sort(res)
    save(res,'merge_sort.txt')
    txt.insert(INSERT, f"\nДанные сохранены успешно в merge_sort.txt")

def clicked_save2():
    res = format(txt2.get())
    res=strTOMass(res)
    res=sort_v(res)
    save(res,'sort_v.txt')
    txt.insert(INSERT, f"\nДанные сохранены успешно в sort_v.txt")
  
def clean1():
    txt1.delete(0, END)

def clean2():
    txt2.delete(0, END)

def clicked1():  
    res = format(txt1.get())
    res=strTOMass(res)
    res=merge_sort(res) 
    txt.insert(INSERT, f"\nсортировка слиянием => {res}") 

def clicked2():  
    res = format(txt2.get())
    res=strTOMass(res)
    res=sort_v(res) 
    txt.insert(INSERT, f"\nсортировка выбором => {res}") 
  
  
window = Tk()  
window.title("ТУСУР ван лав")  
window.geometry('800x400')

lbl1 = Label(window, text="Сорт.Слиянием")  
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, text="Сорт.Выбором")  
lbl2.grid(column=0, row=2)


txt1 = Entry(window,width=30)  
txt1.grid(column=1, row=0)
txt2 = Entry(window,width=30)  
txt2.grid(column=1, row=2)  


btn1 = Button(window, text="Сортировать", command=clicked1)  
btn1.grid(column=2, row=0)
btn2 = Button(window, text="Сортировать", command=clicked2)  
btn2.grid(column=2, row=2)
btn3= Button(window, text="Очистить", command=clean1)
btn3.grid(column=3, row=0) 
btn4= Button(window, text="Очистить", command=clean2)
btn4.grid(column=3, row=2)

btn5 = Button(window, text="сохранить", command=clicked_save1)  
btn5.grid(column=4, row=0)
btn6 = Button(window,text="сохранить", command=clicked_save2) 
btn6.grid(column=4, row=2) 


txt = scrolledtext.ScrolledText(window, width=40, height=20)  
txt.grid(column=0, row=10)




window.mainloop()