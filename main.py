from tkinter import *
import customtkinter
import matplotlib
import matplotlib.pyplot as plt
import matan as mat
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None  # canvas for integral
theme_switch = None  # switch for theme in settings
themeFlag = 0  # flag for icoset

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Calculator")
# app.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons")
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
    global canvas
    print("clickinter")
    result = mat.integrate(v)

    result_length = len(result)  # result length for canvas
    figsize_width = max(4, result_length * 0.1)  # 0.1  - coeff
    fig, ax = plt.subplots(figsize=(figsize_width, 2))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    ax.text(0.1, 0.4, '$%s$' % result, size=25, color="black")  # text position

    if canvas:
        canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=30)


def bintegral_event():
    v = StringVar()
    window = app
    back2.pack_forget()
    back3.pack()
    bintegral.pack_forget()
    window.title("Неопределенный интеграл")
    window.geometry("1000x700")
    intergrateEntry.pack(pady=10)
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
    if themeFlag:
        window.wm_iconbitmap(r"icons/icomain.ico")
    else:
        window.wm_iconbitmap(r"icons/icomaininvert.ico")
    window.mainloop()

theme_var = BooleanVar() # bool for switch

def switch_event():
    global themeFlag
    customtkinter.set_appearance_mode("dark" if theme_var.get() else "light")
    if (theme_var.get()):
        themeFlag = 0
        app.wm_iconbitmap(r"icons/icomain.ico")
    else:
        themeFlag = 1
        app.wm_iconbitmap(r"icons/icomaininvert.ico")


def bsettings_event():
    print("button pressed")
    window = app
    bsettings.pack_forget()
    bsections.pack_forget()
    back.pack()
    window.title("Настройки")
    window.geometry("1000x700")
    global theme_switch
    if not theme_switch:
        # Add a switch for changing the theme
        theme_switch = customtkinter.CTkSwitch(
            app,
            text="Dark mode",
            variable=theme_var,
            onvalue=True,
            offvalue=False,
            command=switch_event
        )

    theme_switch.pack()
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def back_s():

    app.title("Student Calculator")
    bsections.pack()
    bsettings.pack()
    back.pack_forget()


def back_m():
    app.title("Student Calculator")
    bsections.pack()
    bsettings.pack()
    back1.pack_forget()
    bmatan.pack_forget()


def back_z():
    app.title("Разделы")
    back2.pack_forget()
    back1.pack()
    bmatan.pack()
    bintegral.pack_forget()


def back_k():
    app.title("Матан")
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
