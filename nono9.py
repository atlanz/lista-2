import os 
#Faça um programa que leia um número e faça a tabuada do mesmo, faça a tabuada sem limite, exemplo 10x100.

numero = int(input("Digite um número inteiro: "))

while True:
    limite = int(input("Digite o limite da tabuada: "))
    for i in range(1, limite+1):
        print(numero, "x", i, "=", numero*i)

os.system("pause")