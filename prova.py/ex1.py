import numpy as np

def switch(letra, numero):
    if letra == "c":
        array_crescente = np.arange(1, numero + 1)
        return array_crescente
    elif letra == "d":
        array_decresente = np.arange(numero, 0 , -1)
        return array_decresente
    elif letra == "r": 
        array_random = np.random.randint(0, 32000, size = numero)
        return array_random

with open('prova.py/input3.txt', 'r') as file: #recebe e fecha arquivo 
  conteudo = file.read()
  print(conteudo)
  
#armazenar o número e a letra
numero = ''
letra = ''
print(numero, letra)

for char in conteudo:
    if char.isdigit():
        numero += char
    elif char.isalpha():
        letra = char
        break
    
# Converte numero para inteiro 
numero = int(numero)
    
        
resultado = switch(letra, numero)
print(resultado)

