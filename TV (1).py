from tkinter import *
import string
from random import randint, choice
from tkinter.messagebox import *

nbfois = 10
x = 670
y = 180


def generer_code():
    all_chars = string.digits
    code_g = "".join(choice(all_chars) for i in range(4))
    while not verifier_deux_a_deux_different(code_g):
        code_g = "".join(choice(all_chars) for i in range(4))
    print(code_g)
    return code_g


def verifier_longeur(code):
    if len(code) == 4:
        return True


def verifier_deux_a_deux_different(code):
    for i in range(3):
        for j in range(i + 1, 4):
            if code[i] == code[j]:
                return False
    return True


def verifier_tous_des_chiffres(code):
    nb = 0
    for i in range(4):
        if code[i] not in string.digits:
            nb = nb + 1
    if nb == 0:
        return True


def verifier_code_correcte(code, code_generer):
    T = 0
    V = 0
    i = 1
    global y

    for i in range(4):
        if code[i] == code_generer[i]:
            T = T + 1
        elif code[i] in code_generer:
            V = V + 1

    res = Label(scr1, text=code + " :     " + str(T) + " T    " + str(V) + " V     ", bg="black", fg="#FCDCCE",
                font=font_btn)
    res.pack()
    y = y + 25
    res.place(x=x, y=y)

    if T == 4:
        showinfo('YOU WIN', 'BRAVO ! vous avez gagné')
        e1.delete(0, len(code))
        scr1.destroy()
    else:
        e1.delete(0, len(code))  # pour effacer le continue de l entry


def game():
    global nbfois
    code = e1.get()
    if code != "":
        if not verifier_longeur(code):
            showwarning('Erreur', 'votre code doit contenir exactement 4 chiffres ')
            e1.delete(0, len(code))
        elif not verifier_tous_des_chiffres(code):
            showwarning('Erreur', 'votre code doit contenir seulement des chiffres ')
            e1.delete(0, len(code))
        elif not verifier_deux_a_deux_different(code):
            showwarning('Erreur', 'votre code doit contenir  4 chiffres  deux a deux differents ')
            e1.delete(0, len(code))
        else:
            verifier_code_correcte(code, code_generer)
    nbfois -= 1
    print(nbfois)
    compteur = Label(scr1, text="Il vous reste " + str(nbfois) + " tentative ", fg="red", bg="black", font=font_btn,
                     width=25, height=3)
    compteur.pack()
    compteur.place(x=125, y=140)
    if nbfois < 0:
        showinfo('YOU LOSE', 'Vous avez perdu !!!!et le code secret cherche est ' + code_generer)
        if askyesno('Let''s play again', 'Voulez-vous rejoué????????'):
            showinfo('join us','goooood')
            # start_game()
        else:
            quit()


def start_game():
    screen.destroy()
    global e1
    global scr1
    global bsubmit
    global code_generer

    scr1 = Tk()
    scr1.title("Le jeux a commencé !!! ")
    scr1.geometry("1000x600")
    scr1.resizable(width=False, height=False)
    my_font1 = ('Times', 20, 'bold')
    my_font2 = ('Times', 20, 'bold')
    my_font3 = ('Times', 30, 'bold')
    welcome_text1 = Label(scr1, text="Jeux de TAUREAUX & VACHES ", font=my_font1, fg="#A54F49", bg="#FCC1AA", width=250)
    welcome_text1.pack()
    text2 = Label(scr1, text="BON CHANCE !!!", font=my_font1, fg="#A54F49", bg="#FCC1AA", width=250)
    text2.pack(side=BOTTOM)
    txt1 = Label(scr1, text="Entrer votre proposition :", font=my_font2)
    txt1.place(x=90, y=250)
    e1 = Entry(scr1, highlightcolor="gray", width=45)
    e1.place(x=100, y=310)
    code_generer = generer_code()
    bsubmit = Button(scr1, text="ENTRER", fg="black", bg="#FCDCCE", font=font_btn, width=35, height=2,
                     activebackground="#A8B6BB", command=game)
    bsubmit.place(x=90, y=360)
    rectangle = Canvas(scr1, bg="#FCDCCE", width=200, height=300, bd=50, highlightthickness=3,
                       highlightbackground="black")
    rectangle.pack(side='right', padx=85, pady=60)
    text3 = Label(scr1, text="Historique : ", font=my_font3, bg="#FCDCCE")
    text3.place(x=658, y=120)
    text4 = Label(scr1, text="T :Taureau     V: Vache", font=font_btn, bg="#FCDCCE")
    text4.place(x=675, y=170)

    scr1.mainloop()


if __name__ == '__main__':
    screen = Tk()
    screen.title("Jeu Taureaux et vaches ")
    # screen.iconbitmap('5.ico')
    screen.geometry("1200x600")  # dimnsion du screen
    screen.resizable(width=True, height=True)
    screen.config(background="#FFFFFF")
    photo = PhotoImage(file="vache et taureau.png")  # creation os object
    bv = Label(screen, image=photo, width=500, height=205)
    bv.pack()

    my_font = ('Times', 50, 'bold')
    my_font2 = ('Times', 15, 'bold')
    font_btn = ('Comic Sans MS', 10, 'bold')
    welcome_text = Label(screen, text="Jeu Taureaux et Vaches", font=my_font, fg="#A54F49", bg="#FCC1AA", width=500)
    welcome_text.pack()
    bstart = Button(screen, text="START", fg="black", bg="#FCDCCE", font=font_btn, width=20, height=3,
                    command=start_game)

    bstart.place(x=150, y=340)
    bquit = Button(screen, text="QUIT", fg="black", bg="#FCDCCE", font=font_btn, width=20, height=3,
                   activebackground="#A8B6BB", command=quit)
    bquit.place(x=150, y=450)
    welcome_text2 = Label(screen, text="Preparé par : FARAH FEKIH & HADIL ROMDHANE", font=my_font2, fg="#A54F49",
                          bg="#FCC1AA",
                          activebackground="#A8B6BB", width=250)
    welcome_text2.pack(side=BOTTOM)
    c_width = 600
    c_height = 200
    canvas = Canvas(screen, width=c_width, height=c_height)
    canvas.place(x=500, y=330)
    canvas.create_text(300, 90,
                       text="LES REGLES DU JEU  : \n"
                            "1-le code saisie doit être composé de 4 chiffres différents  \n "
                            "2- s'il y a n chiffres du code saisie qui existent dans CS et ayant \nle même rang que celles dans le CS le programme affichera nT \n "
                            "3- s'il y a m chiffres du code saisie qui existent dans CS et n'ayant\n pas le même rang que celles dans le CS le programme affichera n V\n "
                            "4- vous avez 10 tentative ",
                       font=font_btn
                       )
    screen.mainloop()
