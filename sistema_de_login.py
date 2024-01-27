import customtkinter
import sqlite3

def fazer_login():
    
    user = nome.get()
    password = senha.get()

    conexao = sqlite3.connect("Banco_de_dados_usuarios.bd")

    c = conexao.cursor()

    c.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (user, password))
    resultado = c.fetchone()

    conexao.close()

    if resultado:
        print("Login realizado com sucesso!")
    else:
        print("Nome ou senha inválidos!")
    
    nome.delete(0, "end")
    senha.delete(0, "end")



janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Login")

#label
texto = customtkinter.CTkLabel(janela, text="Login")
texto.pack(padx=10, pady=10)

#entrys
nome = customtkinter.CTkEntry(janela, placeholder_text="Nome")
nome.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

#button
botao_login = customtkinter.CTkButton(janela, text="Entrar", command=fazer_login)
botao_login.pack(padx=10, pady=10)


janela.mainloop()
