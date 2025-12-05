# Jogo de Adivinhação com Interface Gráfica
# O programa deve gerar um numero aleatorio entre 1 e 15, e pedir para o usuário adivinhar o numero gerado
# Se a tentativa do user nao for correta, o programa deve informar se ele tentou um valor baixo ou alto comparado ao gerado
# Se o user acertar: parabens, voce acertou!
# o programa deve permitir 3 tentativas por jogo

import random
import tkinter as tk
from tkinter import messagebox, ttk

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação do DK")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#2b2b2b')
        
        # Variáveis do jogo
        self.numeroSorteado = 0
        self.tentativas = 3
        self.acertou = False
        
        # Configurar estilo
        self.setup_ui()
        self.novo_jogo()
        
    def setup_ui(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="🎮 Jogo de Adivinhação do DK 🎮",
            font=("Arial", 20, "bold"),
            bg='#2b2b2b',
            fg='#ffffff'
        )
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = tk.Label(
            self.root,
            text="Tente adivinhar o número entre 1 e 15!",
            font=("Arial", 12),
            bg='#2b2b2b',
            fg='#cccccc'
        )
        subtitulo.pack(pady=5)
        
        # Frame para tentativas
        self.frame_tentativas = tk.Frame(self.root, bg='#2b2b2b')
        self.frame_tentativas.pack(pady=10)
        
        self.label_tentativas = tk.Label(
            self.frame_tentativas,
            text="Tentativas restantes: 3",
            font=("Arial", 14, "bold"),
            bg='#2b2b2b',
            fg='#4CAF50'
        )
        self.label_tentativas.pack()
        
        # Frame para entrada
        frame_entrada = tk.Frame(self.root, bg='#2b2b2b')
        frame_entrada.pack(pady=20)
        
        tk.Label(
            frame_entrada,
            text="Seu chute:",
            font=("Arial", 12),
            bg='#2b2b2b',
            fg='#ffffff'
        ).pack(side=tk.LEFT, padx=5)
        
        self.entrada_chute = tk.Entry(
            frame_entrada,
            font=("Arial", 14),
            width=10,
            justify='center'
        )
        self.entrada_chute.pack(side=tk.LEFT, padx=5)
        self.entrada_chute.bind('<Return>', lambda e: self.processar_chute())
        
        # Botão enviar
        self.botao_enviar = tk.Button(
            frame_entrada,
            text="Enviar",
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            activeforeground='white',
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=self.processar_chute,
            padx=20,
            pady=5
        )
        self.botao_enviar.pack(side=tk.LEFT, padx=10)
        
        # Área de mensagens
        self.texto_mensagem = tk.Text(
            self.root,
            font=("Arial", 11),
            bg='#1e1e1e',
            fg='#ffffff',
            height=12,
            width=50,
            wrap=tk.WORD,
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=10
        )
        self.texto_mensagem.pack(pady=20, padx=20)
        self.texto_mensagem.config(state=tk.DISABLED)
        
        # Frame para botões
        frame_botoes = tk.Frame(self.root, bg='#2b2b2b')
        frame_botoes.pack(pady=10)
        
        self.botao_novo_jogo = tk.Button(
            frame_botoes,
            text="🔄 Novo Jogo",
            font=("Arial", 11, "bold"),
            bg='#2196F3',
            fg='white',
            activebackground='#0b7dda',
            activeforeground='white',
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=self.novo_jogo,
            padx=15,
            pady=8
        )
        self.botao_novo_jogo.pack(side=tk.LEFT, padx=5)
        
        botao_sair = tk.Button(
            frame_botoes,
            text="❌ Sair",
            font=("Arial", 11, "bold"),
            bg='#f44336',
            fg='white',
            activebackground='#da190b',
            activeforeground='white',
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=self.root.quit,
            padx=15,
            pady=8
        )
        botao_sair.pack(side=tk.LEFT, padx=5)
        
    def adicionar_mensagem(self, mensagem, cor='#ffffff'):
        self.texto_mensagem.config(state=tk.NORMAL)
        self.texto_mensagem.insert(tk.END, mensagem + "\n")
        self.texto_mensagem.see(tk.END)
        self.texto_mensagem.config(state=tk.DISABLED)
        
    def novo_jogo(self):
        self.numeroSorteado = random.randint(1, 15)
        self.tentativas = 3
        self.acertou = False
        
        self.label_tentativas.config(text="Tentativas restantes: 3", fg='#4CAF50')
        self.texto_mensagem.config(state=tk.NORMAL)
        self.texto_mensagem.delete(1.0, tk.END)
        self.texto_mensagem.config(state=tk.DISABLED)
        
        self.entrada_chute.delete(0, tk.END)
        self.entrada_chute.focus()
        self.botao_enviar.config(state=tk.NORMAL)
        
        self.adicionar_mensagem("=" * 40, '#4CAF50')
        self.adicionar_mensagem("🎲 Novo jogo iniciado!", '#4CAF50')
        self.adicionar_mensagem("Tente adivinhar o número entre 1 e 15!", '#ffffff')
        self.adicionar_mensagem("=" * 40, '#4CAF50')
        
    def processar_chute(self):
        if self.acertou or self.tentativas <= 0:
            return
            
        try:
            chute = int(self.entrada_chute.get())
            
            if chute < 1 or chute > 15:
                messagebox.showwarning(
                    "Entrada Inválida",
                    "Por favor, digite um número entre 1 e 15!"
                )
                self.entrada_chute.delete(0, tk.END)
                return
                
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Por favor, digite apenas números!"
            )
            self.entrada_chute.delete(0, tk.END)
            return
        
        self.tentativas -= 1
        tentativas_restantes = self.tentativas
        
        self.entrada_chute.delete(0, tk.END)
        
        if chute == self.numeroSorteado:
            self.acertou = True
            self.botao_enviar.config(state=tk.DISABLED)
            self.label_tentativas.config(text="🎉 VOCÊ ACERTOU! 🎉", fg='#4CAF50')
            
            mensagem_vitoria = f"""
╔══════════════════════════════════════╗
║   🎉 PARABÉNS! VOCÊ ACERTOU! 🎉     ║
║                                      ║
║   Número sorteado: {self.numeroSorteado}
║   Tentativas restantes: {tentativas_restantes}
║   Ganhou 500 dkPoints!               ║
╚══════════════════════════════════════╝
"""
            self.adicionar_mensagem(mensagem_vitoria, '#4CAF50')
            messagebox.showinfo("Vitória!", f"Parabéns! Você acertou!\nO número era {self.numeroSorteado}\nGanhou 500 dkPoints!")
            
        elif chute > self.numeroSorteado:
            self.label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}", fg='#FF9800' if tentativas_restantes > 0 else '#f44336')
            self.adicionar_mensagem(f"❌ Chute: {chute} - O número é MENOR que {chute}", '#FF9800')
            self.adicionar_mensagem(f"   Restam {tentativas_restantes} tentativa(s)\n", '#cccccc')
            
        else:
            self.label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}", fg='#FF9800' if tentativas_restantes > 0 else '#f44336')
            self.adicionar_mensagem(f"❌ Chute: {chute} - O número é MAIOR que {chute}", '#FF9800')
            self.adicionar_mensagem(f"   Restam {tentativas_restantes} tentativa(s)\n", '#cccccc')
        
        if self.tentativas <= 0 and not self.acertou:
            self.botao_enviar.config(state=tk.DISABLED)
            self.label_tentativas.config(text="GAME OVER", fg='#f44336')
            
            mensagem_derrota = f"""
╔══════════════════════════════════════╗
║         😢 GAME OVER! 😢            ║
║                                      ║
║   O número secreto era: {self.numeroSorteado}
║   Tente novamente!                   ║
╚══════════════════════════════════════╝
"""
            self.adicionar_mensagem(mensagem_derrota, '#f44336')
            messagebox.showwarning("Game Over", f"Suas tentativas acabaram!\nO número secreto era: {self.numeroSorteado}\nClique em 'Novo Jogo' para tentar novamente!")
        
        self.entrada_chute.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()

