import os 
#Faça um programa que leia um número inteiro e exiba todos os seus múltiplos menores que 100.

numero = int(input("Digite um número inteiro: "))

for i in range(1, 100):
    if i % numero == 0:
        print(i)

os.system("pause")