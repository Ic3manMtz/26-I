#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:04:56 2020
@author: Adriana Perez Espinosa

"""
import TipoToken
import SubTipoToken
import Token


class AnalizadorLexico:
    
    numLinea=1
    L=[]
    codigo=""
    def __init__(self,programa):
        
        archivo = open(programa, 'r') 
        lineas = archivo.readlines() 
        for linea in lineas: 
            self.codigo=self.codigo+linea
               
    
    def obtenerToken(self):
        
        if len(self.L)>0:
            return self.L.pop(0)
        return None
    
    def regresarToken(self,t):
        
        self.L.insert(0,t)
    
    def esPalabraReservada(self,lexeme):
   
        return None
        
    
    def crearLista(self):
        
        index=0
        c=self.codigo[index]
        while (index<len(self.codigo)):
            c=self.codigo[index]

            if c==">" or c=="<":
                if c == ">":
                    index=index+1
                    if(index < len(self.codigo)):
                        c=self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,None,">=",self.numLinea)
                            self.L.append(t)
                        else:
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,None,">",self.numLinea)
                            self.L.append(t)
                else:
                    index=index+1
                    if(index < len(self.codigo)):
                        c=self.codigo[index]
                        if c == "=":
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,None,"<=",self.numLinea)
                            self.L.append(t)
                            index=index+1
                        else:
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,None,"<",self.numLinea)
                            self.L.append(t)
                    else:       
                        print("Hemos terminado") 
                        
            else:        
                print("Error, simbolo extranio ",c) 
                index=index+1                
        print("Elementos: ",len(self.L))
