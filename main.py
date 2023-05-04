import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Calculator")
app.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")
#app.wm_iconbitmap(r"icons/icomain.ico")


def bsections_event():
    print("button pressed")
    window = customtkinter.CTk()
    window.title("Разделы")
    window.geometry("500x500")
    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()
    
def bsettings_event():
    print("button pressed")
    window = customtkinter.CTk()
    window.title("Настройки")
    window.geometry("500x500")
    window.wm_iconbitmap(r"c:/users/kuchi/studcalc/icons/icomain.ico")

    window.mainloop()


bsections = customtkinter.CTkButton(app, text="Разделы", command=bsections_event)
bsettings = customtkinter.CTkButton(app, text="Настройки", command=bsettings_event)
bsections.pack()
bsettings.pack()
app.mainloop()
