from Soundtrack_Class import Soundtrack
import timeit
import prettytable

#----------------------------------------------------------------
def getData():
    music_library = list()
    with open("unique_tracks.txt", "r", encoding="utf8") as track:
        for rad in track:
            track_info = rad.strip().split("<SEP>")
            music_library.append(Soundtrack(track_info[0], track_info[1], track_info[2], track_info[3] ))
    
    return music_library
#----------------------------------------------------------------
#1. merge_sort
def merge_sort(list):
    length = len(list)

    if length == 1:
        return list

    mid = length // 2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output
#----------------------------------------------------------------
#2. selection_sort

def selection_sort(list):
    n = len(list)

    for i in range(n-1): 
        min = i

        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        if min != i:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

    return list

#----------------------------------------------------------------
#3. bubblesort
def bubblesort(lista):
    for run in range(len(lista)-1,0,-1):
        for i in range(run):
            if lista[i].title>lista[i+1].title:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                
#----------------------------------------------------------------

if __name__ == "__main__":
    
    lista = getData()
    lista = lista[:1000000]

    n = len(lista)
    print("Antal element =", n)

    mergesorttime = timeit.timeit(stmt = lambda: merge_sort(lista), number = 1)
    #selectionsorttime = timeit.timeit(stmt = lambda: selection_sort(lista), number = 1)
    bubblesorttime = timeit.timeit(stmt = lambda: bubblesort(lista), number = 1)


    print("Mergesort tar", round(mergesorttime, 4), "sekunder")
    #print("Selectionsort tar", round(selectionsorttime, 4), "sekunder")
    print("Bubblesort tar", round(bubblesorttime, 4), "sekunder")
    