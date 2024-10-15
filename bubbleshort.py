array = [73,	-2,	-62,	-68,	58,	81,	38,	-34,	-21,	-51,	89,	73,	39,	-64,	-92]
print("antes")
def bubbleshort(vetor):
    x = 0
    trocou = True
    while(trocou):
        x = x+1
        print(f"párcial teste  ", array, x)
        trocou = False
        for i in range (0, len(array)-1):
            if(vetor[i]> vetor[i+1]):
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                trocou = True
                
                
                
bubbleshort(vetor = array)
print("---------------")
print("depois")
print(array)                