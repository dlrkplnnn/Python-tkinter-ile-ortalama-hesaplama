from tkinter import *
import tkinter as tk

def hesaplama():

    not1 = float(birincinot.get())*0.4
    not2 = float(ikincinot.get())*0.6
    ortalama_not=not1+not2
    
    if 90<=ortalama_not<=100:
        harf_notu="AA"

    elif 85<=ortalama_not<=89:
        harf_notu="BA"

    elif 80<=ortalama_not<=84:
        harf_notu="BB"

    elif 70<=ortalama_not<=79:
        harf_notu="CB"

    elif 60<=ortalama_not<=69:
        harf_notu="CC"

    elif 55<=ortalama_not<=59:
        harf_notu="DC"

    elif 50<=ortalama_not<=54:
        harf_notu="DD"

    elif 40<=ortalama_not<=49:
        harf_notu="FD"
    
    else:
        harf_notu="FF"

    ortalama.config(text=isim.get()+" "+soyisim.get()+":"+"ortalamanız:" +" "+str(ortalama_not)+" "+"Harf notunuz: "+" "+ harf_notu) 

    with open("notlar.txt", "a", encoding="utf-8") as f:
        f.write(isim.get()+" "+soyisim.get()+":"+"1.notunuz" +"="+str(birincinot.get())+","+"2.notunuz"+"="+str(ikincinot.get())
                +","+"ortalamanız"+"="+str(ortalama_not)+","+"Harf notunuz"+"="+ harf_notu+("\n"))
    
    isim.delete(0,END)
    soyisim.delete(0,END)
    birincinot.delete(0,END)
    ikincinot.delete(0,END)

def göster():

    with open("notlar.txt", "r", encoding="utf-8") as f:
        x=f.read()
    cikti.insert(tk.END, x)

def sinifortalamasi():
     
    with open("notlar.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        line=len(lines)
        
    with open("notlar.txt", "r", encoding="utf-8") as f:
        toplam=0

        for i in f:
            ayir=i.split(":") 
            notlar=ayir[1]
            notlar=notlar.split(",")
            ortalamalar=notlar[2] 
            ortalamalar=ortalamalar.split("=")
            ortalama=float(ortalamalar[1])
            toplam += ortalama 

        sinifort=float(toplam/line)
        cikti.insert(tk.END, "Sınıf ortalaması:"+str(sinifort))
    
    
def temizle():

    cikti.delete("1.0", tk.END)
    with open("notlar.txt", "w", encoding="utf-8") as f:
        f.close()

pencere=tk.Tk()
pencere.title("not ortalaması hesaplama")
pencere.geometry('800x600')

isim_etiket=tk.Label(text='İsim: ',font='verdana 10 italic')
isim_etiket.pack()

isim=tk.Entry()
isim.pack()

soyisim_etiket=tk.Label(text='Soyad: ',font='verdana 10 italic')
soyisim_etiket.pack()

soyisim=tk.Entry()
soyisim.pack()

birincinot_etiket=tk.Label(text='1.not: ',font='verdana 10 italic')
birincinot_etiket.pack()

birincinot=tk.Entry()
birincinot.pack()

ikincinot_etiket=tk.Label(text='2.not: ',font='verdana 10 italic')
ikincinot_etiket.pack()

ikincinot=tk.Entry()
ikincinot.pack()

ortalama = tk.Label(pencere, text='-------')
ortalama.pack()

ortalama_hesapla=tk.Button(text="Ekle", command=hesaplama)
ortalama_hesapla.pack()

göster = tk.Button(text='Göster', command=göster)
göster.pack() 

sinifort = tk.Button(text='Sınıf Ortalaması', command=sinifortalamasi)
sinifort.pack() 

cikti =tk.Text(pencere,height=10, width=100)
cikti.pack()

çikis = tk.Button(text='Çıkış', command=pencere.destroy)
çikis.pack() 

sil=tk.Button(text="Temizle",command=temizle)
sil.pack()

tk.mainloop()