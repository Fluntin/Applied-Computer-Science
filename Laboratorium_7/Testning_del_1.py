from Lab1_Pokemon import Pokemon
from DictHash_Class import DictHash
import os
import csv

#------------------------------------------------------------------------------------------------------------

def get_data ():
    
    pokemon_matrix=[]
    with open ("pokemon.csv", "r") as csvfile:
        row = csv.reader(csvfile)
        for row in row:
            pokemon_matrix.append(row)  
            
    return(pokemon_matrix)

#------------------------------------------------------------------------------------------------------------

def create_pokemon (pokemon_matrix):
    pokemon_list=[]
    for i in range (0, len(pokemon_matrix)):
        pokemon_list.append(Pokemon(pokemon_matrix[i][0],pokemon_matrix[i][1],pokemon_matrix[i][2],
                               pokemon_matrix[i][3],pokemon_matrix[i][4],pokemon_matrix[i][5],
                               pokemon_matrix[i][6],pokemon_matrix[i][7],pokemon_matrix[i][8],
                               pokemon_matrix[i][9],pokemon_matrix[i][10],pokemon_matrix[i][11],
                               pokemon_matrix[i][12]))
    return(pokemon_list)

#------------------------------------------------------------------------------------------------------------

def show_menu ():
    
    print("1 -> Find pokemon by name")
    print("2 -> End program ")
    print('\n')
    
#------------------------------------------------------------------------------------------------------------   

def find_by_name(pokemon_hash):
    
    print("Name of the Pokemon?")
    val=input()
    os.system('cls')
    
    pokemon="Not Found"
    
    pokemon=pokemon_hash.search(val) 
        
    return(pokemon)

#------------------------------------------------------------------------------------------------------------   

def main ():
    
    pokemon_list=create_pokemon(get_data())
    pokemon_hash=DictHash()
    
    for pokemon in pokemon_list:
        pokemon_hash.store(pokemon.Name, pokemon)
     
    while True:
        
        show_menu()
        val=int(input())
        os.system('cls')
        
        if val==1:
            print(find_by_name(pokemon_hash))

            
        elif val==2:
            print("Välkommen åter!")
            break
        
        else:
            print("Välj ett giltigt alternativ.")
            print('\n')

#------------------------------------------------------------------------------------------------------------        

main()