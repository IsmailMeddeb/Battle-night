import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Battlenight")

        self.greet_label = tk.Label(self, text="Willkommen zu Battlenight")
        self.greet_label.pack()

        self.register_button = tk.Button(self, text="Registrieren", command=self.register)
        self.register_button.pack()

        self.loading_label = tk.Label(self, text="Loading", bg="lightblue", fg="black", font=("Party LET", 16))
        self.loading_label.place_forget()

        self.current_background = None
        self.daily_spin_used = False

    def register(self):
        self.clear_widgets()

        self.username_label = tk.Label(self, text="Benutzername:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Passwort:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.confirm_label = tk.Label(self, text="Merke dir das Passwort gut")
        self.confirm_label.pack()

        self.create_button = tk.Button(self, text="Account erstellen", command=self.create_account)
        self.create_button.pack()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.clear_widgets()
            self.create_main_menu()
        else:
            self.confirm_label.config(text="Bitte fülle alle Felder aus.")

    def create_main_menu(self):
        self.clear_widgets()

        toolbar = tk.Frame(self, bg="lightgray", height=self.winfo_reqheight()/13)
        toolbar.pack(side="top", fill="x")

        toolbar_elements = ["Battlepass", "Startmenü", "Shop", "Spin", "Battlebucks", "Spind", "Trophäen", "Turnier", "Username"]
        for element_text in toolbar_elements:
            button = tk.Button(toolbar, text=element_text, padx=27, pady=7, command=lambda text=element_text: self.button_click_action(text))
            button.pack(side="left")

        start_button = tk.Button(self, text="Start", padx=40, pady=20, command=self.create_main_menu)
        start_button.place(x=1100, y=self.winfo_reqheight() + 580)

        freunde_button = tk.Button(self, text="Freunde", padx=40, pady=20, command=self.create_main_menu)
        freunde_button.place(x=10, y=self.winfo_reqheight() + 580)

        spielmodus_button = tk.Button(self, text="Spielmodus", padx=40, pady=20, command=self.create_main_menu)
        spielmodus_button.place(x=1070, y=self.winfo_reqheight() + 500)

    def button_click_action(self, button_text):
        self.clear_widgets()
        self.configure(bg="blue")
        back_button = tk.Button(self, text="Back", padx=10, pady=5, command=self.create_main_menu)
        back_button.place(x=10, y=self.winfo_reqheight() - 30)

        if button_text == "Shop":
            self.create_shop_menu()
        elif button_text == "Spin":
            self.create_spin_menu()

    def create_shop_menu(self):
        shop_label = tk.Label(self, text="Shop", font=("Party LET", 40))
        shop_label.place(x=110, y=10)

        # Angebot "OG-Mod Menü für 10€"
        og_mod_label = tk.Label(self, text="OG-Mod Menü für 10€")
        og_mod_label.place(x=400, y=100)

        # Angebot "No Ads Pack für 10€ Monatlich"
        no_ads_label = tk.Label(self, text="No Ads Pack für 10€ Monatlich")
        no_ads_label.place(x=400, y=200)

        # Glücksrad
        self.create_wheel()

        # Button "Spin"
        spin_button = tk.Button(self, text="Spin", padx=10, pady=5, command=self.spin_wheel)
        spin_button.place(x=300, y=400)

        # Kostenfreie Benutzung und Kostenhinweis
        free_use_label = tk.Label(self, text="Eine kostenfreie Benutzung jeden Tag", font=("Party LET", 20))
        free_use_label.place(x=600, y=600)
        cost_label = tk.Label(self, text="sonst 10€", font=("Party LET", 20))
        cost_label.place(x=630, y=630)


        og_mod_button = tk.Button(self, text="Nehmen für 10€", padx=10, pady=5, command=self.confirm_og_mod)
        og_mod_button.place(x=300, y=200)

    def confirm_og_mod(self):
        self.clear_widgets()

        confirm_label = tk.Label(self, text="Bist du dir sicher?", font=("Helvetica", 16))
        confirm_label.place(x=200, y=100)

        yes_button = tk.Button(self, text="Ja", padx=10, pady=5, command=self.take_og_mod)
        yes_button.place(x=300, y=150)

        no_button = tk.Button(self, text="Nein", padx=10, pady=5, command=self.create_shop_menu)
        no_button.place(x=400, y=150)

    def take_og_mod(self):
        # Hier fügen Sie Ihre Logik zum Kauf des OG-Mod Menüs hinzu
        og_mod_frame = tk.Frame(self, bg="lightgray", width=400, height=200)
        og_mod_frame.place(x=300, y=100)

        og_mod_label = tk.Label(og_mod_frame, text="OG-Mod Menü für 10€")
        og_mod_label.pack()

        take_button = tk.Button(og_mod_frame, text="Nehmen für 10€", command=self.confirm_purchase)
        take_button.pack()

        print("OG-Mod Menü gekauft.")

    def confirm_og_mod(self):
        self.clear_widgets()

        confirm_label = tk.Label(self, text="Bist du dir sicher?", font=("Helvetica", 16))
        confirm_label.place(x=200, y=100)

        yes_button = tk.Button(self, text="Ja", padx=10, pady=5, command=self.take_og_mod)
        yes_button.place(x=300, y=150)

        no_button = tk.Button(self, text="Nein", padx=10, pady=5, command=self.create_shop_menu)
        no_button.place(x=400, y=150)


    def create_spin_menu(self):
        spin_label = tk.Label(self, text="Spin Menu", font=("Helvetica", 20))
        spin_label.place(x=20, y=50)



    def create_wheel(self):
        # Glücksrad mit 12 Segmenten
        wheel_canvas = tk.Canvas(self, width=500, height=500, bg="blue")
        wheel_canvas.place(x=100, y=200)

        num_segments = 12
        angle = 360 / num_segments
        for i in range(num_segments):
            start_angle = i * angle
            end_angle = (i + 1) * angle
            wheel_canvas.create_arc(5, 5, 495, 495, start=start_angle, extent=angle, fill="yellow")

        # Kreis in der Mitte als Button
        spin_button = tk.Button(self, text="Spin", padx=10, pady=5, command=self.spin_wheel)
        spin_button.place(x=200, y=300)

    def spin_wheel(self):
        if not self.daily_spin_used:
            # Funktion zum Drehen des Rads
            # Hier fügen Sie Ihre Logik zum Drehen des Rads ein
            print("Rad wird gedreht.")
            self.daily_spin_used = True
        else:
            print("Du hast das Rad bereits heute gedreht.")

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
