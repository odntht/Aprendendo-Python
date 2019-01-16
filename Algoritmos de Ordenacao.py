import random
import time

vetor = list(range(0,10000)) #gera vetor
random.shuffle(vetor)

##Cada vX desse corresponde a um algoritmo de ordenação, dessa forma é posssivel testar a performace com o mesmo vetor em todos eles!
vb = vetor #Bubble Sort
vs = vetor #Selection Sort
vi = vetor #Insertion Sort

def bubble_sort(vb):

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