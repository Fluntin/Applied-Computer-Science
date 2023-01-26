import os
import csv

class Pokemon:
    def __init__(self, Number, Name,Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary):
        self.Number=Number
        self.Name=Name
        self.Type1=Type1
        self.Type2=Type2
        self.Total=Total
        self.HP=HP
        self.Attack=Attack
        self.Defense=Defense
        self.Sp_Def=Sp_Def
        self.Speed=Speed
        self.Sp_Atk=Sp_Atk
        self.Generation=Generation
        self.Legendary=Legendary
    
    def __str__(self):
        return f"{self.Number} {self.Name}  {self.Type1}  {self.Type2} {self.HP} {self.Attack} {self.Defense} {self.Sp_Def} {self.Speed} {self.Sp_Atk} {self.Generation} {self.Legendary}"

    def __lt__(self, other):
        return self.Number<other.Number
    
    
def get_data ():
    
    pokemon_matrix=[]
    with open ("pokemon.csv", "r") as csvfile:
        row = csv.reader(csvfile)
        for row in row:
            pokemon_matrix.append(row)  
            
    return(pokemon_matrix)


def create_pokemon (pokemon_matrix):
    pokemon_list=[]
    for i in range (0, len(pokemon_matrix)):
        pokemon_list.append(Pokemon(pokemon_matrix[i][0],pokemon_matrix[i][1],pokemon_matrix[i][2],
                               pokemon_matrix[i][3],pokemon_matrix[i][4],pokemon_matrix[i][5],
                               pokemon_matrix[i][6],pokemon_matrix[i][7],pokemon_matrix[i][8],
                               pokemon_matrix[i][9],pokemon_matrix[i][10],pokemon_matrix[i][11],
                               pokemon_matrix[i][12]))
    return(pokemon_list)

def find_by_name(pokemon_list):
    
    print("Name?")
    val=input()
    
    pokemon="Not Found"
    
    for i in range(0,len(pokemon_list)):
        if pokemon_list[i].Name==val:
            pokemon=pokemon_list[i]  
        
    return(pokemon)
  
def show_menu ():
    
    print("1 -> Find pokemon by name")
    print("2 -> End program ")
    print('\n')
    
def main ():
    
    pokemon_list=create_pokemon(get_data())
    
    while True:
        
        show_menu()
        val=int(input())
        os.system('cls')
        
        if val==1:
            print(find_by_name(pokemon_list))

            
        elif val==2:
            print("Välkommen åter!")
            break
        
        else:
            print("Välj ett giltigt alternativ.")
            print('\n')
        
    
main()
