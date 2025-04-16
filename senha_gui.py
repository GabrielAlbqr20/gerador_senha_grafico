import random
import string
import tkinter as tk
from tkinter import messagebox

# Função que gera a senha
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError("Tamanho inválido")

        # Conjunto de caracteres permitidos (sem vírgula)
        simbolos = string.punctuation.replace(",", "")
        caracteres = string.ascii_letters + string.digits + simbolos

        # Geração da senha
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        # Exibe a senha no campo de resultado
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido maior que 0.")

# Criação da janela
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("350x180")
janela.resizable(False, False)

# Layout
tk.Label(janela, text="digite o tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

entry_resultado = tk.Entry(janela, width=30)
entry_resultado.pack()

# Execução
janela.mainloop()
