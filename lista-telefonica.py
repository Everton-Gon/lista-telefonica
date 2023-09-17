

import tkinter as tk
import tkinter.messagebox as msgbox
import csv
from tkinter import filedialog


class ListaTelefonica:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista Telefônica")
        self.master.geometry("400x400")
        self.arquivo = None

        # Criando widgets
        self.label_nome = tk.Label(self.master, text="Nome:",fg='black',font=('Comic Sans MS', 10, 'bold'))
        self.entry_nome = tk.Entry(self.master)

        self.label_telefone = tk.Label(self.master, text="Telefone:",fg='black',font=('Comic Sans MS', 10, 'bold'))
        self.entry_telefone = tk.Entry(self.master)

        self.button_cadastrar = tk.Button(self.master, text="Cadastrar", bd=4 , bg='DarkGray',fg='black',font=('Comic Sans MS', 9, 'bold'),command=self.cadastrar_contato)
        self.button_listar = tk.Button(self.master, text="Listar", bd=4 , bg='DarkGray',fg='black',font=('Comic Sans MS', 9, 'bold'), command=self.listar_contatos)

        # Posicionando widgets
        self.label_nome.grid(row=0, column=1)
        self.entry_nome.grid(row=0, column=2)

        self.label_telefone.grid(row=1, column=1)
        self.entry_telefone.grid(row=1, column=2)

        self.button_cadastrar.grid(row=2, column=1)
        self.button_listar.grid(row=2, column=2)

    def cadastrar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        if nome == "" or telefone == "":
            msgbox.showerror("Erro", "Preencha todos os campos!")
        else:
            if not self.arquivo:
                self.arquivo = filedialog.asksaveasfile(defaultextension=".csv")
            with open(self.arquivo.name, "a", newline="") as arquivo_csv:
                escrever = csv.writer(arquivo_csv)
                escrever.writerow([nome, telefone])
            self.entry_nome.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            msgbox.showinfo("Sucesso", "Contato adicionado com sucesso!")

    def listar_contatos(self):
        if self.arquivo:
            with open(self.arquivo.name, "r") as arquivo_csv:
                ler = csv.reader(arquivo_csv)
                for row in ler:
                    print(row)
        else:
            msgbox.showerror("Erro", "Nenhum arquivo selecionado!")

root = tk.Tk()
root.iconbitmap('phonebook_40497.ico')
app = ListaTelefonica(root)
root.mainloop()
