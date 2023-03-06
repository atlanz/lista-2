import os 
# Faça um programa que leia um número inteiro e exiba a soma dos seus dígitos.

numero = int(input("Digite um número inteiro: "))
soma = 0

while numero > 0:
    digito = numero % 10
    soma += digito
    numero = numero // 10

print("A soma dos dígitos do número é:", soma)

os.system("pause")