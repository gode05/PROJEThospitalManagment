import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, master):
        self.master = master

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
