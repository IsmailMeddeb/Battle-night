import tkinter as tk
import time


name = input ("Hallo. Wie ist dein Name?")
print ("Hallo " + name + ". Willkommen zu Battlenight")
code = input("Willst du dich mit Zwacktus Hacker acc. verknüpfen")
if code == "Yes":
    code2 = input ("Was ist das Passwort")
    if code2 == "899#lol#Hack_90":
        def button_click():
    # Schalte das Laden-Rechteck ein
    loading_label.place(x=10, y=10)
    root.update()  # Aktualisiere das Fenster, um die Änderungen sofort anzuzeigen
    time.sleep(5)  # Warte für 5 Sekunden
    # Schalte das Laden-Rechteck aus
    loading_label.place_forget()
    # Erstelle die Leiste nach dem Laden-Bildschirm
    create_toolbar(root)

# Funktion zum Erstellen der Leiste
def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    # Elemente der Leiste
    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        element = tk.Label(toolbar, text=element_text, padx=10, pady=5)
        element.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

# Erstellen eines Labels für "Loading"
loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()



else:
    def button_click():
    # Schalte das Laden-Rechteck ein
    loading_label.place(x=10, y=10)
    root.update()  # Aktualisiere das Fenster, um die Änderungen sofort anzuzeigen
    time.sleep(5)  # Warte für 5 Sekunden
    # Schalte das Laden-Rechteck aus
    loading_label.place_forget()
    # Erstelle die Leiste nach dem Laden-Bildschirm
    create_toolbar(root)

# Funktion zum Erstellen der Leiste
def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    # Elemente der Leiste
    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        element = tk.Label(toolbar, text=element_text, padx=10, pady=5)
        element.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

# Erstellen eines Labels für "Loading"
loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()

    else:
        def button_click():
    # Schalte das Laden-Rechteck ein
    loading_label.place(x=10, y=10)
    root.update()  # Aktualisiere das Fenster, um die Änderungen sofort anzuzeigen
    time.sleep(5)  # Warte für 5 Sekunden
    # Schalte das Laden-Rechteck aus
    loading_label.place_forget()
    # Erstelle die Leiste nach dem Laden-Bildschirm
    create_toolbar(root)

# Funktion zum Erstellen der Leiste
def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    # Elemente der Leiste
    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        element = tk.Label(toolbar, text=element_text, padx=10, pady=5)
        element.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

# Erstellen eines Labels für "Loading"
loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()


