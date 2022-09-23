import os
from pickle import TRUE
from fileinput import close
import os
os.system('cls')
from tkinter import *
from PIL import ImageTk
import PIL.Image
import sys
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import tkinter as tk

os.system('cls')

##################################################
conn = sqlite3.connect('teams.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS teams')

cur.execute('CREATE TABLE teams (isim TEXT, değer INTEGER)')
##################################################
handle=open('text3.txt',"a")
root=Tk()
root.title("Welcome to Workers app")
root.geometry("800x570")
bg = PIL.Image.open("Rute_logo.png")
img=bg.resize((350, 350))
my_img=ImageTk.PhotoImage(img)
label1 = Label( root, image = my_img)
label1.place(x = 360,y = 170)
########################

text=Text(root, width=35, height=22,bg = "light cyan")
text.place(x=5,y=200)

sifirmi=0


def sifirla():
    answer = askyesno(title='Onay',message='Verileri silmek istediğinen emin misin ?')
    if answer:
        handle=open('text3.txt',"w")
        text.delete('1.0', END)
        text.insert(END, "isim soyisim            değerlendirmesi\n-----------------------------------")
        sifirmi=1
new = tk.Button(
    root,
    text='Verileri sıfırla.',height=4, width=10,bg='red',
    command=sifirla
)
new.place(x=10, y=80)
########################




text.insert(END, "isim soyisim      değerlendirmesi\n-----------------------------------")
f= open("text3.txt")
#t is a Text widget
text.insert(END, f.read())

#text.insert(END,"\n")


ttk.Label(root,text="Hoş Geldiniz",font=("Arial Bold", 12)).pack()


ttk.Label(root,text ="isim soyisim:",font=("Arial Bold", 10)).pack()
entry1=ttk.Entry(root,width=25)
entry1.pack()

ttk.Label(root,text ="dğerlendirmesi(10 üzerinden):",font=("Arial Bold", 10)).pack()
entry2=ttk.Entry(root,width=25)
entry2.pack()

bu1=ttk.Button(root,text="Ekle",width=25)

bu1.pack()
bu2=tk.Button(root,text="Bu kadar.",height=4, width=10,bg='green')
bu2.pack()
bu2.place(x=600, y=75)
#txtlist=tk.Text(root).pack()
#txtlist.place(x = 180,y = 170)


def buclick():
    isim=entry1.get()
    isler=entry2.get()
    print(isim,isler)


    Text(root)
    handle.write(isim)
    handle.write("\t")
    handle.write(isler)
    handle.write("\n")
    entry1.delete(0,END)
    entry2.delete(0,END)
    #text.get(isim)
    #text.insert(entry1.get())
    text.insert(END, isim+"        "+isler+"\n")


def buclick2():
    cur.execute('DROP TABLE IF EXISTS workers')
    root.destroy()
def disable_event():
   sys.exit()

root.protocol("WM_DELETE_WINDOW", disable_event)   # programın x tuşu or alt+f4
bu1.config(command=buclick)

bu2.config(command=buclick2)
root.resizable(width=False, height=False)




root.mainloop()
########################


##################################################
import os
from pickle import TRUE
import sqlite3

os.system('cls')

##################################################
conn = sqlite3.connect('teams.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS teams')

cur.execute('CREATE TABLE teams (isim TEXT, değer INTEGER)')
##################################################
#algoritma başlangıcı
puanlar=list()
adlar=list()

team1=list()
team2=list()
liste=dict()
team1kisileri=list()
team2kisileri=list()



handle=open('text3.txt')
for line in handle:
    line=line.rstrip()
    a=line.split('\t')
    puanlar.append(int(a[1]))
    adlar.append(a[0])
    liste[a[0]]=liste.get(a[0],a[1])
    cur.execute("INSERT INTO TEAMS (isim,değer) VALUES (?,?)",(a[0],int(a[1])))



temp3=list()
for x in puanlar:
    temp3.append(x)
print('Liste :',liste)

ortalama=sum(puanlar)/2
print('Ortalama :',ortalama)
print(adlar)
print(puanlar)
puanlar.sort()
print("sorted:",puanlar)

birtanedaha=0
if len(puanlar)%2==1:
    birtanedaha=1

x1=(len(puanlar))/2
x1=x1-0.1
print(x1)
x1=round(x1)
print("kişi sayısı",x1)

puanlar2=puanlar[::-1]

z2=len(puanlar)
z=0
while z<x1:
    a=puanlar[0]
    b=puanlar[z2-1-z]
    #print(a)
    #print(b)
    if z%2==0:
        team1.append(a)
        team1.append(b)
        """ team1kisileri.append(adlar[0])
        team1kisileri.append(adlar[z2-1-z]) """
    elif z%2==1:
        team2.append(a)
        team2.append(b)
        """ team2kisileri.append(adlar[0])
        team2kisileri.append(adlar[z2-1-z]) """
    puanlar.remove(a)
    puanlar.remove(b)
    """ adlar.remove(adlar[0])
    adlar.pop() """
    z=z+1
    z2=z2-1

