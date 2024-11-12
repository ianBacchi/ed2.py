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
    else:
        raise ValueError("Letra inválida. Use 'c', 'd', ou 'r'.")
    
    
with open('/media/a2586509/home/ed2.c/prova.py/input1.txt', 'r') as file: #recebe e fecha arquivo 
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

#insertionSort, selectionSort, bubbleSort, mergeSort, quickSort, e heapSort
        
def insertionshort(vetor, tamanho):
    
#indica qual elemento que vai ser ordenado
    for I in range (1, tamanho):
        auxiliar = vetor[I]
        J = I - 1
        
        while J >= 0 and auxiliar < vetor[J]:
            vetor[J + 1] = vetor[J]
            J = J - 1
        vetor[J + 1] = auxiliar
    return vetor
        
print("Inserionsort: ", insertionshort(resultado,len(resultado)))
resultado = switch(letra, numero)


def selectionshort(V, tam):
    for N in range(tam):
        menor = V[N]
        indice = N
        
        for i in range(N, tam):
            if V[i] < menor:
                menor = V[i]
                indice = i
        if menor != V[N]:
            aux = V[N]
            V[N] = V[indice]
            V[indice] = aux
    return V

print(resultado)
print("selectionsort: ", selectionshort(resultado, len(resultado)))
resultado = switch(letra, numero)


def bubbleshort(vetor):
    x = 0
    trocou = True
    while(trocou):
        x = x+1
        
        trocou = False
        for i in range (0, len(vetor)-1):
            if(vetor[i]> vetor[i+1]):
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                trocou = True
    return vetor

print(resultado)
print("bubllesort: ", bubbleshort(resultado))
resultado = switch(letra, numero)

def mergesort(arr):
    # Caso base: se o tamanho do array é 1 ou 0, ele já está ordenado
    if len(arr) <= 1:
        return arr

    # Divide o array ao meio
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]

    # Chama recursivamente o merge_sort nas duas metades
    esquerda = mergesort(esquerda)
    direita = mergesort(direita)

    # Mescla as duas metades ordenadas e retorna o resultado
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Mescla os arrays enquanto ambos têm elementos
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Se ainda restarem elementos em alguma das metades, adiciona ao resultado
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

print(resultado)
print("mergesort: ", mergesort(resultado))
resultado = switch(letra, numero)

def quickshort(V, ini, fim):
    if ini < fim:
        pivo = Particiona(V, ini, fim)
        quickshort(V, ini, pivo - 1)
        quickshort(V, pivo + 1, fim)

def Particiona(V, ini, fim):
    esq = ini + 1
    dir = fim
    pivo = V[ini]
    
    while esq <= dir:
        while esq <= fim and V[esq] <= pivo:
            esq += 1
        while dir >= ini and V[dir] > pivo:
            dir -= 1
        if esq < dir:
            V[esq], V[dir] = V[dir], V[esq]
    
    V[ini], V[dir] = V[dir], V[ini]  # coloca o pivô na posição correta
    return dir 

print(resultado)
quickshort(resultado, 0 ,len(resultado - 1))
resultado = switch(letra, numero)




