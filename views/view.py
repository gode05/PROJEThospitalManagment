import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, master):
        self.master = master

        # Création de la fenêtre principale
        self.master.title("Gestion Hospitalière")

        # Style des boutons
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), foreground='black', background='#00bfff', padding=10)

        # Création des widgets
        label_patient = tk.Label(self.master, text="Gestion des Patients", font=('Arial', 16, 'bold'))
        button_add_patient = ttk.Button(self.master, text="Ajouter Patient", command=self.new_patient_window)
        button_view_patient = ttk.Button(self.master, text="Voir Patients", command=self.new_patient_window)
        label_appointment = tk.Label(self.master, text="Gestion des Rendez-vous", font=('Arial', 16, 'bold'))
        button_add_appointment = ttk.Button(self.master, text="Ajouter Rendez-vous", command=self.new_appointment_window)
        button_view_appointment = ttk.Button(self.master, text="Voir Rendez-vous", command=self.new_appointment_window)
        label_medical_record = tk.Label(self.master, text="Gestion des Dossiers Médicaux", font=('Arial', 16, 'bold'))
        button_add_record = ttk.Button(self.master, text="Ajouter Dossier Médical", command=self.new_record_window)
        button_view_record = ttk.Button(self.master, text="Voir Dossiers Médicaux", command=self.new_record_window)
        button_view_record = ttk.Button(self.master, text="Voir Dossiers Médicaux", command=self.new_record_window)
        label_treatment = tk.Label(self.master, text="Gestion des Traitements", font=('Arial', 16, 'bold'))
        button_add_treatment = ttk.Button(self.master, text="Ajouter Traitement", command=self.new_treatment_window)

        # Configuration de la grille pour la responsivité
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)

        # Affichage des widgets sur la fenêtre principale
        label_patient.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        button_add_patient.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        button_view_patient.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        label_appointment.grid(row=0, column=1, padx=20, pady=20, sticky="w")
        button_add_appointment.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        button_view_appointment.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        label_medical_record.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        button_add_record.grid(row=1, column=2, padx=20, pady=10, sticky="w")
        button_view_record.grid(row=2, column=2, padx=20, pady=10, sticky="w")
        label_treatment.grid(row=0, column=3, padx=20, pady=20, sticky="w")
        button_add_treatment.grid(row=1, column=3, padx=20, pady=10, sticky="w")

    # Fonction pour créer une nouvelle fenêtre pour la gestion des patients
    def new_patient_window(self):
        # Création de la fenêtre
        patient_window = tk.Toplevel(self.master)
        patient_window.title("Gestion des Patients")

        # Ajout des widgets pour la gestion des patients
        label = tk.Label(patient_window, text="Cette fenêtre permettra la gestion des patients")
        label.pack(pady=20)

    # Fonction pour créer une nouvelle fenêtre pour la gestion des rendez-vous
    def new_appointment_window(self):
        # Création de la fenêtre
        appointment_window = tk.Toplevel(self.master)
        appointment_window.title("Gestion des Rendez-vous")

        # Ajout des widgets pour la gestion des rendez-vous
        label = tk.Label(appointment_window, text="Cette fenêtre permettra la gestion des rendez-vous")
        label.pack(pady=20)

    # Fonction pour créer une nouvelle fenêtre pour la gestion des dossiers médicaux
    def new_record_window(self):
        # Création de la fenêtre
        record_window = tk.Toplevel(self.master)
        record_window.title("Gestion des Dossiers Médicaux")

        # Ajout des widgets pour la gestion des dossiers médicaux r
        label = tk.Label(record_window, text="Cette fenêtre permettra la gestion des dossiers médicaux")
        label.pack(pady=20)

    # Fonction pour créer une nouvelle fenêtre pour la gestion des traitements
    def new_treatment_window(self):
        # Création de la fenêtre
        treatment_window = tk.Toplevel(self.master)
        treatment_window.title("Gestion des Traitements")

        # Ajout des widgets pour la gestion des traitements
        label = tk.Label(treatment_window, text="Cette fenêtre permettra la gestion des traitements")
        label.pack(pady=20)

root = tk.Tk()
app = Application(root)
root.mainloop()
