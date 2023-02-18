from Soundtrack_Class import Soundtrack
import timeit

#----------------------------------------------------------------
def getData():
    music_library = list()
    with open("unique_tracks.txt", "r", encoding="utf8") as track:
        for rad in track:
            track_info = rad.strip().split("<SEP>")
            music_library.append(Soundtrack(track_info[0], track_info[1], track_info[2], track_info[3] ))
    
    return music_library
#----------------------------------------------------------------
#1. quicksort
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v

#----------------------------------------------------------------
#2. bubblesort
def bubblesort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i].title>lista[i+1].title:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                # lista[i], lista[i+1] = lista[i+1], lista[i]

#----------------------------------------------------------------

if __name__ == "__main__":
    
    lista = getData()
    lista = lista[:10000]

    n = len(lista)
    print("Antal element =", n)

    quicksorttime = timeit.timeit(stmt = lambda: quicksort(lista), number = 1)
    bubblesorttime = timeit.timeit(stmt = lambda: bubblesort(lista), number = 1)

    print("Quicksort tog", round(quicksorttime, 4) , "sekunder")
    print("Bubblesort tar", round(bubblesorttime, 4), "sekunder")