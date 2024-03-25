import tkinter as tk
import time


name = input ("Hallo. Wie ist dein Name?")
print ("Hallo " + name + ". Willkommen zu Battlenight!")
code = input("Willst du dich mit Zwacktus Hacker acc. verknüpfen?")
if code == "Yes":
    code2 = input ("Was ist das Passwort?")
    if code2 == "899#lol#Hack_90":
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

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()


else:
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

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()
    else:
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

def create_toolbar(parent):
    toolbar = tk.Frame(parent, bg="lightgray", height=parent.winfo_reqheight()/13)
    toolbar.pack(side="top", fill="x")

    toolbar_elements = ["Battlepass", "Start", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
    for element_text in toolbar_elements:
        button = tk.Button(toolbar, text=element_text, padx=10, pady=5, command=lambda text=element_text: button_click_action(text))
        button.pack(side="left")

root = tk.Tk()
root.title("Mein GUI")

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()

label = tk.Label(root, text="Hallo, das ist mein GUI!")
label.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_click)
button.pack()

# Erstellen eines Labels für "Loading"
loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

root.mainloop()


