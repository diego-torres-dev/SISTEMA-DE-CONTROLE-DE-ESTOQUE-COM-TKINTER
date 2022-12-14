# Importa todos os objetos do tkinter
from tkinter import *

# Importa o messagebox do tkinter
import tkinter.messagebox

# Importa o pyodbc
import pyodbc

# Dados para conexão
driver = "{SQL Server}"
server = "DESKTOP-UP32DT2"
db = "Estoque"

# Dados da conexão
dados_conexao = f"Driver={driver};Server={server};Database={db}"

# Conexão
conexao = pyodbc.connect(dados_conexao)

# Criação de um cursor para executar instruções SQL
cursor = conexao.cursor()


# Adicionar insumo (CREATE)
def adicionar_insumo():
    # Obter informações do insumo
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    qtde = entry4.get()

    # Comando para adicionar um insumo no banco de dados
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde)
        VALUES
            ('{nome_insumo}', '{data_validade}', '{lote}', '{qtde}')"""

    # Executa o comando
    cursor.execute(comando)

    # Faz o commit do comando para salvar a alteração no banco de dados
    cursor.commit()

    # Exibe uma mensagem para alertar o usuário de que um novo registro foi criado
    tkinter.messagebox.showinfo(
        title="Aviso de Insumo Adicionado",
        message="Insumo adicionado com sucesso!")

    # Limpa todos os campos preenchidos
    entry1.delete(first=0, last=END)
    entry2.delete(first=0, last=END)
    entry3.delete(first=0, last=END)
    entry4.delete(first=0, last=END)


# Procurar insumo (READ)
def procurar_insumo():
    # Obter nome do insumo
    nome_insumo = entry1.get()

    # Comando para procurar o insumo no banco de dados
    comando = f"SELECT * FROM Insumos WHERE nome_insumo = '{nome_insumo}'"

    # Faz o cursor executar o comando
    cursor.execute(comando)

    # Percorre a lista de tuplas armazenada no cursor
    for linha in cursor.fetchall():
        # Mensagem a ser exibida na caixa de resultados (entry0)
        mensagem = f"Item: {linha.nome_insumo}\nData de validade: {linha.data_validade}\n" \
                   f"Lote: {linha.lote}\nQuantidade: {linha.qtde}"

        # Limpa o campo de resultados
        entry0.delete("1.0", END)

        # Coloca a mensagem na caixa de resultados
        entry0.insert("1.0", mensagem)





# Registrar uso de insumo (UPDATE)
def registrar_uso_insumo():
    # Obter nome do insumo
    nome_insumo = entry1.get()

    # Obter quantidade
    qtde = entry4.get()

    # Comando para atualizar o banco de dados
    comando = f"""UPDATE Insumos
        SET qtde = qtde - {qtde}
        WHERE nome_insumo = '{nome_insumo}'"""

    # Faz o cursor executar o comando
    cursor.execute(comando)

    # Faz o commit do comando
    cursor.commit()

    # Exibe uma mensagem para o usuário
    tkinter.messagebox.showinfo(
        title="Aviso de Uso de Insumo",
        message=f"{qtde} unidades de {nome_insumo} foram usadas.")

    # Limpa os campos preenchidos
    entry1.delete(first=0, last=END)
    entry4.delete(first=0, last=END)

# Deletar insumo (DELETE)
def deletar_insumo():
    # Obter nome do insumo
    nome_insumo = entry1.get()

    # Comando para deletar insumo do banco de dados
    comando = f"DELETE FROM Insumos WHERE nome_insumo = '{nome_insumo}'"

    # Faz o cursor executar o comando
    cursor.execute(comando)

    # Faz o commit do comando
    cursor.commit()

    # Exibe uma mensagem para o usuário de que um insumo foi removido
    tkinter.messagebox.showinfo(
        title="Aviso de insumo removido",
        message=f"{nome_insumo} foi removido com sucesso!")

    # Limpa o campo preenchido
    entry1.delete(first=0, last=END)


window = Tk()

window.title("Sistema de Controle de Estoque")

window.geometry("711x646")
window.configure(bg="#ffffff")

canvas = Canvas(
    window,
    bg="#ffffff",
    height=646,
    width=711,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=procurar_insumo,
    relief="flat")

b0.place(
    x=479, y=195,
    width=178,
    height=38)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=deletar_insumo,
    relief="flat")

b1.place(
    x=247, y=197,
    width=178,
    height=36)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=registrar_uso_insumo,
    relief="flat")

b2.place(
    x=479, y=123,
    width=178,
    height=35)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=adicionar_insumo,
    relief="flat")

b3.place(
    x=247, y=125,
    width=178,
    height=34)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image=entry0_img)

entry0 = Text(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=250, y=502,
    width=410,
    height=114)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry1.place(
    x=377, y=278,
    width=280,
    height=31)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry2.place(
    x=377, y=324,
    width=280,
    height=31)

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry3.place(
    x=377, y=372,
    width=280,
    height=31)

entry4_img = PhotoImage(file=f"img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image=entry4_img)

entry4 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry4.place(
    x=377, y=420,
    width=280,
    height=31)

window.resizable(False, False)
window.mainloop()