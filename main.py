from tkinter import *
from gtts import *
from playsound import playsound
import os

root = Tk()
root.title = ('Texto em fala')
root.geometry('500x420')
root.maxsize(500, 420)
root.minsize(500, 420)
root.configure(bg='#1d1d1d')

def margem(altura):
    tela = Canvas(root, width=500, height=altura, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
    tela.pack()
def botao(texto, comando, padx):
    botao = Button(root,
            text=texto,
            padx=padx,
            pady=20,
            command= comando,
            fg='#FFFFFF',
            activebackground='#C69749',
            activeforeground='#FFFFFF',
            bg='#C69749',
            relief=FLAT,
            font=('Montserrat', 12, 'bold'))
    botao.pack()
def resetar():
    e.delete(0, 'end')
    os.remove('arquivo_fala.mp3')
def texto_em_fala():
    texto_inserido = e.get()
    fala = gTTS( text = texto_inserido, lang = 'pt', slow=False, tld='com.br' )
    arquivo_fala = 'arquivo_fala.mp3'
    fala.save(arquivo_fala)
    playsound(arquivo_fala)
margem(20)
titulo = Label(root, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 18, 'bold'), text='Conversor texto em fala')
titulo.pack()
margem(30)
insere_texto = Label(root, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 16, 'bold'), text='Insira o texto:')
insere_texto.pack()
margem(30)
e = Entry(root, width=25, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#000000', font=('Montserrat', 21, 'bold'), justify=CENTER)
e.pack()
margem(20)
play = botao('INICIAR', texto_em_fala, 37)
margem(10)
reset = botao('RESETAR', resetar, 30)
root.mainloop()