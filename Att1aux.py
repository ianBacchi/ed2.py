import sys
import random
import os
import time

def arquivo_vazio(arquivo_input): #Verifica se o Arquivo está vazio
    with open(arquivo_input, 'r') as file:
        return os.stat(arquivo_input).st_size == 1

def switch(numero, letra, arquivo_input):
    if arquivo_vazio(arquivo_input): #Para a execução se o arquivo for vazio
        print(f'O arquivo {arquivo_input} está vazio.')
        sys.exit()
        
    try:
        #Abre o arquivo e salva em letra e numero
        with open(arquivo_input, 'r') as file:
            numero = file.readline()
            letra = file.readline()
    except FileNotFoundError: #Verifica se o arquivo existe
        print("Error: O arquivo não foi encontrado")
        sys.exit()
    except IOError: #Verifica se foi aberto com sucesso
        print("Error: Erro ao abrir o arquivo")
        sys.exit()
    
    try: #Verifica se a letra é uma letra
        letra = int(letra)
        print(f"Error: Arquivo com a formatação invalida!")
        sys.exit()
    except ValueError:
        pass

    #Transforma numero em int, e retira o \n da variavel letra
    numero = int(numero)
    letra = letra.rstrip('\n')
    
    return numero, letra

def ordem_crescente(qnt): #Função que gera uma quantidade qnt de valores em ordem crescente
    return list(range(1, qnt + 1))

def ordem_decrescente(qnt): #Função que gera uma quantidade qnt de valores em ordem decrescente
    return list(range(qnt, 0, -1))

def ordem_aleatoria(qnt): #Função que gera uma quantidade qnt de valores em ordem aleatoria entre 0 e 32000
    numeros = list(range(1, qnt + 1))
    random.shuffle(numeros)
    return [random.randint(0, 32000) for _ in range(qnt)]

def insertionSort(lista_num):
    comp = 0
    tempo_execucao = 0
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"

def selectionSort(lista_num):
    comp = 0
    tempo_execucao = 0
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"

def bubbleSort(lista_num):
    comp = 0
    n = len(lista_num)
    
    start_time = time.time()  # Marca o início do tempo de execução

    # Percorre toda a lista_num
    for i in range(n):
        trocou = False  # Flag para verificar se houve troca

        # Últimos elementos já estão na posição correta após cada iteração
        for j in range(0, n - i - 1):
            comp += 1  # Incrementa o contador de comparações
            
            # Compara os elementos adjacentes
            if lista_num[j] > lista_num[j + 1]:
                # Troca os elementos se estiverem na ordem errada
                lista_num[j], lista_num[j + 1] = lista_num[j + 1], lista_num[j]
                trocou = True

        # Se não houve troca, a lista_num já está ordenada
        if not trocou:
            break
    
    end_time = time.time()  # Marca o final do tempo de execução
    tempo_execucao = (end_time - start_time) * 1000000 # Calcula o tempo de execução
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"
 
def mergeSort(lista_num):
    tempo_execucao = 0
    comp = 0
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"

def quickSort(lista_num):
    comp = 0
    tempo_execucao = 0   
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"

def heapSort(lista_num):
    comp = 0
    tempo_execucao = 0
    return f"{lista_num}, {comp} comp, {tempo_execucao}ms"

def chama_algoritimos(lista_num):
    #insertionSort, selectionSort, bubbleSort, mergeSort, quickSort, e heapSort;
    print(f"InsertionSort {insertionSort(lista_num)}")
    print(f"SelectionSort {selectionSort(lista_num)}")
    print(f"BubbleSort {bubbleSort(lista_num)}")
    print(f"MergeSort {mergeSort(lista_num)}")
    print(f"QuickSort {quickSort(lista_num)}")
    print(f"HeapSort {heapSort(lista_num)}")
    
def main():
    arquivo_python = os.path.basename(__file__)
    if len(sys.argv) != 3: #Verifica se foram passados a quantidade de argumentos certos no terminal
        print(f"Error, use: python {arquivo_python} <arquivo_input> <arquivo_output>")
        sys.exit()
        
    arquivo_input = sys.argv[1] #Arquivo de entrada/Leitura
    arquivo_output = sys.argv[2] #Arquivo de saida/Escrita
        
    letra = ''
    qnt = ''
    qnt, letra = switch(qnt, letra, arquivo_input) #Chama a funão que abre e verifica o arquivo, e retorna o que foi lido em 2 variaveis
    if qnt <= 0: #Verifica se o arquivo não contem um numero invalido de tamanho do vetor/lista_num
        print("Error: O arquivo contem um numero invalido para a execução do programa")
        sys.exit()

    if letra == 'c': #Verifica se o arquivo tem o caracter que corresponde a alguma função do programa
        lista_num = ordem_crescente(qnt)
    elif letra == 'd':
        lista_num = ordem_decrescente(qnt)
    elif letra == 'r':
        lista_num = ordem_aleatoria(qnt)
    else: #Sai do programa se o caracter nao for c, d ou r
        print("Error: O arquivo contem uma letra invalida para a execução do programa")
        sys.exit()
    
    chama_algoritimos(lista_num)

if __name__ == "__main__":
    main()

