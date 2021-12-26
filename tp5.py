from tkinter import * 
import time
import threading
import numpy as np
import random

from numpy.lib.function_base import copy 

def init():
    RESET()
    global liste
    liste=np.random.randint(0,100,random.randint(15,20))
    liste=list(liste)
    for i in range(len(liste)):
        CH.insert(END,str(liste[i])+'\n')
    Valeur.set(int(liste[0]/10)*10)
    POS.config(text=str(int(liste[0]/10)*10))
        
def RESET():
    global sens
    global index
    sens=''
    index=len(liste)+1
    CH.delete(index1='1.0',index2=END)
    Valeur.set(0)   
    POS.config(text=str(0))
def maj(nouvelleValeur): 
    print(nouvelleValeur) 


    
    
def FIFO():
    global index
    if(index>len(liste)-1):
        index=0
        return
    ne=int(liste[index]/10)*10
    POS.config(text=str(ne))
    Valeur.set(ne)
    timer = threading.Timer(1,FIFO)
    timer.start()
    index += 1
    
    
    
def sup(liste):
    x=liste[0]
    list=[]
    for i in range(1,len(liste)):
        if(liste[i]>x):
           list.append(liste[i])
    return list

def inf(liste):
    x=liste[0]
    list=[]
    for i in range(1,len(liste)):
        if(liste[i]<x):
           list.append(liste[i])
    return list



   
    
def start():
    global sens        
    global listesup
    global listeinf
    global index
    
    if(sens=='droite'):
        if(index>=len(listesup)):
            timer = threading.Timer(1,start)
            index = 0
            listesup=[]
            if(len(listeinf)!=0):
                sens='gauche'
                Valeur.set(int(liste[0]/10)*10)
                POS.config(text=str(int(liste[0]/10)*10))
            else:
                sens=''
            timer.start()
        else:
            ne=int(listesup[index]/10)*10
            POS.config(text=str(ne))
            print(ne)
            Valeur.set(ne)
            timer = threading.Timer(1,start)
            timer.start()
            index += 1
    elif(sens=='gauche') :
        if(index>=len(listeinf)):
            timer = threading.Timer(1,start)
            index=0
            listeinf=[]
            if(len(listesup)!=0):
                sens='droite'
                Valeur.set(int(liste[0]/10)*10)
                POS.config(text=str(int(liste[0]/10)*10))
            else:
                sens=''
            timer.start()
        else:
            ne=int(listeinf[index]/10)*10
            POS.config(text=str(ne))
            print(ne)
            Valeur.set(ne)
            timer = threading.Timer(1,start)
            timer.start()
            index += 1
    else:
        return
    
        
        
def ASC():
    global sens
    global listesup
    global listeinf
    global index
    index=0
    listesup=sup(liste)
    listesup.sort()
    listeinf=inf(liste)
    listeinf.sort(reverse=True)
    if(var.get()==1):
        sens='droite'
    elif(var.get()==2):
        sens='gauche'
    start()
        
        
    
    return 
# Création de la fenêtre principale (main window) 
Mafenetre = Tk() 
Mafenetre.geometry('700x500')
Mafenetre.title("TP_5") 

CH=Text(Mafenetre,width=10)
CH.place(x=10,y=30)

var = IntVar()
FS=LabelFrame(Mafenetre,text="Sens")

RD = Radiobutton(FS, text="Droite ", variable=var, value=1)
RD.pack()

RG = Radiobutton(FS, text="Gauche", variable=var, value=2)
RG.pack()

FS.place(x=400,y=280)

position=Label(Mafenetre,text='Position courante')
position.place(x=370,y=360)

POS=Label(Mafenetre,text='')
POS.place(x=500,y=360)

fifo=Button(Mafenetre,text='FIFO',command=FIFO ,width=10,bg='#008B8B',fg='#6495ED')
fifo.config(font=('times',14,'bold'))
fifo.place(x=400,y=100)

asc=Button(Mafenetre,text='ASCENSEUR',command=ASC ,width=10,bg='#008B8B',fg='#6495ED')
asc.config(font=('times',14,'bold'))
asc.place(x=400,y=150)

reset=Button(Mafenetre,text='RESET',command=RESET,width=10,bg='#008B8B',fg='#6495ED')
reset.config(font=('times',14,'bold'))
reset.place(x=400,y=200)

Binit=Button(Mafenetre,text='INIT',command=init,width=10,bg='#008B8B',fg='#6495ED')
Binit.config(font=('times',14,'bold'))
Binit.place(x=200,y=150)

Valeur = StringVar() 
 
# Création d'un widget Scale 
echelle = Scale(Mafenetre,from_=0,to=100,resolution=10,orient=HORIZONTAL,length=670,width=20,label="DISQUE",tickinterval=10,variable=Valeur,command=maj) 
echelle.place(x=10,y=400)


liste = []
listesup=[]
listeinf=[]
#Valeur.set(liste[0])
index=0
sens=''  
#init(liste)

Mafenetre.mainloop()
