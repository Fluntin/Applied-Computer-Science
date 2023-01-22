import csv
import os

class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defense, spAtk, 
                 spDef, generation, legendary):
        self.name = name
        self.type1 = int(type1)
        self.type2 = int(type2)
        self.total = int(total)
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.spAtk = int(spAtk)
        self.spDef = int(spDef)
        self.generation = int(generation)
        self.legendary = bool(legendary)
    

    def __str__(self):
        return f'{self.name}'
    
    def __lt__(self, other):
        return self.total < other.total
    
ß
def get_pokelist(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        csv_matrix = list(reader)
        pokemon_list = []
    
        for i in range(1, len(csv_matrix)):
            pokemon_list.append(Pokemon(csv_matrix[i][1], csv_matrix[i][2],
                        csv_matrix[i][3], csv_matrix[i][4],csv_matrix[i][5],
                        csv_matrix[i][6],csv_matrix[i][7],csv_matrix[i][8],
                        csv_matrix[i][9],csv_matrix[i][10],csv_matrix[i][11],
                        csv_matrix[i][12]))
            
    return pokemon_list

print(get_pokelist('pokemon.csv'))