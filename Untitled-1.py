import tkinter as tk
from tkinter import ttk
import mysql.connector

class HospitalManager:
    def __init__(self, window):
        self.window = window
        self.window.title("Hospital Manager")
        self.window.geometry("500x500")
        self.window.configure(background="white")

        self.name = tk.StringVar()
        self.room_number = tk.StringVar()
        self.age = tk.StringVar()
        self.sex = tk.StringVar()
        self.doctor = tk.StringVar()
        self.appointment_date = tk.StringVar()

        self.name_label = tk.Label(self.window, text="Name", bg="white")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window, textvariable=self.name)
        self.name_entry.grid(row=0, column=1)

        self.room_number_label = tk.Label(self.window, text="Room Number", bg="white")
        self.room_number_label.grid(row=1, column=0)
        self.room_number_entry = tk.Entry(self.window, textvariable=self.room_number)
        self.room_number_entry.grid(row=1, column=1)

        self.age_label = tk.Label(self.window, text="Age", bg="white")
        self.age_label.grid(row=2, column=0)
        self.age_entry = tk.Entry(self.window, textvariable=self.age)
        self.age_entry.grid(row=2, column=1)

        self.sex_label = tk.Label(self.window, text="Sex", bg="white")
        self.sex_label.grid(row=3, column=0)
        self.sex_entry = tk.Entry(self.window, textvariable=self.sex)
        self.sex_entry.grid(row=3, column=1)

        self.doctor_label = tk.Label(self.window, text="Doctor", bg="white")
        self.doctor_label.grid(row=4, column=0)
        self.doctor_entry = tk.Entry(self.window, textvariable=self.doctor)
        self.doctor_entry.grid(row=4, column=1)

        self.appointment_date_label = tk.Label(self.window, text="Appointment Date", bg="white")
        self.appointment_date_label.grid(row=5, column=0)
        self.appointment_date_entry = tk.Entry(self.window, textvariable=self.appointment_date)
        self.appointment_date_entry.grid(row=5, column=1)

        self.add_button = tk.Button(self.window, text="Add", command=self.add_patient)
        self.add_button.grid(row=6, column=0)
        self.delete_button = tk.Button(self.window, text="Delete", command=self.delete_patient)
        self.delete_button.grid(row=6, column=1)
        self.modify_button = tk.Button(self.window, text="Modify", command=self.modify_patient)
        self.modify_button.grid(row=6, column=2)
        self.view_button = tk.Button(self.window, text="View", command=self.view_patients)
        self.view_button.grid(row=6, column=3)

        self.tree = ttk.Treeview(self.window, column=("column1", "column2", "column3", "column4", "column5", "column6"))
        self.tree.heading("#0", text="Name")
        self.tree.heading("#1", text="Room Number")
        self.tree.heading("#2", text="Age")
        self.tree.heading("#3", text="Sex")
        self.tree.heading("#4", text="Doctor")
        self.tree.heading("#5", text="Appointment Date")
        self.tree.grid(row=7, column=0, columnspan=4)

        self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="hospitalmanager")
        self.cursor = self.connection.cursor()

    def add_patient(self):
        self.cursor.execute("INSERT INTO Patient VALUES(%s, %s, %s, %s, %s, %s)", (self.name.get(), self.room_number.get(), self.age.get(), self.sex.get(), self.doctor.get(), self.appointment_date.get()))
        self.connection.commit()
        self.name_entry.delete(0, tk.END)
        self.room_number_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.sex_entry.delete(0, tk.END)
        self.doctor_entry.delete(0, tk.END)
        self.appointment_date_entry.delete(0, tk.END)

    def delete_patient(self):
        self.cursor.execute("DELETE FROM Patient WHERE Nom = %s", (self.name.get(),))
        self.connection.commit()
        self.name_entry.delete(0, tk.END)
        

    def modify_patient(self):
        self.cursor.execute("UPDATE Patient SET Numerodechambre = %s, Age = %s, Sexe = %s, Médecin = %s, DatedeRdv = %s WHERE Nom = %s", (self.room_number.get(), self.age.get(), self.sex.get(), self.doctor.get(), self.appointment_date.get(), self.name.get()))
        self.connection.commit()
        self.name_entry.delete(0, tk.END)
        self.room_number_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.sex_entry.delete(0, tk.END)
        self.doctor_entry.delete(0, tk.END)
        self.appointment_date_entry.delete(0, tk.END)

    def view_patients(self):
        self.cursor.execute("SELECT * FROM Patient")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        else:
            self.tree.delete(*self.tree.get_children())
            self.tree.insert("", tk.END, text="No data found.")

window = tk.Tk()
HospitalManager(window)
window.mainloop()