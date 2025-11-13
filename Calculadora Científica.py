import tkinter as tk
from tkinter import ttk, messagebox
import math


class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#2b2b2b')

        # Título
        titulo = tk.Label(root, text="Calculadora Científica",
                          font=('Arial', 20, 'bold'),
                          bg='#2b2b2b', fg='#ffffff')
        titulo.pack(pady=20)

        # Frame principal com notebook (abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Criar abas
        self.criar_aba_basica()
        self.criar_aba_trigonometrica()
        self.criar_aba_calculo()
        self.criar_aba_equacoes()

    def criar_aba_basica(self):
        """Aba com operações básicas"""
        frame = tk.Frame(self.notebook, bg='#3c3c3c')
        self.notebook.add(frame, text='Básica')

        # Frame para entradas
        entrada_frame = tk.Frame(frame, bg='#3c3c3c')
        entrada_frame.pack(pady=20)

        tk.Label(entrada_frame, text="Número 1:", bg='#3c3c3c',
                 fg='white', font=('Arial', 11)).grid(row=0, column=0, padx=5, pady=5)
        self.num1_basica = tk.Entry(entrada_frame, width=20, font=('Arial', 12))
        self.num1_basica.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(entrada_frame, text="Número 2:", bg='#3c3c3c',
                 fg='white', font=('Arial', 11)).grid(row=1, column=0, padx=5, pady=5)
        self.num2_basica = tk.Entry(entrada_frame, width=20, font=('Arial', 12))
        self.num2_basica.grid(row=1, column=1, padx=5, pady=5)

        # Botões de operações
        botoes_frame = tk.Frame(frame, bg='#3c3c3c')
        botoes_frame.pack(pady=20)

        operacoes = [
            ("Adição (+)", lambda: self.operacao_basica('add')),
            ("Subtração (-)", lambda: self.operacao_basica('subtract')),
            ("Multiplicação (×)", lambda: self.operacao_basica('multiply')),
            ("Divisão (÷)", lambda: self.operacao_basica('divide')),
            ("Potência (^)", lambda: self.operacao_basica('power')),
            ("Raiz Quadrada", self.raiz_quadrada),
            ("Logaritmo (base 10)", self.logaritmo)
        ]

        for i, (texto, comando) in enumerate(operacoes):
            btn = tk.Button(botoes_frame, text=texto, command=comando,
                            width=20, height=2, font=('Arial', 10, 'bold'),
                            bg='#4CAF50', fg='white', cursor='hand2')
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        # Resultado
        self.resultado_basica = tk.Text(frame, height=4, width=60,
                                        font=('Arial', 11), bg='#1e1e1e',
                                        fg='#00ff00', state='disabled')
        self.resultado_basica.pack(pady=20, padx=20)

    def criar_aba_trigonometrica(self):
        """Aba com funções trigonométricas"""
        frame = tk.Frame(self.notebook, bg='#3c3c3c')
        self.notebook.add(frame, text='Trigonometria')

        entrada_frame = tk.Frame(frame, bg='#3c3c3c')
        entrada_frame.pack(pady=30)

        tk.Label(entrada_frame, text="Ângulo (graus):", bg='#3c3c3c',
                 fg='white', font=('Arial', 11)).grid(row=0, column=0, padx=5, pady=5)
        self.angulo_entry = tk.Entry(entrada_frame, width=20, font=('Arial', 12))
        self.angulo_entry.grid(row=0, column=1, padx=5, pady=5)

        botoes_frame = tk.Frame(frame, bg='#3c3c3c')
        botoes_frame.pack(pady=30)

        funcoes = [
            ("Seno", lambda: self.funcao_trig('sin')),
            ("Cosseno", lambda: self.funcao_trig('cos')),
            ("Tangente", lambda: self.funcao_trig('tan'))
        ]

        for i, (texto, comando) in enumerate(funcoes):
            btn = tk.Button(botoes_frame, text=texto, command=comando,
                            width=15, height=2, font=('Arial', 11, 'bold'),
                            bg='#2196F3', fg='white', cursor='hand2')
            btn.grid(row=0, column=i, padx=15, pady=10)

        self.resultado_trig = tk.Text(frame, height=4, width=60,
                                      font=('Arial', 11), bg='#1e1e1e',
                                      fg='#00ff00', state='disabled')
        self.resultado_trig.pack(pady=20, padx=20)

    def criar_aba_calculo(self):
        """Aba com derivadas e integrais"""
        frame = tk.Frame(self.notebook, bg='#3c3c3c')
        self.notebook.add(frame, text='Cálculo')

        info_label = tk.Label(frame, text="Polinômio: a₀ + a₁x + a₂x² + ... + aₙxⁿ",
                              bg='#3c3c3c', fg='#ffeb3b', font=('Arial', 10, 'italic'))
        info_label.pack(pady=10)

        # Grau do polinômio
        grau_frame = tk.Frame(frame, bg='#3c3c3c')
        grau_frame.pack(pady=10)

        tk.Label(grau_frame, text="Grau do polinômio:", bg='#3c3c3c',
                 fg='white', font=('Arial', 11)).grid(row=0, column=0, padx=5)
        self.grau_entry = tk.Entry(grau_frame, width=10, font=('Arial', 12))
        self.grau_entry.grid(row=0, column=1, padx=5)

        btn_gerar = tk.Button(grau_frame, text="Gerar Coeficientes",
                              command=self.gerar_coeficientes,
                              bg='#FF9800', fg='white', font=('Arial', 10, 'bold'))
        btn_gerar.grid(row=0, column=2, padx=10)

        # Frame para coeficientes
        self.coef_frame = tk.Frame(frame, bg='#3c3c3c')
        self.coef_frame.pack(pady=10)

        # Frame para parâmetros
        self.param_frame = tk.Frame(frame, bg='#3c3c3c')
        self.param_frame.pack(pady=10)

        # Botões de ação
        botoes_frame = tk.Frame(frame, bg='#3c3c3c')
        botoes_frame.pack(pady=10)

        btn_deriv = tk.Button(botoes_frame, text="Calcular Derivada",
                              command=self.calcular_derivada,
                              width=20, height=2, bg='#9C27B0', fg='white',
                              font=('Arial', 10, 'bold'))
        btn_deriv.grid(row=0, column=0, padx=10)

        btn_integ = tk.Button(botoes_frame, text="Calcular Integral",
                              command=self.calcular_integral,
                              width=20, height=2, bg='#9C27B0', fg='white',
                              font=('Arial', 10, 'bold'))
        btn_integ.grid(row=0, column=1, padx=10)

        self.resultado_calculo = tk.Text(frame, height=4, width=60,
                                         font=('Arial', 11), bg='#1e1e1e',
                                         fg='#00ff00', state='disabled')
        self.resultado_calculo.pack(pady=10, padx=20)

    def criar_aba_equacoes(self):
        """Aba com equações do 1º e 2º grau"""
        frame = tk.Frame(self.notebook, bg='#3c3c3c')
        self.notebook.add(frame, text='Equações')

        # Equação do 1º grau
        frame1 = tk.LabelFrame(frame, text="Equação do 1º Grau (ax + b = 0)",
                               bg='#3c3c3c', fg='white', font=('Arial', 11, 'bold'))
        frame1.pack(pady=20, padx=20, fill='x')

        entrada1 = tk.Frame(frame1, bg='#3c3c3c')
        entrada1.pack(pady=10)

        tk.Label(entrada1, text="a:", bg='#3c3c3c', fg='white',
                 font=('Arial', 11)).grid(row=0, column=0, padx=5)
        self.a1_entry = tk.Entry(entrada1, width=15, font=('Arial', 11))
        self.a1_entry.grid(row=0, column=1, padx=5)

        tk.Label(entrada1, text="b:", bg='#3c3c3c', fg='white',
                 font=('Arial', 11)).grid(row=0, column=2, padx=5)
        self.b1_entry = tk.Entry(entrada1, width=15, font=('Arial', 11))
        self.b1_entry.grid(row=0, column=3, padx=5)

        btn1 = tk.Button(frame1, text="Resolver", command=self.resolver_linear,
                         bg='#FF5722', fg='white', font=('Arial', 10, 'bold'))
        btn1.pack(pady=10)

        # Equação do 2º grau
        frame2 = tk.LabelFrame(frame, text="Equação do 2º Grau (ax² + bx + c = 0)",
                               bg='#3c3c3c', fg='white', font=('Arial', 11, 'bold'))
        frame2.pack(pady=20, padx=20, fill='x')

        entrada2 = tk.Frame(frame2, bg='#3c3c3c')
        entrada2.pack(pady=10)

        tk.Label(entrada2, text="a:", bg='#3c3c3c', fg='white',
                 font=('Arial', 11)).grid(row=0, column=0, padx=5)
        self.a2_entry = tk.Entry(entrada2, width=10, font=('Arial', 11))
        self.a2_entry.grid(row=0, column=1, padx=5)

        tk.Label(entrada2, text="b:", bg='#3c3c3c', fg='white',
                 font=('Arial', 11)).grid(row=0, column=2, padx=5)
        self.b2_entry = tk.Entry(entrada2, width=10, font=('Arial', 11))
        self.b2_entry.grid(row=0, column=3, padx=5)

        tk.Label(entrada2, text="c:", bg='#3c3c3c', fg='white',
                 font=('Arial', 11)).grid(row=0, column=4, padx=5)
        self.c2_entry = tk.Entry(entrada2, width=10, font=('Arial', 11))
        self.c2_entry.grid(row=0, column=5, padx=5)

        btn2 = tk.Button(frame2, text="Resolver", command=self.resolver_quadratica,
                         bg='#FF5722', fg='white', font=('Arial', 10, 'bold'))
        btn2.pack(pady=10)

        self.resultado_eq = tk.Text(frame, height=5, width=60,
                                    font=('Arial', 11), bg='#1e1e1e',
                                    fg='#00ff00', state='disabled')
        self.resultado_eq.pack(pady=10, padx=20)

    # Métodos para operações
    def operacao_basica(self, op):
        try:
            x = float(self.num1_basica.get())
            y = float(self.num2_basica.get())

            if op == 'add':
                resultado = x + y
                operacao = f"{x} + {y}"
            elif op == 'subtract':
                resultado = x - y
                operacao = f"{x} - {y}"
            elif op == 'multiply':
                resultado = x * y
                operacao = f"{x} × {y}"
            elif op == 'divide':
                if y == 0:
                    self.mostrar_resultado(self.resultado_basica, "Erro: Divisão por zero!")
                    return
                resultado = x / y
                operacao = f"{x} ÷ {y}"
            elif op == 'power':
                resultado = x ** y
                operacao = f"{x}^{y}"

            self.mostrar_resultado(self.resultado_basica, f"{operacao} = {resultado}")
        except ValueError:
            self.mostrar_resultado(self.resultado_basica, "Erro: Digite números válidos!")

    def raiz_quadrada(self):
        try:
            x = float(self.num1_basica.get())
            if x < 0:
                self.mostrar_resultado(self.resultado_basica, "Erro: Raiz de número negativo!")
                return
            resultado = math.sqrt(x)
            self.mostrar_resultado(self.resultado_basica, f"√{x} = {resultado}")
        except ValueError:
            self.mostrar_resultado(self.resultado_basica, "Erro: Digite um número válido!")

    def logaritmo(self):
        try:
            x = float(self.num1_basica.get())
            if x <= 0:
                self.mostrar_resultado(self.resultado_basica, "Erro: Log de número não positivo!")
                return
            resultado = math.log10(x)
            self.mostrar_resultado(self.resultado_basica, f"log₁₀({x}) = {resultado}")
        except ValueError:
            self.mostrar_resultado(self.resultado_basica, "Erro: Digite um número válido!")

    def funcao_trig(self, func):
        try:
            angulo = float(self.angulo_entry.get())
            rad = math.radians(angulo)

            if func == 'sin':
                resultado = math.sin(rad)
                nome = "sen"
            elif func == 'cos':
                resultado = math.cos(rad)
                nome = "cos"
            elif func == 'tan':
                resultado = math.tan(rad)
                nome = "tan"

            self.mostrar_resultado(self.resultado_trig,
                                   f"{nome}({angulo}°) = {resultado:.6f}")
        except ValueError:
            self.mostrar_resultado(self.resultado_trig, "Erro: Digite um ângulo válido!")

    def gerar_coeficientes(self):
        try:
            grau = int(self.grau_entry.get())
            if grau < 0 or grau > 5:
                messagebox.showerror("Erro", "Grau deve estar entre 0 e 5!")
                return

            # Limpar frame de coeficientes
            for widget in self.coef_frame.winfo_children():
                widget.destroy()

            self.coef_entries = []
            for i in range(grau + 1):
                tk.Label(self.coef_frame, text=f"a{i} (x^{i}):",
                         bg='#3c3c3c', fg='white',
                         font=('Arial', 10)).grid(row=i // 3, column=(i % 3) * 2, padx=5, pady=5)
                entry = tk.Entry(self.coef_frame, width=10, font=('Arial', 10))
                entry.grid(row=i // 3, column=(i % 3) * 2 + 1, padx=5, pady=5)
                self.coef_entries.append(entry)

            # Gerar campos de parâmetros
            for widget in self.param_frame.winfo_children():
                widget.destroy()

            tk.Label(self.param_frame, text="Ponto x (derivada):",
                     bg='#3c3c3c', fg='white', font=('Arial', 10)).grid(row=0, column=0, padx=5)
            self.x_deriv = tk.Entry(self.param_frame, width=10, font=('Arial', 10))
            self.x_deriv.grid(row=0, column=1, padx=5)

            tk.Label(self.param_frame, text="Limite inferior:",
                     bg='#3c3c3c', fg='white', font=('Arial', 10)).grid(row=1, column=0, padx=5)
            self.a_integ = tk.Entry(self.param_frame, width=10, font=('Arial', 10))
            self.a_integ.grid(row=1, column=1, padx=5)

            tk.Label(self.param_frame, text="Limite superior:",
                     bg='#3c3c3c', fg='white', font=('Arial', 10)).grid(row=1, column=2, padx=5)
            self.b_integ = tk.Entry(self.param_frame, width=10, font=('Arial', 10))
            self.b_integ.grid(row=1, column=3, padx=5)

        except ValueError:
            messagebox.showerror("Erro", "Digite um grau válido!")

    def calcular_derivada(self):
        try:
            coefs = [float(entry.get()) for entry in self.coef_entries]
            x = float(self.x_deriv.get())

            n = len(coefs)
            deriv = sum(i * coefs[i] * (x ** (i - 1)) for i in range(1, n))

            self.mostrar_resultado(self.resultado_calculo,
                                   f"Derivada no ponto x = {x}: {deriv:.6f}")
        except (ValueError, AttributeError):
            self.mostrar_resultado(self.resultado_calculo,
                                   "Erro: Gere os coeficientes e preencha todos os campos!")

    def calcular_integral(self):
        try:
            coefs = [float(entry.get()) for entry in self.coef_entries]
            a = float(self.a_integ.get())
            b = float(self.b_integ.get())

            n = len(coefs)
            integ = sum((coefs[i] / (i + 1)) * (b ** (i + 1) - a ** (i + 1))
                        for i in range(n))

            self.mostrar_resultado(self.resultado_calculo,
                                   f"Integral de {a} a {b}: {integ:.6f}")
        except (ValueError, AttributeError):
            self.mostrar_resultado(self.resultado_calculo,
                                   "Erro: Gere os coeficientes e preencha todos os campos!")

    def resolver_linear(self):
        try:
            a = float(self.a1_entry.get())
            b = float(self.b1_entry.get())

            if a == 0:
                self.mostrar_resultado(self.resultado_eq,
                                       "Erro: Coeficiente 'a' não pode ser zero!")
                return

            x = -b / a
            self.mostrar_resultado(self.resultado_eq,
                                   f"Solução da equação {a}x + {b} = 0:\nx = {x:.6f}")
        except ValueError:
            self.mostrar_resultado(self.resultado_eq, "Erro: Digite valores válidos!")

    def resolver_quadratica(self):
        try:
            a = float(self.a2_entry.get())
            b = float(self.b2_entry.get())
            c = float(self.c2_entry.get())

            D = b ** 2 - 4 * a * c

            if D < 0:
                self.mostrar_resultado(self.resultado_eq, "Erro: Raízes complexas!")
                return

            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)

            self.mostrar_resultado(self.resultado_eq,
                                   f"Soluções de {a}x² + {b}x + {c} = 0:\n" +
                                   f"x₁ = {x1:.6f}\nx₂ = {x2:.6f}\n" +
                                   f"Delta (Δ) = {D:.6f}")
        except ValueError:
            self.mostrar_resultado(self.resultado_eq, "Erro: Digite valores válidos!")

    def mostrar_resultado(self, widget, texto):
        widget.config(state='normal')
        widget.delete(1.0, tk.END)
        widget.insert(1.0, texto)
        widget.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()