if birtanedaha==1:
    s=puanlar[0]
    team2.append(s)
    puanlar.remove(s)

#team2=puanlar
temp1=team1
temp2=team2


print("team 1 :",team1,"toplam =",sum(team1))
print("team 2 :",team2,"toplam =",sum(team2))

d1=round(ortalama+0.1)
d2=d1-1
print("d1 = ",d1,"d2 = ",d2)

t1=1
if sum(team2) > sum(team1):
    t1=0
    print("team2 sum is higher")

cc=1
print("temp 1 :",temp1)
if t1==0 :
    for x in team1:
        if cc==1:
            for y in team2:
                if sum(team2)-sum(team1)>10 and cc==1:
                    if(abs(x-y))==round((d1-sum(team1))/2) or (abs(x-y))==round((d2-sum(team1))/2):
                        if x<y:
                            temp1.append(y)
                            temp2.append(x)
                            temp1.remove(x)
                            temp2.remove(y)
                            cc=0
                            break

                if((abs(x-y))==abs(d1-sum(team1)) or (abs(x-y))==abs(d2-sum(team1))) and cc==1:
                    if y>x:
                        temp1.append(y)
                        temp2.append(x)
                        temp1.remove(x)
                        temp2.remove(y)
                        print("xxxxxxxxxxxxxx",x,y)
                        cc=0
                        break

if len(team1)>len(team2)+1:
    u=abs(ortalama-sum(team2))
    u=u-0.1
    u1=round(u)
    u2=u1+1
    if u1 in team1 :
        team2.append(u1)
        team1.remove(u1)
    elif u2 in team1:
        team2.append(u2)
        team1.remove(u2)

c=1
for x in team1:
        for y in team2:
            if(sum(temp1)>sum(temp2)) and cc==1:
                if(x-y)==abs(ortalama-sum(team1)) and c==1:
                    print(temp1)
                    temp1.append(y)
                    temp2.append(x)
                    temp1.remove(x)
                    temp2.remove(y)
                    print(x,y)
                    c=0
                    print("zzzzzzzzzzz",temp1)
                    break
if c==1:
    for x in team1:
        for y in team2:
            if ((x-y)==abs(d1-sum(team1)) or (x-y)==abs(d2-sum(team1))) and c==1 and cc==1:
                print(temp1)
                temp1.append(y)
                temp2.append(x)
                temp1.remove(x)
                temp2.remove(y)
                print(x,y)
                c=0
                print("yyyyyyyyy",temp1)
                break
                
""" print("\n\nteam 1 :",team1,"toplam =",sum(team1),team1kisileri)
print("team 2 :",team2,"toplam =",sum(team2),team2kisileri) """
#print("temp 1 :",temp1)


cur.execute('DROP TABLE IF EXISTS team1')
cur.execute('DROP TABLE IF EXISTS team2')
cur.execute("CREATE TABLE team1 (isim TEXT, değer INTEGER)")
cur.execute("CREATE TABLE team2 (isim TEXT, değer INTEGER)")


for x in team1:
    p=temp3.index(x)
    yapan=adlar[p]
    team1kisileri.append(yapan)
    temp3.pop(p)
    adlar.pop(p)

for x in team2:
    p=temp3.index(x)
    yapan=adlar[p]
    team2kisileri.append(yapan)
    temp3.pop(p)
    adlar.pop(p)

for x,y in zip(team1,team1kisileri):
    cur.execute("INSERT INTO team1 (isim,değer) VALUES (?,?)",(y,int(x)))
for x,y in zip(team2,team2kisileri):
    cur.execute("INSERT INTO team2 (isim,değer) VALUES (?,?)",(y,int(x)))



conn.commit()


print("\n\nteam 1 :",team1,"toplam =",sum(team1),", kişileri:",team1kisileri)
print("team 2 :",team2,"toplam =",sum(team2),", kişileri:",team2kisileri)


###############################################
#proogram biitşinde tablo

win = Tk()
win.title("Takımların listesi")
# Set the size of the tkinter window
win.geometry("800x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('winnative')#winnative#clam

# Add a Treeview widget
tree = ttk.Treeview(win, column=("Takım 1 üyeleri", "Takım 2 üyeleri"), show='headings', height=len(team1))
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Takım 1 üyeleri")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Takım 2 üyeleri")




conn = sqlite3.connect("teams.sqlite")
cur = conn.cursor()
cur.execute("SELECT isim FROM team1")
rows = cur.fetchall()
cur.execute("SELECT isim FROM team2")
rows2 = cur.fetchall()
for row,row2 in zip(rows,rows2):
    tree.insert("", tk.END, values=(row,row2))
"""     tree.insert("",column=1,values=row)
    tree.insert("",column=2,values=row2) """
conn.close()

tree.pack()

win.mainloop()


