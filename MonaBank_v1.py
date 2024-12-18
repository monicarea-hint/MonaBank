import tkinter as tk
from tkinter import messagebox
import itertools

class MonaBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MonaBank")
        self.root.configure(bg="white")

        # Configurar ventana para ocupar gran parte de la pantalla
        self.root.geometry("800x600")

        # Variables
        self.saldo_actual = 0.0

        # Letrero animado
        self.colors = itertools.cycle(["orange", "gray", "white"])
        self.letrero_frame = tk.Frame(root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        # Mostrar saldo actual
        self.saldo_label = tk.Label(root, text=f"Saldo Actual: $0.00", font=("Arial", 14), bg="white", fg="gray")
        self.saldo_label.pack(pady=10)

        # Entrada de monto
        self.monto_label = tk.Label(root, text="Ingrese el monto:", font=("Arial", 12), bg="white", fg="gray")
        self.monto_label.pack()
        self.monto_entry = tk.Entry(root, font=("Arial", 12))
        self.monto_entry.pack(pady=5)

        # Botones
        self.consultar_button = tk.Button(root, text="Consultar Saldo", font=("Arial", 12), bg="orange", fg="white", command=self.consultar_saldo)
        self.consultar_button.pack(pady=5)

        self.depositar_button = tk.Button(root, text="Depositar Dinero", font=("Arial", 12), bg="orange", fg="white", command=self.depositar)
        self.depositar_button.pack(pady=5)

        self.retirar_button = tk.Button(root, text="Retirar Dinero", font=("Arial", 12), bg="orange", fg="white", command=self.retirar)
        self.retirar_button.pack(pady=5)

    def animate_letrero(self):
        next_color = next(self.colors)
        self.letrero.config(fg=next_color)
        self.root.after(500, self.animate_letrero)

    def consultar_saldo(self):
        self.saldo_label.config(text=f"Saldo Actual: ${self.saldo_actual:.2f}")

    def depositar(self):
        try:
            monto = float(self.monto_entry.get())
            if monto > 0:
                self.saldo_actual += monto
                self.consultar_saldo()
                messagebox.showinfo("Depósito Exitoso", f"Se han depositado ${monto:.2f}")
            else:
                messagebox.showerror("Error", "El monto debe ser positivo.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido.")

    def retirar(self):
        try:
            monto = float(self.monto_entry.get())
            if monto > 0:
                if monto <= self.saldo_actual:
                    self.saldo_actual -= monto
                    self.consultar_saldo()
                    messagebox.showinfo("Retiro Exitoso", f"Se han retirado ${monto:.2f}")
                else:
                    messagebox.showerror("Error", "Saldo insuficiente.")
            else:
                messagebox.showerror("Error", "El monto debe ser positivo.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido.")

# Crear ventana principal
root = tk.Tk()
app = MonaBankApp(root)
root.mainloop()
