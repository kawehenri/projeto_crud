from tkinter import *
from tkinter import ttk
import services

# get modo de leitura
def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome,email,senha)

        # Para limpar os campos
        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    def lista_usuario():
        usuarios = services.listar_usuario()

        # Criar uma janela para mostrar a lista
        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de usuarios')
        janela_listar.geometry('600x300')

        # Criar uma treeview (visualização) da lista de usuarios, show='healdings' = limpa cabeçalho
        tree = ttk.Treeview(janela_listar, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # Criar botão de voltar que ira fechar a lista de usuario
        voltar = Button(janela_listar, text='Voltar', width=10, command=janela_listar.destroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)

        tree.pack(fill=BOTH, expand=True)

        # Inserir dados de usuario na treeview
        for usuario in usuarios:
            # END vai inserir o item no final da tabela
            tree.insert('', END, values=usuario)


    # Criação de janela
    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de gerenciamento de usuario')

    # Criação do titulo da interface
    titulo = Label(janela, text = 'CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    # Nome
    nome = Label(janela, text='Nome: ')
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    # Email
    email = Label(janela, text='Email: ')
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    # Senha
    senha = Label(janela, text='Senha: ')
    senha.place(x=50, y=160)

    # Comando show para esconder senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=100, y=160)

    # Listar cadastro
    cadastrar = Button(janela, text='Cadastrar', width=10, command=on_enviar)
    cadastrar.place(x=100, y=200)

    listar = Button(janela, text='Listar usuarios', width=15, command=lista_usuario)
    listar.place(x=200, y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()
