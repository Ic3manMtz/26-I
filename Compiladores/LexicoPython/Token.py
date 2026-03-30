#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:04:56 2020


@author: Adriana Perez Espinosa
"""
class Token:
   numLinea=0
   def __init__(self,tipotoken, subtipotoken,lexema,numLinea):
      self.tipotoken=tipotoken
      self.subtipotoken=subtipotoken
      self.lexema=lexema
      self.numLinea=numLinea
   def getTipo(self):
      return self.tipotoken
   def getSubType(self):
      return self.subtipotoken
   def getlexema(self):
      return self.lexema
   def setnumLinea(self,n):
      self.numLinea=n
   def getnumLinea(self):
      return self.numLinea
   def __str__(self):
      subtipo = self.subtipotoken if self.subtipotoken is not None else "None"
      return f"Token Identificado\n\t[Tipo: {self.tipotoken}|Subtipo: {subtipo}|Línea: {self.numLinea}]\n\tLexema: {self.lexema}\n"
   

