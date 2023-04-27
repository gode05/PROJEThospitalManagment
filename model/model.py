class Application:
    def __init__(self, master):
        self.master = master
class Patient:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance


class RendezVous:
    def __init__(self, date, heure, patient):
        self.date = date
        self.heure = heure
        self.patient = patient


class DossierMedical:
    def __init__(self, patient, antecedents, traitements_en_cours):
        self.patient = patient
        self.antecedents = antecedents
        self.traitements_en_cours = traitements_en_cours


class Traitement:
    def __init__(self, patient, medicaments, posologie):
        self.patient = patient
        self.medicaments = medicaments
        self.posologie = posologie
