import random
import time

vetor = list(range(0,1000)) #gera vetor
random.shuffle(vetor)
print(vetor)

##Cada vX desse corresponde a um algoritmo de ordenação, dessa forma é posssivel testar a performace com o mesmo vetor em todos eles!
vb = vetor.copy() #Bubble Sort
vs = vetor.copy() #Selection Sort
vi = vetor.copy() #Insertion Sort
vh = vetor.copy() #Shell Sort
vm = vetor.copy() #Merge Sort
vq = vetor.copy() #Quick Sort


def bubble_sort(vb):

    fim = len(vb)

    while fim > 0:

        i = 0
        #percorrendo o vetor de zero até fim
        while i < fim-1:
            if vb[i] > vb[i+1]:
                temp = vb[i]
                vb[i] = vb[i+1]
                vb[i+1] = temp
            i += 1
        fim -= 1

antes = time.time()
bubble_sort(vb)
depois = time.time()

total = (depois - antes)*1000
print("Bubble sort: %0.2f ms" % total)

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

print("Selection Sort: %0.2f ms" % total)

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

print("Insertion Sort: %0.2f ms" % total)

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
                vh[j+h] = temp
            i+= 1
        h = h // 2

antes = time.time()
shell_sort(vh)
depois = time.time()

total = (depois - antes)*1000

print("Shell Sort: %0.2f ms" % total)


def merge_sort(vm, p, r): #onde 'p' representa a posição inicial do vetor e 'r' a posicao final
    if p < r: #condicao de parada (condicao de existencia)
        q = (p+r) // 2 #posicao do elemento do meio
        merge_sort(vm, p, q) #quebrando o vetor em um subvetor 1 (metade da esquerda )
        merge_sort(vm, q+1, r) #quebrando o vetor em um subvetor 2 (metade da direita)
        intercalar(vm, p, q, r)

def intercalar(vm, p, q, r): #comparar elemento dos subvetores e ir colocando no vetor real de forma ordenada
    temp = vm.copy() #copia do vetor real
    i = p #contador do subvetor 1
    j = q+1 #contador do subvetor 2
    k = p #contador do vetor real 'vm'

    while k <= r: #momento em que a INTERCALAÇÃO será realizada
        if i > q: #entra quando nao tiver mais elementos no subvetor 1
            vm[k] = temp[j]
            j += 1
        elif j > r: #entra quando nao tiver mais elementos no subvetor 2
            vm[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]: #neste caso, retirar o elemento do subvetor 1
            vm[k] = temp[i]
            i += 1
        else: #neste caso, retirar o elemento do subvetor 2
            vm[k] = temp[j]
            j += 1

        k += 1
antes = time.time()
merge_sort(vm, 0, len(vm)-1)
depois = time.time()

total = (depois - antes)*1000

print("Merge Sort: %0.2f ms" % total)

#Quick Sort Variante Lomuto (pivo extrema esquerda)
def quick_sort(vq, p, r):
    if p < r: #Condicao de Parada (ou condicao de existencia)
        q = particionar(vq, p, r)
        quick_sort(vq, p, q-1) #Pivotar a Esquerda (Ordenar os elementos menores do que o Pivô)
        quick_sort(vq, q+1, r) #Pivotar a Direita (Ordenar os elementos maiores do que o Pivô)

def particionar(vq, p, r):
    x = vq[p] #Escolhendo o Pivo (É o primeiro elemento da esquerda)
    i = p #Destino final do Pivô
    j =  p + 1 #Contador para percorrer o restante do vetor

    while j<= r: #Percorrer o vetor
        if vq[j] < x: #detectou-se um elemento menor que o pivô, incrementa o i
            i += 1
            trocar(vq, i, j)
        j += 1 #passa para o proximo elemento

    trocar(vq, p, i)

    return i

def trocar(v, n, m):
    temp = vq[n]
    vq[n] = vq[m]
    vq[m] = temp
antes = time.time()
quick_sort(vq, 0, len(vq)-1)
depois = time.time()

total = (depois - antes)*1000

print("Quick Sort %0.2f ms" %total)
