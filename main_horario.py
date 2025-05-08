import tkinter as tk
import subprocess as sp
import horario

janela = tk.Tk()
janela.title("Main window")
janela.geometry("500x300")
janela.configure(bg="white")

def abrir_horario():
    horario.janela_horario()

def fechar_janela():
    janela.destroy()

texto = tk.Label(janela, text="Janela principal", font=("Arial",40))
texto.pack(pady=20)

verHorario = tk.Button(janela, text="Ver horário", font=("Arial",20), command=abrir_horario, relief="solid")
verHorario.pack(pady=20)

fechar = tk.Button(janela, text="Fechar", font=("Arial",15), command=fechar_janela, relief="solid")
fechar.pack(pady=20)






janela.mainloop()