import math

# We will use the following constants in our program
A2_LENGTH = 0.5946035575013605
A2_WIDTH = 0.42044820762685725

def main():
    
    # First I need to deal with the input. I will read the first line and ignore it.
    # The only think we are interested in is the second line 
    # which contains the the amount of paper available.
    
    _ = input() 
    resources = input()
    
    # Here I will convert the string of numbers into a list of integers.
    resources_list = list(map(int, resources.split()))
    
    # Now I will call the function that will do the actual work.
    if check_if_enough_paper(resources_list):
        
        # if there is enough paper, I will call the recursion function. 
        tape_length = recursion(0, 2, 0, resources_list)
        
        # if the recursion fuction return a value, I will print it.
        if tape_length is not None:
            print(tape_length)
            
        # if the recursion function return None, I will print impossible.
        else:
            print("impossible") 
    
    # if there is not enough paper, I will print impossible.
    else:
        print("impossible")


def recursion(index, need_to_use, tape_length, data):
    
    # Here I check if we have some paper to work with.
    if index >= len(data): 
        return None

    # calculate the length of tape required at a particular level in the recursive function
    # if the index is even then the length of tape required is A2_LENGTH / (2 ** (indx / 2.0))
    # if the index is odd then the length of tape required is A2_WIDTH / (2 ** ((indx - 1) / 2.0))
    if index % 2 == 0:
        length = A2_LENGTH / (2 ** (index / 2.0))  
    else:
        length = A2_WIDTH / (2 ** ((index - 1) / 2.0))

    #avaliable_paper is the amount of paper available at a particular level in the recursive function.
    available_paper = data[index] 

    #tape_length is the total length of tape required to make joints at a particular level in the recursive function.
    #need_to_use is the amount of paper required to make joints at a particular level in the recursive function.
    tape_length +=(need_to_use / 2.0) * length

    # if the available paper is less than the paper required at a particular level in the recursive function
    # then we need to go to the next level
    if available_paper >= need_to_use:
        return tape_length
    else:
        next_level_need_to_use = (need_to_use - available_paper) * 2 # calculate next level need to use
        return recursion(index + 1, next_level_need_to_use, tape_length, data) # return recursion call

# This function checks if there is enough paper to make an A2 sheet.
def check_if_enough_paper(data):
    
    index = 0
    target_area = 2.0
    available_area = 0.0
    
    # enough is a boolean variable that will be true if there is enough paper.
    enough = available_area > target_area or math.isclose(available_area, target_area)

    # while there is still paper and we don't have enough...
    while not enough and index < len(data):
        
        # calculate available area
        available_area = available_area + data[index] * (2 ** -index)
        
        # check if enough
        enough = available_area >= target_area or math.isclose(available_area, target_area)
        
        # increment index
        index += 1

    return enough # return if enough


if __name__ == "__main__":
    main()
