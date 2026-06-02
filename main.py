import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import csv

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("REVO-LUTION Paie | Système de Gestion")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f4f7f6") # Couleur de fond légèrement grisâtre pour le contraste

        # Configuration du style moderne
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="#333", rowheight=35)
        style.configure("Treeview.Heading", background="#2c3e50", foreground="#ffffff", relief="flat", font=('Segoe UI', 10, 'bold'))
        style.map("Treeview", background=[('selected', '#3498db')])
        
        # Header
        header = tk.Frame(root, bg="#2c3e50", pady=25)
        header.pack(fill=tk.X)
        tk.Label(header, text="REVO-LUTION PAIE | GESTION DES EMPLOYÉS", font=('Segoe UI', 18, 'bold'), bg="#2c3e50", fg="#ffffff").pack()

        # Zone de recherche améliorée
        control_frame = tk.Frame(root, bg="#f4f7f6", pady=20, padx=20)
        control_frame.pack(fill=tk.X)
        
        tk.Label(control_frame, text="Recherche rapide :", font=('Segoe UI', 10), bg="#f4f7f6").pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(control_frame, textvariable=self.search_var, font=('Segoe UI', 11), width=40, relief="flat", highlightthickness=1, highlightbackground="#bdc3c7")
        self.search_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        self.search_entry.bind("<KeyRelease>", self.filter_data)

        # Bouton Rechercher ajouté
        btn_search = tk.Button(control_frame, text="Rechercher", command=self.filter_data, 
                               bg="#3498db", fg="white", font=('Segoe UI', 9, 'bold'), relief="flat", padx=15, pady=3, cursor="hand2")
        btn_search.pack(side=tk.LEFT, padx=10)

        # Tableau
        table_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(table_frame, columns=("id", "nom", "prenom", "poste", "dept", "salaire", "date"), show='headings')
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = [("id", "ID"), ("nom", "NOM"), ("prenom", "PRÉNOM"), ("poste", "POSTE"), 
                   ("dept", "DÉPARTEMENT"), ("salaire", "SALAIRE"), ("date", "DATE EMB.")]
        for col, text in columns:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120, anchor="center")

        # Footer
        footer = tk.Frame(root, bg="#f4f7f6", pady=20)
        footer.pack(fill=tk.X)
        tk.Button(footer, text="Exporter les données vers CSV", command=self.export_csv, 
                  bg="#27ae60", fg="white", font=('Segoe UI', 11, 'bold'), 
                  relief="flat", cursor="hand2", padx=30, pady=10).pack()

        self.load_data()

    def load_data(self, query=None):
        for item in self.tree.get_children(): self.tree.delete(item)
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        if not query:
            cursor.execute("SELECT id, nom, prenom, poste, departement, salaire_brut, date_embauche FROM employees")
        else:
            search_pattern = f"%{query}%"
            cursor.execute("""SELECT id, nom, prenom, poste, departement, salaire_brut, date_embauche 
                              FROM employees WHERE nom LIKE ? OR prenom LIKE ? OR poste LIKE ? OR departement LIKE ?""", 
                           (search_pattern, search_pattern, search_pattern, search_pattern))
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def filter_data(self, event=None):
        self.load_data(self.search_var.get().strip())

    def export_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if not filepath: return
        rows = [self.tree.item(item)["values"] for item in self.tree.get_children()]
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["ID", "NOM", "PRENOM", "POSTE", "DEPARTEMENT", "SALAIRE", "DATE EMB"])
            writer.writerows(rows)
        messagebox.showinfo("Succès", "Données exportées avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
