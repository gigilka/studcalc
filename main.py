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
#app.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons")
app.wm_iconbitmap(r"icons/icomain.ico")


def bmatan_event():

    window = app
    bmatan.pack_forget()
    back1.pack_forget()
    back2.pack()
    window.title("Матан")
    window.geometry("1000x700")
    bintegral.pack()
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def integrate(v):

    print("clickinter")
    str = mat.integrate(v)
    print(str)
    ax = plt.axes([0, 0, 0.3, 0.3])  #left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    plt.text(0.4, 0.4, '$%s$' % str, size=25, color="black")
    plt.show()


def bintegral_event():
    v = StringVar()
    window = app
    back2.pack_forget()
    back3.pack()
    bintegral.pack_forget()
    window.title("Неопределнный интеграл")
    window.geometry("1000x700")
    intergrateEntry.pack(pady=30)
    bintegrate.pack(pady=5)
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def bsections_event():
    window = app
    window.title("Разделы")
    window.geometry("1000x700")
    bsections.pack_forget()
    bsettings.pack_forget()
    back1.pack()
    bmatan.pack()
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def bsettings_event():
    print("button pressed")
    window = app
    bsettings.pack_forget()
    bsections.pack_forget()
    back.pack()
    window.title("Настройки")
    window.geometry("1000x700")
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()

def back_s():
    bsections.pack()
    bsettings.pack()
    back.pack_forget()


def back_m():
    bsections.pack()
    bsettings.pack()
    back1.pack_forget()
    bmatan.pack_forget()


def back_z():
    back2.pack_forget()
    back1.pack()
    bmatan.pack()
    bintegral.pack_forget()


def back_k():
    back3.pack_forget()
    back2.pack()
    bintegral.pack()
    bintegrate.pack_forget()
    intergrateEntry.pack_forget()


bmatan = customtkinter.CTkButton(app, text="Матан", command=bmatan_event)
bsections = customtkinter.CTkButton(app,
                                    text="Разделы",
                                    command=bsections_event)
bsettings = customtkinter.CTkButton(app,
                                    text="Настройки",
                                    command=bsettings_event)
bintegral = customtkinter.CTkButton(app,
                                    text="Неопределенный интеграл",
                                    command=bintegral_event)
intergrateEntry = customtkinter.CTkEntry(
    app, placeholder_text="Введите интегрируемую функцию: ")
bintegrate = customtkinter.CTkButton(
    app, text="Вычислить", command=lambda: integrate(intergrateEntry.get()))
back = customtkinter.CTkButton(app, text="Назад", command=back_s)
back1 = customtkinter.CTkButton(app, text="Назад", command=back_m)
back2 = customtkinter.CTkButton(app, text="Назад", command=back_z)
back3 = customtkinter.CTkButton(app, text="Назад", command=back_k)
bsections.pack()
bsettings.pack()
app.mainloop()
