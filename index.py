from tkinter import *  # tkinter modülünü çağırmış olduk.

pencere = Tk()  # daha kolay kullanabilmek için kolay bir nesneye atadık.
pencere.title('E-Katolog')  # pencere başlığı
pencere.geometry("800x500")  # pencerenin büyüklüğü
MET = "Mevcut Eserleri Tara"  # kısaltma


def MET():
    bilgi = x.get()
    katalogBilgisi = open(r"metindosyasi.txt", "r")

    if bilgi == "1":  # eğer kullanıcı biri seçmişşe kitapEkle fonksiyonunu çalıştırır.
        kitapEkle()


    elif bilgi == "2":
        yönLendirme2.config(text="E-Katalog Mevcut Kitaplar:", font=("Flux", 15, "bold"),
                            fg="black")  # eğer kullanıcı ikiyi seçmisse mevcut kitaplarımızı gösterir.
        katalogBilgisi.seek(0)

        yönLendirme3.config(text=katalogBilgisi.read(), font=("Dotum", 15))




    elif bilgi == "3":
        hakkındaBilgisi.config(text="Program Mete Özcan tarafından yapılmıştır.", fg="grey", font=("Flux", 12, "bold"))
    # üç seçilmişse uyguluma hakkında bilgi verir.

    elif bilgi == "":
        yönLendirme2["text"] = "Yukarıdaki sayılardan birini yazınız "

    else:
        yönLendirme2["text"] = "Yanlış sayı grdiniz"


def kitapEkle():
    katalogBilgisi = open(r"metindosyasi.txt", "a+")
    x.pack_forget()
    tuş.pack_forget()
    x2.pack()
    tuş2.pack()
    yönLendirme["text"] = "Kataloğa ekleyeceğiniz kitabın bilgilerini arasında \":\" olacak şekilde giriniz:"

    katalogBilgisi.write(x2.get())
    x2.config(text=katalogBilgisi.write("\n"))

    if x2.config(text="2"):
        x2.pack_forget()
        tuş2.pack_forget()
        x.pack()
        tuş.pack()


anaSayfa = Label(text="""Kitap eklemek icin 1 
  Mevcut kitapları görmek için 2
  Program Hakkinda 3 
  """, font=("Dotum", 15, "bold"))
anaSayfa.pack()

yönLendirme = Label(text="Seçimizi yapınız: ", fg="black", font=("dotum", 15, "bold"))
yönLendirme.pack()

x = Entry()
x.pack()
x2 = Entry()

tuş = Button(pencere)
tuş.config(text="Onayla", bg="red", fg="white", activebackground="blue",
           activeforeground="black", font=("Calibri", 12), command=MET)
tuş.pack(expand="yes", anchor="center")

tuş2 = Button(text="Kitap Eklemek İçin Bir Kere Tıklayın", command=kitapEkle, font=(24))

yönLendirme2 = Label(text="")
yönLendirme2.pack()

hakkındaBilgisi = Label(text="")
hakkındaBilgisi.pack()

yönLendirme3 = Label(text="")
yönLendirme3.pack()

UygulamayıKapat = Button(pencere)
UygulamayıKapat.config(text="Çıkış", bg="red", fg="white", activebackground="blue",
                       activeforeground="black", font=("Calibri", 12), command=pencere.destroy)
UygulamayıKapat.pack(side=RIGHT)
pencere.mainloop()  # kullanıcı kapatmadığı sürece açık kalır.
