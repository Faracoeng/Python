#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:05:41 2019

@author: andre
"""

from Tkinter import *

class calc:
    def _init_(obj, pai):
        obj.frame = Frame(pai) #frmae vai ser o pai da aplicação
        obj.frame.grid()    #contrloe do layout
        obj.dados = Entry(pai,width = 34)
        obj.dados.grid(row = 1, column = 0) #layout tbm
        
        #Criando botoes
        but = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","=","CLR"]
        lin = 1
        col = 0
        for bt in but:
            comando = lambda x = bt:obj.calc(x) #funcao anonima (descartavel aqui)
            obj.botao = Button(obj.frame,text = bt, width = 6 ,command = comando)#command chama a funcao comando
            obj.botao.grid(row = lin, column = col)
            col += 1
            if c > 3:
                c = 0
                r += 1
    def calcular(obj, valor): #valor passa o bota que foi clicado para o metodo   metodo calcular
        if valor == "=":
            todos = "123456789/.*-+"  #limita dados que usuário pode inserir 
            if obj.dados.get()[0] not in todos:
                obj.dados.insert(END, "Operação inválida")
                try:
                    resultado = eval(obj.dados.get())
                    obj.dados.insert(END,"=" + str(resultado))
                except obj.dados.insert(END,"Deu ruim!"):
        elif (valor == "CLR"):
            obj.dados.delete(0, END)
        else:
            if "=" in  obj.dados.get():
                obj.dados.delete(0, END)
            obj.dados.insert(END, valor)
    root = TK() #instancia
    root.title("Calculadora")
    Calculadora(root)
    root.mainloop()