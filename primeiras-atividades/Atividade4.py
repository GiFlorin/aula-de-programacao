#Objetivo: Adicionar os botoes e as funcionalidades de:
    #Potencia
    #Raiz
    #1/x

import tkinter as tk
import math

calculo=str()

def inserir_texto(x):
    
    global calculo

    calculo=calculo+x
    texto.delete(1.0,"end")
    texto.insert(1.0,calculo)
    

def avaliar():

    global calculo

    a=str(eval(texto.get(1.0,"end")))
    calculo=str()
    inserir_texto(a)

def apagar():

    global calculo

    calculo=str()
    texto.delete(1.0,"end")

def raiz():
    a=(eval(texto.get(1.0,"end"))** 0.5)
    apagar()
    inserir_texto('{:.0f}'.format(a))

def umsobrex():
    a=str((1/eval(texto.get(1.0,"end"))))
    apagar()
    inserir_texto(a)

#bônus por botões coloridinhos?


janela=tk.Tk()

janela.config(bg = '#e5dfdc')

#caixa de texto
texto = tk.Text(janela, height=5, width= 55, font=("Arial", 14), bg = '#e5dfdc')
texto.grid(columnspan=5)

#botao 1
botao1 = tk.Button(janela, text="1",command=lambda:inserir_texto("1"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao1.grid(column=1,row=2)

#botao 2
botao2 = tk.Button(janela, text="2",command=lambda:inserir_texto("2"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao2.grid(column=2,row=2)

#botao 3
botao3 = tk.Button(janela, text="3",command=lambda:inserir_texto("3"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao3.grid(column=3,row=2)

#botao 4
botao4 = tk.Button(janela, text="4",command=lambda:inserir_texto("4"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao4.grid(column=1,row=3)

#botao 5
botao5 = tk.Button(janela, text="5",command=lambda:inserir_texto("5"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao5.grid(column=2,row=3)

#botao 6
botao5 = tk.Button(janela, text="6",command=lambda:inserir_texto("6"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao5.grid(column=3,row=3)

#botao 7
botao7 = tk.Button(janela, text="7",command=lambda:inserir_texto("7"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao7.grid(column=1,row=4)

#botao 8
botao8 = tk.Button(janela, text="8",command=lambda:inserir_texto("8"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao8.grid(column=2,row=4)

#botao 9
botao9 = tk.Button(janela, text="9",command=lambda:inserir_texto("9"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao9.grid(column=3,row=4)

#botao 0
botao0 = tk.Button(janela, text="0",command=lambda:inserir_texto("0"), height=4,width=16, font=("Arial", 12), bg = '#d4cac4', relief = 'ridge')
botao0.grid(column=2,row=5)

#botao parenteses(
botao_abrepar = tk.Button(janela, text="(",command=lambda:inserir_texto("("), height=4,width=16, font=("Arial", 12), bg = '#d4b483', relief = 'ridge')
botao_abrepar.grid(column=1,row=5)

#botao parenteses)
botao_fechapar = tk.Button(janela, text=")",command=lambda:inserir_texto(")"), height=4,width=16, font=("Arial", 12), bg = '#d4b483', relief = 'ridge')
botao_fechapar.grid(column=3,row=5)

#botao mais
botao_mais = tk.Button(janela, text="+",command=lambda:inserir_texto("+"), height=4,width=16, font=("Arial", 12), bg='#c1666b', relief = 'ridge')
botao_mais.grid(column=4,row=2)

#botao menos
botao_menos = tk.Button(janela, text="-",command=lambda:inserir_texto("-"), height=4,width=16, font=("Arial", 12), bg='#c1666b', relief = 'ridge')
botao_menos.grid(column=4,row=3)

#botao multiplicar
botao_mult = tk.Button(janela, text="*",command=lambda:inserir_texto("*"), height=4,width=16, font=("Arial", 12), bg='#c1666b', relief = 'ridge')
botao_mult.grid(column=4,row=4)

#botao dividir
botao_div = tk.Button(janela, text="/",command=lambda:inserir_texto("/"), height=4,width=16, font=("Arial", 12), bg='#c1666b', relief = 'ridge')
botao_div.grid(column=4,row=5)

#botao igual
botao_igual = tk.Button(janela, text="=",command=lambda:avaliar(), height=4,width=33, font=("Arial", 12), bg='#48a9a6', relief = 'ridge')
botao_igual.grid(column=1,row=6, columnspan = 2)

#botao clear
botao_C = tk.Button(janela, text="C",command= lambda:apagar(), height=4,width=33, font=("Arial", 12), bg='#48a9a6', relief = 'ridge')
botao_C.grid(column=3,row=6, columnspan = 2)
#botao potencia
botao_po=tk.Button(janela, text="**",command=lambda:inserir_texto("**"),width=13, height=4,font=("Arial",12), bg='#c1666b', relief = 'ridge')
botao_po.grid(column=5,row=2)
#botao raiz
botao_raiz=tk.Button(janela, text="Raiz",command=lambda:raiz(),width=13, height=4,font=("Arial",12), bg='#c1666b', relief = 'ridge')
botao_raiz.grid(column=5,row=3)
#botao 1/x
botao_1x=tk.Button(janela, text="1/x",command=lambda:umsobrex(),width=13, height=4,font=("Arial",12), bg='#c1666b', relief = 'ridge')
botao_1x.grid(column=5,row=4)

janela.mainloop()
