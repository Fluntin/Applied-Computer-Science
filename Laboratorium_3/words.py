from bintreeFile2 import Bintree

print("\n")
swedish = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as swedish:
    for row in swedish:
        word = row.strip()                # Ett trebokstavsord per row
        if word in swedish:
            print(word, end = " ") 
        else:
            swedish.put(word)             # in i sökträdet
print("\n")

english = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        for ordet in rad.split():
            if ordet in english:
                pass
            elif ordet in swedish:
                english.put(ordet)
                print(ordet, end=" ")

#Com#
print("\n")