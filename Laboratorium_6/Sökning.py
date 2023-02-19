from Soundtrack_Class import Soundtrack
import timeit

#----------------------------------------------------------------
def getdata():
    lista = list()
    with open("unique_tracks.txt", "r", encoding="utf8") as track:
        for rad in track:
            track_info = rad.strip().split("<SEP>")
            lista.append(Soundtrack(track_info[0], track_info[1], track_info[2], track_info[3] ))
    print("getdata=>Done")
    return lista

#----------------------------------------------------------------
#1.Linjärsökning i en osorterad lista.

def linjärsökning(lista, testartist):
    count=0
    for song in lista:
        count+=1
        if song.artist == testartist:
            break
    #print("linjärsökning=>Done")
    print(count)
        
#----------------------------------------------------------------
#2. Binärsökning i en sorterad lista. Sortera listan först med pythons sort-metod.

def binärsökning(lista, testartist):
    print("binärsökning=>Start")
  
    low = 0
    high = len(lista)-1
    found = False
    while low <= high and not found:
        middle = (low + high)//2
        if lista[middle].artist == testartist:
            found = True
        else:
            if testartist < lista[middle].artist:
                high = middle - 1
            else:
                low = middle + 1
         
    print("binärsökning=>Done")
    return found

#----------------------------------------------------------------
#3. Sökning i hashtabell. Här kan du antingen använda pythons dict eller din egen hashtabell.

def hashtabellsökning(hashtabell, testartist):
       return hashtabell[testartist]


#----------------------------------------------------------------
def create_hashtabell(lista):
    hashtabell=dict()
    for element in lista:
        hashtabell[element.artist]=element
    return(hashtabell)
        
#----------------------------------------------------------------
#Skriv ett program som tar tid på varje variant av sökning ovan. 

if __name__ == "__main__":
    
    lista = getdata()
    hashtabell=create_hashtabell(lista)
    sorted_lista=sorted(lista)
    
    n = len(lista)
    print("Antal element =", n)

    last = lista[n-1]
    testartist = last.artist

    lintime = timeit.timeit(stmt = lambda: linjärsökning(lista, testartist), number = 1000)
    bintime = timeit.timeit(stmt = lambda: binärsökning(sorted_lista, testartist), number = 1000)
    hashtime = timeit.timeit(stmt = lambda: hashtabellsökning(hashtabell, testartist), number = 1000)

    print("Linjärsökningen tog", round(lintime, 4) , "sekunder")
    print("Binärsökning tog", round(bintime, 10), "sekunder")
    print("Hashsökning tog", round(hashtime, 10), "sekunder")
    print(len(lista))