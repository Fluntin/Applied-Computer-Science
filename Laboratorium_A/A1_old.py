import math

A2_LENGTH = 0.5946035575013605
A2_WIDTH = 0.42044820762685725

def main():
    _ = input() # ignore first line

    val = input() # read second line
    
    input_list = list(map(int, val.split())) # convert to list of ints

    if check_if_enough_paper(input_list): # check if enough paper
        tape_length = rec(0, 2, 0.0, input_list) # start recursion
        if tape_length is not None: # if recursion returned a value
            print(tape_length) # print it
        else:
            print("impossible") # else print impossible
    else:
        print("impossible") # else print impossible


def rec(indx, need_to_use, tape_length, data): # recursion function
    if indx >= len(data): # if index is out of bounds
        return None # return None

    leng = A2_LENGTH / (2 ** (indx / 2.0)) if indx % 2 == 0 else A2_WIDTH / (2 ** ((indx - 1) / 2.0)) # calculate length of tape

    available = data[indx] # get available tape

    tape_length = tape_length + (need_to_use / 2.0) * leng # add to tape length

    if available >= need_to_use: # if enough tape
        return tape_length # return tape length
    else:
        next_level_need_to_use = (need_to_use - available) * 2 # calculate next level need to use
        return rec(indx + 1, next_level_need_to_use, tape_length, data) # return recursion call


def check_if_enough_paper(data): # check if enough paper
    indx = 0
    target_area = 2.0
    available_area = 0.0
    enough = available_area > target_area or math.isclose(available_area, target_area)

    while not enough and indx < len(data): # while not enough and index is not out of bounds
        available_area = available_area + data[indx] * (2 ** -indx) # calculate available area
        enough = available_area >= target_area or math.isclose(available_area, target_area) # check if enough
        indx += 1 # increment index

    return enough # return if enough


if __name__ == "__main__":
    main()