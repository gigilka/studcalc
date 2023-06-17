from tkinter import *
import customtkinter
import matplotlib
import matplotlib.pyplot as plt
import matan as mat
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None  # canvas for integral
canvas1 = None  # canvas for derivative
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
    backfSections.pack_forget()
    backfMatan.pack()
    window.title("Матан")
    window.geometry("1000x700")
    bintegral.pack()
    bderivative.pack()
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


def diff(v):
    global canvas1
    result = mat.diff(v)

    result_length = len(result)  # result length for canvas
    figsize_width = max(4, result_length * 0.1)  # 0.1  - coeff
    fig, ax = plt.subplots(figsize=(figsize_width, 2))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    ax.text(0.1, 0.4, '$%s$' % result, size=25, color="black")  # text position

    if canvas1:
        canvas1.get_tk_widget().pack_forget()
    canvas1 = FigureCanvasTkAgg(fig, master=app)
    canvas1.draw()
    canvas1.get_tk_widget().pack(pady=30)


def bintegral_event():
    v = StringVar()
    window = app
    backfMatan.pack_forget()
    backfIntegral.pack()
    bintegral.pack_forget()
    window.title("Неопределенный интеграл")
    window.geometry("1000x700")
    intergrateEntry.pack(pady=10)
    bintegrate.pack(pady=5)
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def bderivative_event():
    v = StringVar()
    window = app
    backfMatan.pack_forget()
    backfDerivative.pack()
    bderivative.pack_forget()
    window.title("Производная")
    window.geometry("1000x700")
    derivativeEntry.pack(pady=10)
    bdiff.pack(pady=5)
    window.wm_iconbitmap(r"icons/icomain.ico")
    window.mainloop()


def bsections_event():
    window = app
    window.title("Разделы")
    window.geometry("1000x700")
    bsections.pack_forget()
    bsettings.pack_forget()
    backfSections.pack()
    bmatan.pack()
    if themeFlag:
        window.wm_iconbitmap(r"icons/icomain.ico")
    else:
        window.wm_iconbitmap(r"icons/icomaininvert.ico")
    window.mainloop()


theme_var = BooleanVar()  # bool for switch


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
    backfSettings.pack()
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


def back_set():

    app.title("Student Calculator")
    bsections.pack()
    bsettings.pack()
    backfSettings.pack_forget()
    theme_switch.pack_forget()


def back_sec():
    app.title("Student Calculator")
    bsections.pack()
    bsettings.pack()
    backfSections.pack_forget()
    bmatan.pack_forget()


def back_mat():
    app.title("Разделы")
    backfMatan.pack_forget()
    backfSections.pack()
    bmatan.pack()
    bintegral.pack_forget()


def back_int():
    app.title("Матан")
    backfIntegral.pack_forget()
    backfMatan.pack()
    bintegral.pack()
    bintegrate.pack_forget()
    intergrateEntry.pack_forget()


def back_der():
    app.title("Матан")
    backfDerivative.pack_forget()
    backfMatan.pack()
    bderivative.pack()
    bdiff.pack_forget()
    derivativeEntry.pack_forget()


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
bderivative = customtkinter.CTkButton(app,
                                      text="Производная",
                                      command=bderivative_event)
intergrateEntry = customtkinter.CTkEntry(
    app, placeholder_text="Введите интегрируемую функцию: ")
derivativeEntry = customtkinter.CTkEntry(
    app, placeholder_text="Введите дифференцируемую функцию: ")
bintegrate = customtkinter.CTkButton(
    app, text="Вычислить", command=lambda: integrate(intergrateEntry.get()))
bdiff = customtkinter.CTkButton(
    app, text="Вычислить", command=lambda: diff(derivativeEntry.get()))
backfSettings = customtkinter.CTkButton(app, text="Назад", command=back_set)
backfSections = customtkinter.CTkButton(app, text="Назад", command=back_sec)
backfMatan = customtkinter.CTkButton(app, text="Назад", command=back_mat)
backfIntegral = customtkinter.CTkButton(app, text="Назад", command=back_int)
backfDerivative = customtkinter.CTkButton(app, text="Назад", command=back_der)
bsections.pack()
bsettings.pack()
app.mainloop()
