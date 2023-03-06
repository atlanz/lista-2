import os 
# Faça um programa que leia um número inteiro e exiba todos os seus divisores.

# Lê o número inteiro a ser processado
numero = int(input("Digite um número inteiro: "))

# Inicializa uma lista para armazenar os divisores
divisores = []

# Encontra todos os divisores do número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Exibe os divisores encontrados
print("Os divisores de", numero, "são:", divisores)

os.system("pause")