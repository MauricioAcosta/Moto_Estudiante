#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from sys import stdin
import sys.path.append("..")
from Pila import *

class Nodo:
	def __init__(self , valor):
		self.valor = valor
		self.izquierda = None
		self.derecha = None

class ArbolPosFijo:
	diccionario={}
	def buscarOperador(self, caracter):
		if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/'):
			return 1
		elif(type(caracter)==int):
			return 2
		else:
			return 0

	def construirDiccionario(self,indice,valor):
		self.diccionario[indice]=[valor]
	def getValorDiccionario(self,indice):
		return self.diccionario.get(indice)

	def variablesDiccionario(self):
		 for i in self.diccionario:
			 print ("variable: {} --> Valor: {}".format(i,str(self.getValorDiccionario(i))))


	def evaluar(self, arbol):
		if arbol.valor=='+':
			return self.evaluar(arbol.izquierda)+self.evaluar(arbol.derecha)
		if arbol.valor=='-':
			return self.evaluar(arbol.izquierda)-self.evaluar(arbol.derecha)
		if arbol.valor=='*':
			return self.evaluar(arbol.izquierda)*self.evaluar(arbol.derecha)
		if arbol.valor=='/':
			try:
				return self.evaluar(arbol.izquierda)/self.evaluar(arbol.derecha)
			except ZeroDivisionError:
				print("Error!! ---> Division entre cero")
				sys.exit()
		try:
			return float(arbol.valor)
		except:
			return (self.getValorDiccionario(arbol.valor))[0]

	def construirArbol(self, posfijo):
		posfijo.pop()
		variable=posfijo.pop()
		pilaOperador = Pila()
		#Recorra todo el string
		for caracter in posfijo :

			# si NO es operador lo apila
			if self.buscarOperador(caracter)!=1:
				arbol = Nodo(caracter)
				pilaOperador.apilar(arbol)

			# Operador
			else:
				# desapila dos nodos
				arbol = Nodo(caracter)
				arbol1 = pilaOperador.desapilar()
				arbol2 = pilaOperador.desapilar()

				# los convierte en hijos
				arbol.derecha = arbol1
				arbol.izquierda = arbol2

				# Anade nuevo arbol a la pila
				pilaOperador.apilar(arbol)

		# Al final el ultimo elemento de la pila sera el arbol
		arbol = pilaOperador.desapilar()
		self.construirDiccionario(variable,self.evaluar(arbol))
		return self.evaluar(arbol)

def main():
	obj = ArbolPosFijo()
	while True:

	  expresion = stdin.readline().split()
	  if not expresion:

		  print ('--*-- Variables Finales --*--')
		  obj.variablesDiccionario()
		  break
	  
	  print (' '.join(expresion))
	  print ("El valor resultante es: {} ".format(str(obj.construirArbol(expresion))))

if __name__ == '__main__':
	main()
