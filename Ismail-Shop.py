import tkinter as tk
import time


name = input ("Hallo. Wie ist dein Name?")
print ("Hallo " + name + ". Willkommen zu Battlenight!")
code = input("Willst du dich mit Zwacktus Hacker acc. verknüpfen?")
if code == "Yes":
    code2 = input ("Was ist das Passwort?")
    if code2 == "899#lol#Hack_90":
 class Account:
    def __init__(self):
        self.balance = 1000  # Startguthaben des Kontos

    def spin_wheel(self):
        if self.balance >= 10:
            self.balance -= 10
            return True
        else:
            return False

def button_click():
    loading_label.place(x=10, y=10)
    root.update()
    root.after(5000, loading_done)  # Warte für 5 Sekunden und rufe dann loading_done auf

def loading_done():
    loading_label.place_forget()
    create_toolbar(root)

def button_click_action(button_text):
    # Ändere den Hintergrund des Fensters auf blau
    root.configure(bg="blue")
    # Drucke den Text des angeklickten Buttons
    print(button_text)
    if button_text == "Shop":
        show_shop_menu()

def show_shop_menu():
    shop_window = tk.Toplevel(root)
    shop_window.title("Shop")

    # Kasten für das OG-Mod Menü
    og_mod_label = tk.Label(shop_window, text="OG-Mod Menü für 10€", padx=10, pady=5)
    og_mod_label.grid(row=0, column=1)

    # Kasten für das Angebot "No Ads Pack für 10€ Monatlich"
    no_ads_label = tk.Label(shop_window, text="No Ads Pack für 10€ Monatlich", padx=10, pady=5)
    no_ads_label.grid(row=0, column=0)

    # Glücksrad mit Angeboten
    wheel_frame = tk.Frame(shop_window)
    wheel_frame.grid(row=1, column=1)
    wheel_label = tk.Label(wheel_frame, text="Glücksrad", padx=10, pady=5)
    wheel_label.pack()
    spin_button = tk.Button(wheel_frame, text="Spin", command=spin_wheel)
    spin_button.pack()
    free_spin_label = tk.Label(wheel_frame, text="Eine kostenfreie Benutzung jeden Tag")
    free_spin_label.pack()
    cost_label = tk.Label(wheel_frame, text="Sonst 10€")
    cost_label.pack()

def spin_wheel():
    if account.spin_wheel():
        print("Wheel spinning...")
        # Hier kann die Logik für den Spinning-Vorgang implementiert werden
    else:
        print("Nicht genug Geld auf dem Konto!")

# Konto initialisieren
account = Account()

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

    # Erstelle den "Start"-Knopf unten links
    start_button = tk.Button(parent, text="Start", padx=10, pady=5, command=start_button_click)
    start_button.place(x=10, y=parent.winfo_reqheight() - 50)  # Platziere den Start-Button unten links

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()

else:
class Account:
    def __init__(self):
        self.balance = 1000  # Startguthaben des Kontos

    def spin_wheel(self):
        if self.balance >= 10:
            self.balance -= 10
            return True
        else:
            return False

def button_click():
    loading_label.place(x=10, y=10)
    root.update()
    root.after(5000, loading_done)  # Warte für 5 Sekunden und rufe dann loading_done auf

def loading_done():
    loading_label.place_forget()
    create_toolbar(root)

def button_click_action(button_text):
    # Ändere den Hintergrund des Fensters auf blau
    root.configure(bg="blue")
    # Drucke den Text des angeklickten Buttons
    print(button_text)
    if button_text == "Shop":
        show_shop_menu()

