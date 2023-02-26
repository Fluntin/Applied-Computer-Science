class DictHash:

    def __init__(self):
        self.dicthash = dict()

#Definiera store(nyckel, data) som lagrar data som value i din dictionary, med nyckel som nyckel.
    def store(self, nyckel, data):
        self.dicthash = save(self.dicthash, nyckel, data)

#Definiera metoden __getitem__(self, nyckel) Links to an external site.som anropar din search-metod.
    def __getitem__(self, nyckel):
        return self.search(nyckel)

#Definiera metoden __contains__(self, nyckel) Links to an external site.som returnerar True om nyckel finns i d, False annars.
    def __contains__(self, nyckel):
        return exits(self.dicthash, nyckel)

#-----------------------------------------------------------------------------------------------------------------------------------

#Coupled to the store(self, nyckel, data) function
def save(hash_lista, nyckel, data):
    hash_lista[nyckel] = data
    return hash_lista

#Coupled to the __getitem__(self, nyckel) function
def search(self, nyckel):
    if nyckel in self:
        return self[nyckel]
    else:
        raise Exception("That Pokemon does not exist in the pokedex")

#Coupled to the __contains__(self, nyckel) function
def exits(hash_lista, nyckel):
    
    try:
        print(hash_lista[nyckel])
        return True
    
    except KeyError:
        return False