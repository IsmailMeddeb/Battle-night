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


        root = tk.Tk()
        root.title("Battlenight modpack Zwacktus")

        label = tk.Label(root, text="Willkommwn im Spiel")
        label.pack(pady=10)

        button = tk.Button(root, text="Spiel starten", command=button_click)
        button.pack()

        # Erstellen eines Labels für "Loading"
        loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

        root.mainloop()





else:
    code3 = input ("Willst du dich mit Isi Hacker acc verknüpfen")
    if code3 == "Yes":
        code4 = input ("Was ist das Passwort?")
        if code4 == "899#lol#Hack_90_Isi":
            def button_click():
                # Schalte das Laden-Rechteck ein
                loading_label.place(x=10, y=10)
                root.update()  # Aktualisiere das Fenster, um die Änderungen sofort anzuzeigen
                time.sleep(5)  # Warte für 5 Sekunden
                # Schalte das Laden-Rechteck aus
                loading_label.place_forget()


            root = tk.Tk()
            root.title("Battlenight")

            label = tk.Label(root, text="Willkommen im Modpack Isi")
            label.pack(pady=10)

            button = tk.Button(root, text="Spiel starten!", command=button_click)
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
            root = tk.Tk()
            root.title("Battlenight")

            label = tk.Label(root, text="Willkommen im Modpack Isi")
            label.pack(pady=10)

            button = tk.Button(root, text="Spiel starten!", command=button_click)
            button.pack()

            # Erstellen eines Labels für "Loading"
            loading_label = tk.Label(root, text="Loading", bg="blue", fg="white")

            root.mainloop()

