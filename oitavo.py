import os 
# Faça um programa que leia um número inteiro e exiba o seu valor em binário.

numero = int(input("Digite um número inteiro: "))
binario = ""

while numero > 0:
    binario = str(numero % 2) + binario
    numero //= 2

print("O valor em binário é:", binario)

os.system("pause")