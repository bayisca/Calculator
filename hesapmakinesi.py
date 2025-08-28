import tkinter as tk

root = tk.Tk()
root.title("Hesap Makinesi 1")


entrybox = tk.Entry(root,width=50,font=('Arial',48),justify="center") 
entrybox.pack(pady=50) 

frame1 = tk.Frame(root) 
frame1.pack(fill='both', expand=True,padx=0,pady=0,ipady=0)

# Kolonları esnet
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)

# Satırları da esnet (önemli!)
for i in range(3):
    frame1.rowconfigure(i, weight=1)


def sayigir(sayi):
     entrybox.insert(tk.END,sayi)

def islem_sec(op):
    global sayi1,islem

    islem = op
    sayi1 = float(entrybox.get())
    entrybox.delete(0,tk.END)

def hesapla():
    global sayi1,islem
    sayi2 = float(entrybox.get())
    sonuc = 0
    if islem == "+":
       
       sonuc = sayi1+sayi2

    elif islem == "-":
       
       sonuc = sayi1-sayi2

    elif islem == "X":

       sonuc = sayi1*sayi2

    elif islem == "/":
       
       sonuc = sayi1/sayi2

    elif islem == "%":

       sonuc = sayi1%sayi2   

    entrybox.delete(0, tk.END)
    entrybox.insert(tk.END, str(sonuc))  

def temizle():

 entrybox.delete(0, tk.END)    

btn1 = tk.Button(frame1,text="1",font=('Arial',28),command= lambda: sayigir("1"))
btn1.grid(row=1,column=0,sticky="nsew")
btn2 = tk.Button(frame1,text="2",font=('Arial',28),command= lambda: sayigir("2"))
btn2.grid(row=1,column=1,sticky="nsew")
btn3 = tk.Button(frame1,text="3",font=('Arial',28),command= lambda: sayigir("3"))
btn3.grid(row=1,column=2,sticky="nsew")

btn4 = tk.Button(frame1,text="4",font=('Arial',28),command= lambda: sayigir("4"))
btn4.grid(row=2,column=0,sticky="nsew")
btn5 = tk.Button(frame1,text="5",font=('Arial',28),command= lambda: sayigir("5"))
btn5.grid(row=2,column=1,sticky="nsew")
btn6 = tk.Button(frame1,text="6",font=('Arial',28),command= lambda: sayigir("6"))
btn6.grid(row=2,column=2,sticky="nsew")

btn7 = tk.Button(frame1,text="7",font=('Arial',28),command= lambda: sayigir("7"))
btn7.grid(row=3,column=0,sticky="nsew")
btn8 = tk.Button(frame1,text="8",font=('Arial',28),command= lambda: sayigir("8"))
btn8.grid(row=3,column=1,sticky="nsew")
btn9 = tk.Button(frame1,text="9",font=('Arial',28),command= lambda: sayigir("9"))
btn9.grid(row=3,column=2,sticky="nsew")

btn16 = tk.Button(frame1,text="%",font=('Arial',28),command= lambda: islem_sec("%"))
btn16.grid(row=4,column=0,sticky="nsew")
btn17 = tk.Button(frame1,text="0",font=('Arial',28),command= lambda: sayigir("0"))
btn17.grid(row=4,column=1,sticky="nsew")
btn18 = tk.Button(frame1,text=".",font=('Arial',28),command= lambda: sayigir("."))
btn18.grid(row=4,column=2,sticky="nsew")



btn10 = tk.Button(frame1,text="X",font=('Arial',28),command= lambda: islem_sec("X"))
btn10.grid(row=6,column=0,sticky="nsew")
btn11 = tk.Button(frame1,text="/",font=('Arial',28),command= lambda: islem_sec("/"))
btn11.grid(row=6,column=1,sticky="nsew")
btn12 = tk.Button(frame1,text="+",font=('Arial',28),command= lambda: islem_sec("+"))
btn12.grid(row=5,column=0,sticky="nsew")
btn13 = tk.Button(frame1,text="-",font=('Arial',28),command= lambda: islem_sec("-"))
btn13.grid(row=5,column=1,sticky="nsew")
btn14 = tk.Button(frame1,text="=",font=('Arial',28),command= hesapla)
btn14.grid(row=6,column=2,sticky="nsew")
btn15 = tk.Button(frame1,text="C",font=('Arial',28),command= temizle)
btn15.grid(row=5,column=2,sticky="nsew")











           



    
             


root.mainloop()
