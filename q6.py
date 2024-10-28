import math

def find_square_for_grains(grains):

    square = math.ceil(math.log2(grains + 1))
    return square
print(find_square_for_grains(16)) 
