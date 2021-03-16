# IMPORT MODULE
import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# SET TKINTER
root = Tk()
root.title("Math")
root.iconbitmap("favicon.ico")
root.geometry("500x700")
pygame.init()

# SOUND
mixer.music.load("sound.mp3")
mixer.music.play(-1)

# BACKGROUND
bg = PhotoImage(file="mulai.png")
lbl = Label(root, image=bg)
lbl.place(x=0,y=0)

image1 = PhotoImage(file="mulai1.png")
image2 = PhotoImage(file="materi1.png")
image3 = PhotoImage(file="about1.png")


# MATERI
def materi():
    global img
    global img1
    
    root1 = Toplevel()
    root1.title('Materi')
    root1.iconbitmap("favicon.ico")
    root1.geometry('500x700')
    img = PhotoImage(file='materi.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        materi()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=460, y=0)


def about():
    global img
    global img1
    root1 = Toplevel()
    root1.iconbitmap("favicon.ico")
    root1.title('Materi')
    root1.geometry('500x700')
    img = PhotoImage(file='about.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        materi()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


# SOAL
def soal():
    global img
    global img1
    global img2
    global img3
    global img4
    global img5

    root1 = Toplevel()
    root1.title('Materi')
    root1.iconbitmap("favicon.ico")
    root1.geometry('500x700')
    img = PhotoImage(file='soal.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        materi()

    def tambah():
        game = root1.destroy 
        go = tambah1
        game()
        go()

    img5 = PhotoImage(file="back.png")
    button = Button(root1, image=img5, command=back, bd=0)
    button.place(x=0, y=0)

    img1 = PhotoImage(file="01.png")
    img2 = PhotoImage(file="02.png")
    img3 = PhotoImage(file="03.png")
    img4 = PhotoImage(file="04.png")
    
    button_tambah = Button(root1, image=img1, bd=0, command=tambah)
    button_kurang = Button(root1, image=img2, bd=0, state=DISABLED)
    button_kali = Button(root1, image=img3, bd=0, state=DISABLED)
    button_bagi = Button(root1, image=img4, bd=0, state=DISABLED)

    button_tambah.place(x=135, y=300)
    button_kurang.place(x=245, y=300)
    button_kali.place(x=135, y=410)
    button_bagi.place(x=245, y=410)


# TAMBAH
def tambah1():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 1")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="1.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "22":
            game = root1.destroy
            go = tambah2
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = tambah1
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image=imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = soal
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def tambah2():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 2")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="2.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "50":
            game = root1.destroy
            go = tambah3
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = tambah2
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = tambah1
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def tambah3():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 3")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="3.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "63":
            game = root1.destroy
            go = soal1
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = tambah3
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = tambah2
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def soal1():
    global img
    global img1
    global img2
    global img3
    global img4
    global img5

    root1 = Toplevel()
    root1.title('Soal')
    root1.iconbitmap("favicon.ico")
    root1.geometry('500x700')
    img = PhotoImage(file='soal.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        go = tambah3
        materi()
        go()

    def tambah():
        game = root1.destroy 
        go = tambah1
        game()
        go()

    def kurang():
        game = root1.destroy 
        go = kurang1
        game()
        go()

    img5 = PhotoImage(file="back.png")
    button = Button(root1, image=img5, command=back, bd=0)
    button.place(x=0, y=0)

    img1 = PhotoImage(file="01.png")
    img2 = PhotoImage(file="02.png")
    img3 = PhotoImage(file="03.png")
    img4 = PhotoImage(file="04.png")
    
    button_tambah = Button(root1, image=img1, bd=0, command=tambah)
    button_kurang = Button(root1, image=img2, bd=0, command=kurang)
    button_kali = Button(root1, image=img3, bd=0, state=DISABLED)
    button_bagi = Button(root1, image=img4, bd=0, state=DISABLED)

    button_tambah.place(x=135, y=300)
    button_kurang.place(x=245, y=300)
    button_kali.place(x=135, y=410)
    button_bagi.place(x=245, y=410)


# MINUS
def kurang1():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 1")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="4.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "3":
            game = root1.destroy
            go = kurang2
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kurang1
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = soal1
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def kurang2():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 2")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="5.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "20":
            game = root1.destroy
            go = kurang3
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kurang2
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = kurang1
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def kurang3():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 3")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="6.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "7":
            game = root1.destroy
            go = soal2
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kurang3
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = kurang2
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def soal2():
    global img
    global img1
    global img2
    global img3
    global img4
    global img5

    root1 = Toplevel()
    root1.title('Soal')
    root1.iconbitmap("favicon.ico")
    root1.geometry('500x700')
    img = PhotoImage(file='soal.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        go = kurang3
        materi()
        go()

    def tambah():
        game = root1.destroy 
        go = tambah1
        game()
        go()

    def kurang():
        game = root1.destroy 
        go = kurang1
        game()
        go()

    def kali():
        game = root1.destroy 
        go = kali1
        game()
        go()

    img5 = PhotoImage(file="back.png")
    button = Button(root1, image=img5, command=back, bd=0)
    button.place(x=0, y=0)

    img1 = PhotoImage(file="01.png")
    img2 = PhotoImage(file="02.png")
    img3 = PhotoImage(file="03.png")
    img4 = PhotoImage(file="04.png")
    
    button_tambah = Button(root1, image=img1, bd=0, command=tambah)
    button_kurang = Button(root1, image=img2, bd=0, command=kurang)
    button_kali = Button(root1, image=img3, bd=0, command=kali)
    button_bagi = Button(root1, image=img4, bd=0, state=DISABLED)

    button_tambah.place(x=135, y=300)
    button_kurang.place(x=245, y=300)
    button_kali.place(x=135, y=410)
    button_bagi.place(x=245, y=410)


# KALI
def kali1():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 1")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="7.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban1():
        hello = e.get()

        if hello == "40":
            game = root1.destroy
            go = kali2
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kali1
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban1)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = soal2
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def kali2():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 2")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="8.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "20":
            game = root1.destroy
            go = kali3
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kali2
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = kali1
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def kali3():
    global image
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 3")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    image = PhotoImage(file="9.png")
    label = Label(root1, image=image)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "8":
            game = root1.destroy
            go = soal3
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = kali3
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = kali2
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def soal3():
    global img
    global img1
    global img2
    global img3
    global img4
    global img5

    root1 = Toplevel()
    root1.title('Soal')
    root1.iconbitmap("favicon.ico")
    root1.geometry('500x700')
    img = PhotoImage(file='soal.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        go = kali3
        materi()
        go()

    def tambah():
        game = root1.destroy 
        go = tambah1
        game()
        go()

    def kurang():
        game = root1.destroy 
        go = kurang1
        game()
        go()

    def kali():
        game = root1.destroy 
        go = kali1
        game()
        go()

    def bagi():
        game = root1.destroy 
        go = bagi1 
        game()
        go()

    img5 = PhotoImage(file="back.png")
    button = Button(root1, image=img5, command=back, bd=0)
    button.place(x=0, y=0)

    img1 = PhotoImage(file="01.png")
    img2 = PhotoImage(file="02.png")
    img3 = PhotoImage(file="03.png")
    img4 = PhotoImage(file="04.png")
    
    button_tambah = Button(root1, image=img1, bd=0, command=tambah)
    button_kurang = Button(root1, image=img2, bd=0, command=kurang)
    button_kali = Button(root1, image=img3, bd=0, command=kali)
    button_bagi = Button(root1, image=img4, bd=0, command=bagi)

    button_tambah.place(x=135, y=300)
    button_kurang.place(x=245, y=300)
    button_kali.place(x=135, y=410)
    button_bagi.place(x=245, y=410)


# BAGI
def bagi1():
    global imaged
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 1")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    imaged = PhotoImage(file="10.png")
    label = Label(root1, image=imaged)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "4":
            game = root1.destroy
            go = bagi2
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = bagi1
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = soal3
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def bagi2():
    global imaged
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 2")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    imaged = PhotoImage(file="11.png")
    label = Label(root1, image=imaged)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "10":
            game = root1.destroy
            go = bagi3
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = bagi2
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        go = bagi1
        materi = root1.destroy
        go()
        materi()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


def bagi3():
    global imaged
    global imagee
    global img1

    root1 = Toplevel()
    root1.title("Soal 3")
    root1.iconbitmap("favicon.ico")
    root1.geometry("500x700")

    imaged = PhotoImage(file="12.png")
    label = Label(root1, image=imaged)
    label.place(x=0,y=0)

    e = Entry(root1, width=50)
    e.place(x=90,y=350)

    def jawaban():
        hello = e.get()

        if hello == "5":
            game = root1.destroy
            go = end
            game()
            go()
        else:
            messagebox.askokcancel("info","Jawaban anda salah, coba lagi...")
            game = root1.destroy
            go = bagi3
            game()
            go()

    imagee = PhotoImage(file="cek.png")
    button = Button(root1, image= imagee, command=jawaban)
    button.place(x=120,y=380)

    def back():
        materi = root1.destroy
        go = bagi2
        materi()
        go()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=0, y=0)


# END
def end():
    global img
    global img1
    
    root1 = Toplevel()
    root1.title('END')
    
    root1.geometry('500x700')
    img = PhotoImage(file='end.png')
    lbl = Label(root1, image=img)
    lbl.place(x=0,y=0)

    def back():
        materi = root1.destroy
        game = root1.destroy
        materi()
        game()

    img1 = PhotoImage(file="back.png")
    button = Button(root1,bd=0, image=img1, command=back)
    button.place(x=460, y=0)


# BUTTON
btn = Button(root, image=image1 ,command=soal, bd=0)
btn1 = Button(root, image=image2 ,command=materi, bd=0)
btn2 = Button(root, image=image3 ,command=about, bd=0)
btn.place(x=120,y=310)
btn1.place(x=120,y=370)
btn2.place(x=120,y=430)

# GAME LOOP
root.mainloop()