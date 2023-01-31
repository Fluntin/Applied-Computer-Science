from bintreeFile2 import Bintree

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as swedish:
    for row in swedish:
        word = row.strip()                # Ett trebokstavsord per row
        if word in svenska:
            print(word, end = " ") 
        else:
            svenska.put(word)             # in i sökträdet
print("\n")

english = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        for ordet in rad.split():
            if ordet in english:
                pass
            elif ordet in svenska:
                english.put(ordet)
                print(ordet, end=" ")

#Com#
print("\n")