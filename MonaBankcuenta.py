import tkinter as tk
from tkinter import messagebox
import itertools

class MonaBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MonaBank")
        self.root.configure(bg="white")
        self.root.geometry("800x600")

        self.colors = itertools.cycle(["orange", "gray", "white"])

        # Variables
        self.saldo_actual = 0.0
        self.movimientos = []

        # Pantalla inicial
        self.init_login_screen()

    def init_login_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        # Usuario y contraseña
        self.user_label = tk.Label(self.root, text="Usuario:", font=("Arial", 12), bg="white", fg="gray")
        self.user_label.pack(pady=5)
        self.user_entry = tk.Entry(self.root, font=("Arial", 12))
        self.user_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Contraseña:", font=("Arial", 12), bg="white", fg="gray")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        # Botones
        self.login_button = tk.Button(self.root, text="Iniciar Sesión", font=("Arial", 12), bg="orange", fg="white", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Registrarse", font=("Arial", 12), bg="orange", fg="white", command=self.init_register_screen)
        self.register_button.pack(pady=5)

    def init_register_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        # Formulario de registro
        self.name_label = tk.Label(self.root, text="Nombre:", font=("Arial", 12), bg="white", fg="gray")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        self.surname_label = tk.Label(self.root, text="Apellido:", font=("Arial", 12), bg="white", fg="gray")
        self.surname_label.pack(pady=5)
        self.surname_entry = tk.Entry(self.root, font=("Arial", 12))
        self.surname_entry.pack(pady=5)

        self.cc_label = tk.Label(self.root, text="Cédula de Ciudadanía:", font=("Arial", 12), bg="white", fg="gray")
        self.cc_label.pack(pady=5)
        self.cc_entry = tk.Entry(self.root, font=("Arial", 12))
        self.cc_entry.pack(pady=5)

        self.account_label = tk.Label(self.root, text="Número de Cuenta:", font=("Arial", 12), bg="white", fg="gray")
        self.account_label.pack(pady=5)
        self.account_entry = tk.Entry(self.root, font=("Arial", 12))
        self.account_entry.pack(pady=5)

        self.type_label = tk.Label(self.root, text="Tipo de Cuenta:", font=("Arial", 12), bg="white", fg="gray")
        self.type_label.pack(pady=5)

        self.account_type = tk.StringVar(value="Ahorros")
        self.savings_radio = tk.Radiobutton(self.root, text="Ahorros", variable=self.account_type, value="Ahorros", font=("Arial", 12), bg="white")
        self.savings_radio.pack()
        self.current_radio = tk.Radiobutton(self.root, text="Corriente", variable=self.account_type, value="Corriente", font=("Arial", 12), bg="white")
        self.current_radio.pack()

        self.register_button = tk.Button(self.root, text="Registrar", font=("Arial", 12), bg="orange", fg="white", command=self.register)
        self.register_button.pack(pady=5)

    def init_main_screen(self, name, surname):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        # Bienvenida
        self.welcome_label = tk.Label(self.root, text=f"Bienvenido/a {name} {surname}", font=("Arial", 14), bg="white", fg="gray")
        self.welcome_label.pack(pady=10)

        # Opciones de gestión
        self.deposit_button = tk.Button(self.root, text="Depositar Fondos", font=("Arial", 12), bg="orange", fg="white", command=self.init_deposit_withdraw_screen)
        self.deposit_button.pack(pady=5)

        self.transactions_button = tk.Button(self.root, text="Transacciones", font=("Arial", 12), bg="orange", fg="white", command=self.init_transactions_screen)
        self.transactions_button.pack(pady=5)

        self.movements_button = tk.Button(self.root, text="Movimientos", font=("Arial", 12), bg="orange", fg="white", command=self.init_movements_screen)
        self.movements_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Finalizar", font=("Arial", 12), bg="orange", fg="white", command=self.init_exit_screen)
        self.exit_button.pack(pady=5)

    def init_deposit_withdraw_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        # Entrada de monto
        self.monto_label = tk.Label(self.root, text="Ingrese el monto:", font=("Arial", 12), bg="white", fg="gray")
        self.monto_label.pack(pady=5)
        self.monto_entry = tk.Entry(self.root, font=("Arial", 12))
        self.monto_entry.pack(pady=5)

        self.depositar_button = tk.Button(self.root, text="Depositar", font=("Arial", 12), bg="orange", fg="white", command=lambda: self.transaccion("depósito"))
        self.depositar_button.pack(pady=5)

        self.retirar_button = tk.Button(self.root, text="Retirar", font=("Arial", 12), bg="orange", fg="white", command=lambda: self.transaccion("retiro"))
        self.retirar_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Regresar", font=("Arial", 12), bg="orange", fg="white", command=self.init_main_screen)
        self.back_button.pack(pady=5)

    def init_transactions_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        self.transaction_label = tk.Label(self.root, text="Realice sus transacciones", font=("Arial", 14), bg="white", fg="gray")
        self.transaction_label.pack(pady=10)

        self.payment_button = tk.Button(self.root, text="Pago de Servicios", font=("Arial", 12), bg="orange", fg="white", command=self.init_exit_screen)
        self.payment_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Regresar", font=("Arial", 12), bg="orange", fg="white", command=self.init_main_screen)
        self.back_button.pack(pady=5)

    def init_movements_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        self.movements_label = tk.Label(self.root, text="Historial de Movimientos", font=("Arial", 14), bg="white", fg="gray")
        self.movements_label.pack(pady=10)

        for movimiento in self.movimientos:
            tk.Label(self.root, text=movimiento, font=("Arial", 12), bg="white", fg="gray").pack()

        self.back_button = tk.Button(self.root, text="Regresar", font=("Arial", 12), bg="orange", fg="white", command=self.init_main_screen)
        self.back_button.pack(pady=5)

    def init_exit_screen(self):
        self.clear_screen()

        # Letrero animado
        self.letrero_frame = tk.Frame(self.root, bg="black", height=100)
        self.letrero_frame.pack(fill="x", pady=10)
        self.letrero = tk.Label(self.letrero_frame, text="MonaBank", font=("Arial", 36, "bold"), fg="orange", bg="black")
        self.letrero.pack()
        self.animate_letrero()

        self.thank_you_label = tk.Label(self.root, text="Gracias por haber usado los servicios de su banco", font=("Arial", 14), bg="white", fg="gray")
        self.thank_you_label.pack(pady=20)

    def transaccion(self, tipo):
        try:
            monto = float(self.monto_entry.get())
            if tipo == "depósito":
                self.saldo_actual += monto
                self.movimientos.append(f"Depósito: ${monto:.2f}")
            elif tipo == "retiro":
                if monto <= self.saldo_actual:
                    self.saldo_actual -= monto
                    self.movimientos.append(f"Retiro: ${monto:.2f}")
                else:
                    messagebox.showerror("Error", "Saldo insuficiente.")
                    return
            messagebox.showinfo("Éxito", f"Transacción de {tipo} realizada por ${monto:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido.")

    def login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        if user and password:
            self.init_main_screen(user, "Usuario")
        else:
            messagebox.showerror("Error", "Ingrese credenciales válidas.")

    def register(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        if name and surname:
            messagebox.showinfo("Registro Exitoso", f"Usuario {name} {surname} registrado.")
            self.init_login_screen()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def animate_letrero(self):
        next_color = next(self.colors)
        self.letrero.config(fg=next_color)
        self.root.after(500, self.animate_letrero)

# Crear ventana principal
root = tk.Tk()
app = MonaBankApp(root)
root.mainloop()
