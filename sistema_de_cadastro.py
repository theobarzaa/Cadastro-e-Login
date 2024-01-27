import customtkinter
import sqlite3

def cadastrar_clientes():
        conexao = sqlite3.connect("Banco_de_dados_usuarios.bd")
        c = conexao.cursor()

        c.execute("INSERT INTO usuarios VALUES(:nome, :senha)",
                  {
                      'nome': nome.get(),
                      'senha': senha.get()
                  }
                  )

        conexao.commit()
        
        # Limpar os campos após o cadastro
        nome.delete(0, "end")
        senha.delete(0, "end")


        conexao.close()

janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Cadastro")

# label
label_titulo = customtkinter.CTkLabel(janela, text="Cadastro")
label_titulo.pack(padx=10, pady=10)

# entrys
nome = customtkinter.CTkEntry(janela, placeholder_text="Nome")
nome.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

# buttons
botao_cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar_clientes)
botao_cadastrar.pack(padx=10, pady=10)

janela.mainloop()