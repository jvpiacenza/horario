import tkinter as tk 
import time 

def janela_horario():
        
    janela = tk.Tk() 
    janela.title("Horário")
    janela.geometry("300x200")

    hora = tk.Label(janela, text= "Horario de Brasília: ", font=("Arial",20))
    hora.pack(pady=10) 

    def fechar_janela():
        janela.destroy() 

    def atualizar_relogio() :
        tempo_atual = time.strftime("%H:%M:%S") 
        relogio.config(text=tempo_atual)
        relogio.after(1000, atualizar_relogio)

    relogio = tk.Label(janela, font=("Arial", 48), bg="white") 
    relogio.pack() 

    btnFechar = tk.Button(janela, text="Fechar", font=("Arial",15), command=fechar_janela, relief="solid")
    btnFechar.pack(pady=20) 

    atualizar_relogio() 