def show_shop_menu():
    shop_window = tk.Toplevel(root)
    shop_window.title("Shop")

    # Kasten für das OG-Mod Menü
    og_mod_label = tk.Label(shop_window, text="OG-Mod Menü für 10€", padx=10, pady=5)
    og_mod_label.grid(row=0, column=1)

    # Kasten für das Angebot "No Ads Pack für 10€ Monatlich"
    no_ads_label = tk.Label(shop_window, text="No Ads Pack für 10€ Monatlich", padx=10, pady=5)
    no_ads_label.grid(row=0, column=0)

    # Glücksrad mit Angeboten
    wheel_frame = tk.Frame(shop_window)
    wheel_frame.grid(row=1, column=1)
    wheel_label = tk.Label(wheel_frame, text="Glücksrad", padx=10, pady=5)
    wheel_label.pack()
    spin_button = tk.Button(wheel_frame, text="Spin", command=spin_wheel)
    spin_button.pack()
    free_spin_label = tk.Label(wheel_frame, text="Eine kostenfreie Benutzung jeden Tag")
    free_spin_label.pack()
    cost_label = tk.Label(wheel_frame, text="Sonst 10€")
    cost_label.pack()

def spin_wheel():
    if account.spin_wheel():
        print("Wheel spinning...")
        # Hier kann die Logik für den Spinning-Vorgang implementiert werden
    else:
        print("Nicht genug Geld auf dem Konto!")

# Konto initialisieren
account = Account()

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

    # Erstelle den "Start"-Knopf unten links
    start_button = tk.Button(parent, text="Start", padx=10, pady=5, command=start_button_click)
    start_button.place(x=10, y=parent.winfo_reqheight() - 50)  # Platziere den Start-Button unten links

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()   

else:
class Account:
    def __init__(self):
        self.balance = 1000  # Startguthaben des Kontos

    def spin_wheel(self):
        if self.balance >= 10:
            self.balance -= 10
            return True
        else:
            return False

def button_click():
    loading_label.place(x=10, y=10)
    root.update()
    root.after(5000, loading_done)  # Warte für 5 Sekunden und rufe dann loading_done auf

def loading_done():
    loading_label.place_forget()
    create_toolbar(root)

def button_click_action(button_text):
    # Ändere den Hintergrund des Fensters auf blau
    root.configure(bg="blue")
    # Drucke den Text des angeklickten Buttons
    print(button_text)
    if button_text == "Shop":
        show_shop_menu()

def show_shop_menu():
    shop_window = tk.Toplevel(root)
    shop_window.title("Shop")

    # Kasten für das OG-Mod Menü
    og_mod_label = tk.Label(shop_window, text="OG-Mod Menü für 10€", padx=10, pady=5)
    og_mod_label.grid(row=0, column=1)

    # Kasten für das Angebot "No Ads Pack für 10€ Monatlich"
    no_ads_label = tk.Label(shop_window, text="No Ads Pack für 10€ Monatlich", padx=10, pady=5)
    no_ads_label.grid(row=0, column=0)

    # Glücksrad mit Angeboten
    wheel_frame = tk.Frame(shop_window)
    wheel_frame.grid(row=1, column=1)
    wheel_label = tk.Label(wheel_frame, text="Glücksrad", padx=10, pady=5)
    wheel_label.pack()
    spin_button = tk.Button(wheel_frame, text="Spin", command=spin_wheel)
    spin_button.pack()
    free_spin_label = tk.Label(wheel_frame, text="Eine kostenfreie Benutzung jeden Tag")
    free_spin_label.pack()
    cost_label = tk.Label(wheel_frame, text="Sonst 10€")
    cost_label.pack()

def spin_wheel():
    if account.spin_wheel():
        print("Wheel spinning...")
        # Hier kann die Logik für den Spinning-Vorgang implementiert werden
    else:
        print("Nicht genug Geld auf dem Konto!")

# Konto initialisieren
account = Account()

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

    # Erstelle den "Start"-Knopf unten links
    start_button = tk.Button(parent, text="Start", padx=10, pady=5, command=start_button_click)
    start_button.place(x=10, y=parent.winfo_reqheight() - 50)  # Platziere den Start-Button unten links

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()
