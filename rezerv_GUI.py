# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

pencere = Tk()
pencere.geometry("700x500")

pencere.title("Python GUI")

L1 = Label(pencere, text="Name:")
L2 = Label(pencere, text="Surname:")
L3 = Label(pencere, text="Communication:")
L4 = Label(pencere, text="How many people will you be:")
L5 = Label(pencere, text="Choose the Location:")
L6 = Label(pencere, text="Kids:")
L7 = Label(pencere, text="Adults:")
L8 = Label(pencere, text="How many nigts will you stay:")
L9 = Label(pencere, text="")
L10 = Label(pencere, text="")
L11=Label(pencere, text="")
L12=Label(pencere, text="", font=("Arial", 10))
L13=Label(pencere, text="FAMILY has 100, DELUXE has 50, KING_SUIT has 10 person capasity", font=("Arial", 10))

L1.grid(row=0,column=0)
L2.grid(row=1,column=0)
L3.grid(row=2,column=0)
L4.grid(row=16,column=0)
L5.grid(row=21,column=0)
L6.place(x=160,y=152)
L7.grid(row=17,column=2)
L8.grid(row=19,column=0)
L9.grid(row=18,column=0)
L10.grid(row=20,column=0)
L11.place(x=180,y=290)
L12.place(x=320,y=290)
L13.place(x=200,y=360)


entryName=Entry(pencere)
entryName.grid(row=0,column=1)

entryS_Name=Entry(pencere)
entryS_Name.grid(row=1,column=1)

entryTel=Entry(pencere)
entryTel.grid(row=2,column=1)

entryKid=Entry(pencere)
entryKid.grid(row=17, column=1)
entryKid.config(textvariable=0)
entryKid.insert(END,'0')

entryAdult=Entry(pencere)
entryAdult.grid(row=17, column=3)
entryAdult.insert(END,'0')

entryDay=Entry(pencere)
entryDay.grid(row=19, column=1)

liste=[[[[],[]],[[],[]],[[],[]]],[[[],[]],[[],[]],[[],[]]],[[[],[]],[[],[]],[[],[]]]]
dosya = open("C:\\Users\\irems\\OneDrive\\Masaüstü\\OdevEk\\pythonGUI.txt","r")
b=[]
for line in dosya:
    b.append(line)

for i in range(3):
    for j in range(3):
        for k in range(2):
            liste[i][j][k]=b[k+(2*j)+(3*2*i)]   #fiyatlar dosyadan çekilmiştir.
print(liste)
oda={"FAMILY":0,"DELUXE":1,"KING_SUIT":2}
FAMILY={'0':100,'1':100,'2':100}
DELUXE={"0":50,"1":50,"2":50}
KING_SUIT={"0":10,"1":10,"2":10}

print(oda["DELUXE"])
print(type(FAMILY))

def total():
    kid = entryKid.get()
    adult = entryAdult.get()
    day = entryDay.get()
    i=v.get() #tatil yeri
    j=roomchoosen.get()  #oda türü

    if (day == "" or kid == "" or adult == ""):
        L11.config(text="Field can not be empty", font=("Arial", 10))
    # elif (kid == "" and adult == ""):
    #     L11.config(text="Kişi sayısı boş olamaz", font=("Arial", 10))
    else:
        L11.config(text="", font=("Arial", 12))
        total =int(day)*((int(kid)*int(liste[int(i)][(oda[j])][1]))+(int(adult)*int(liste[int(i)][(oda[j])][0])))
        #entryKid.delete(0, END)
        L11.config(text=(str(total)+"0$"))

def bilgiAl():
    name=entryName.get()
    sName=entryS_Name.get()
    tel=entryTel.get()
    if(name=="" or sName=="" or tel==""):
        return 0
    elif (len(tel)!=11):
        return 1
    else:
        return 2

def rezervasyon():
    kid = entryKid.get()
    adult = entryAdult.get()
    day = entryDay.get()
    i=v.get()
    j=roomchoosen.get()
    a=eval(j)

    if (day == "" or kid == "" or adult == "" or bilgiAl()==0 or (kid=='0' and adult=='0')):
        L12.config(text="Field can not be empty", font=("Arial", 10))
    # elif (kid == "0"and adult=="0"):
    #     L12.config(text="Kişi sayısı boş olamaz", font=("Arial", 12))
    elif(bilgiAl()==1):
        L12.config(text="Tel number should contain 11 number", font=("Arial", 10))
    elif((a[i]- int(kid) - int(adult))<0):
        L12.config(text="There are no available rooms in this quantity, Rezervation failed")
    else:
        a.update({(str(i), (a[str(i)] - int(kid) - int(adult)))})
        L12.config(text="Reservation has done behalf %s %s" %(entryName.get(),entryS_Name.get()), font=("Arial", 10))
        #L1.config(text=a[i])

def cıkıs():
    pencere.quit()

def reset():
    i = v.get()
    j = roomchoosen.get()
    a=eval(j)

    entryKid.delete(0,END)
    entryAdult.delete(0,END)
    entryDay.delete(0,END)
    L12.config(text="")

    entryKid.insert(END, '0')
    entryAdult.insert(END, '0')
    L11.config(text="")

btn=Button(text="Total",command=total)
btn.place(x=190,y=260)

btn2=Button(text="Rezervation",command=rezervasyon)
btn2.place(x=290,y=260)

btn3=Button(text="Reset",command=reset)
btn3.place(x=390,y=260)

btn4=Button(text="Exit",command=cıkıs)
btn4.place(x=490,y=260)

v = StringVar(pencere, "1")

values = {"Bodrum   ": "0",
          "Çeşme      ": "1",
          "Marmaris ": "2"}

for (text, value) in values.items():
    Radiobutton(pencere, text=text, variable=v,
                value=value).grid(column=0)


ttk.Label(pencere, text="Select the Room:",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)
n = StringVar()
roomchoosen = ttk.Combobox(pencere, width=27,
                           textvariable=n)

roomchoosen['values'] = ('FAMILY',
                          'DELUXE',
                          'KING_SUIT',
                          )
roomchoosen.grid(column=1, row=15)

roomchoosen.current(1)

mainloop()