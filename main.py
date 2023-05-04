from tkinter import StringVar
import customtkinter
import matan as mat
import matplotlib.pyplot as plt

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Calculator")
app.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")
# app.wm_iconbitmap(r"icons/icomain.ico")


def bmatan_event():

    window = customtkinter.CTk()
    window.title("Матан")
    window.geometry("500x500")
    bintegral = customtkinter.CTkButton(
        window, text="Неопределенный интеграл", command=bintegral_event)
    bintegral.pack()
    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()


def integrate(v):
    print("clickinter")
    str = mat.integrate(v)
    print(str)
    ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    plt.text(0.4,0.4,'$%s$' %str,size=25,color="black")
    plt.show()   


def bintegral_event():
    v = StringVar()
    window = customtkinter.CTk()
    window.title("Неопределнный интеграл")
    window.geometry("500x500")
    intergrateEntry = customtkinter.CTkEntry(
        window, placeholder_text="Введите интегрируемую функцию: ", textvariable=v)
    intergrateEntry.pack(pady=20)
    bintegrate = customtkinter.CTkButton(
        window, text="Вычислить", command=lambda: integrate(intergrateEntry.get()))
    bintegrate.pack(pady=5)

    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()


def bsections_event():
    window = customtkinter.CTk()
    window.title("Разделы")
    window.geometry("500x500")
    bmatan = customtkinter.CTkButton(
        window, text="Матан", command=bmatan_event)
    bmatan.pack()
    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()


def bsettings_event():
    print("button pressed")
    window = customtkinter.CTk()
    window.title("Настройки")
    window.geometry("500x500")
    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()


bsections = customtkinter.CTkButton(
    app, text="Разделы", command=bsections_event)
bsettings = customtkinter.CTkButton(
    app, text="Настройки", command=bsettings_event)
bsections.pack()
bsettings.pack()
app.mainloop()
