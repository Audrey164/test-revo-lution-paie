import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import csv

class App:
    """Application principale de gestion des employés pour REVO-LUTION Paie."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("REVO-LUTION Paie | Système de Gestion")
        self.root.geometry("1000x650")
        self.root.configure(bg="#ffffff")

        # Configuration du style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="#333", rowheight=30)
        style.map("Treeview", background=[('selected', '#3498db')])
        style.configure("Treeview.Heading", background="#2c3e50", foreground="#ffffff", relief="flat")
        
        # Header
        header = tk.Frame(root, bg="#2c3e50", pady=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="GESTION DES EMPLOYÉS", font=('Segoe UI', 20, 'bold'), bg="#2c3e50", fg="#ffffff").pack()

        # Zone de recherche
        control_frame = tk.Frame(root, bg="#ffffff", pady=20, padx=20)
        control_frame.pack(fill=tk.X)
        
        tk.Label(control_frame, text="Recherche :", font=('Segoe UI', 10), bg="#ffffff").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(control_frame, textvariable=self.search_var, font=('Segoe UI', 11), width=40, relief="solid")
        self.search_entry.pack(side=tk.LEFT, padx=10)
        self.search_entry.bind("<KeyRelease>", self.filter_data)

        btn_search = tk.Button(control_frame, text="RECHERCHER", command=self.filter_data, 
                               bg="#3498db", fg="white", font=('Segoe UI', 9, 'bold'), relief="flat", padx=10)
        btn_search.pack(side=tk.LEFT)

        # Tableau
        self.tree = ttk.Treeview(root, columns=("id", "nom", "prenom", "poste", "dept", "salaire", "date"), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))
        
        columns = [("id", "ID"), ("nom", "NOM"), ("prenom", "PRÉNOM"), ("poste", "POSTE"), 
                   ("dept", "DÉPARTEMENT"), ("salaire", "SALAIRE"), ("date", "DATE EMB.")]
        for col, text in columns:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120, anchor="center")

        # Footer
        footer = tk.Frame(root, bg="#ffffff", pady=10)
        footer.pack(fill=tk.X)
        tk.Button(footer, text="Exporter vers CSV", command=self.export_csv, 
                  bg="#27ae60", fg="white", font=('Segoe UI', 10, 'bold'), 
                  relief="flat", cursor="hand2", padx=20).pack()

        self.load_data()

    def load_data(self, query=None):
        """Charge les données depuis SQLite avec sécurité (placeholders)."""
        for item in self.tree.get_children(): 
            self.tree.delete(item)
            
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        
        if not query:
            cursor.execute("SELECT id, nom, prenom, poste, departement, salaire_brut, date_embauche FROM employees")
        else:
            # CORRECTION : On passe le pattern via un tuple, pas de f-string dans l'execute
            search_pattern = f"%{query}%"
            cursor.execute("""SELECT id, nom, prenom, poste, departement, salaire_brut, date_embauche 
                              FROM employees WHERE 
                              nom LIKE ? OR prenom LIKE ? OR poste LIKE ? OR departement LIKE ?""", 
                           (search_pattern, search_pattern, search_pattern, search_pattern))
            
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def filter_data(self, event=None):
        """Déclenche le filtrage basé sur la saisie utilisateur."""
        query = self.search_var.get().strip()
        self.load_data(query)

    def export_csv(self):
        """Exporte les données actuelles vers un fichier CSV compatible Excel."""
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if not filepath: 
            return
            
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