import random
import time

vetor = list(range(0,1000)) #gera vetor com mil posições, se quiser mais ou menos só mudar o segundo valor
random.shuffle(vetor) #funcao que embaralha os valores do vetor

print(vetor) #apenas exibe o vetor já embaralhado (em vetores de até uns 50 valores é ok visualizar, mas se expandir pra vetores de mil valores ou mais, já nao fica bom, ai recomendo comentar essa linha...)

##Cada vX desse corresponde a um algoritmo de ordenação, dessa forma é posssivel testar a performace com o mesmo vetor em todos eles!
vb = vetor #Bubble Sort
vs = vetor #Selection Sort
vi = vetor #Insertion Sort
vh = vetor #Shell Sort

def bubble_sort(vb): #funcao Bubble Sort

    fim = len(vb)

    while fim > 0:

        i = 0
        #percorrendo o vetor de zero até fim
        while i < fim-1:
            if vb[i] >vb[i+1]:
                temp = vb[i]
                vb[i] = vb[i+1]
                vb[i+1] = temp
            i += 1
        fim -= 1

antes = time.time()
bubble_sort(vb)
depois = time.time()

total = (depois - antes)*1000

print("Bubble sort: %0.2f ms" % total) #Exibe o tempo total de execução deste algoritmo

def selection_sort(vs):
    i = 0
    while i < len(vs) - 1:
        menor = i
        j = i + 1
        while j < len(vs):
            if vs[j] < vs[menor]:
                menor = j

            j += 1

        if menor != i:
            temp = vs[i]
            vs[i] = vs[menor]
            vs[menor] = temp
        i += 1

antes = time.time()
selection_sort(vs)
depois = time.time()

total = (depois - antes)*1000

print("Selection Sort: %0.2f ms" % total) #Exibe o tempo total de execução deste algoritmo

def insertion_sort(vi):
    i = 1
    while 1 < len(vi):
        temp = vi[i]
        trocou = False
        j = i -1
        while j>= 0 and vi[j] > temp:
            vi[j+1] = vi[j]
            trocou = True
            j -= 1

        if trocou:
            v[j+1] = temp
        i += 1

antes = time.time()
selection_sort(vi)
depois = time.time()

total = (depois - antes)*1000

print("Insertion Sort: %0.2f ms" % total) #Exibe o tempo total de execução deste algoritmo

def shell_sort(vh):

    h = len(vh)//2

    while h > 0:
        i = h

        while i < len(vh):
            temp = vh[i]
            trocou = False
            j = i -h

            while j >= 0 and vh[j] > temp:
                vh[j+h] = vh[j]
                trocou = True
                j -= h

            if trocou:
                v[j+h] = temp
            i+= 1
        h = h // 2

antes = time.time()
shell_sort(vh)
depois = time.time()

total = (depois - antes)*1000

print("Shell Sort: %0.2f ms" % total) #Exibe o tempo total de execução deste algoritmo
