from math import prod


def solution():
    numbers = set()
    number = ""
    total = 0

    with open("input.txt", 'r') as input:
        rows = input.read().strip().split("\n")
        input_array = [list(row) for row in rows]
        
        for i in range(len(input_array)):
            for j in range(len(input_array[0])):
                if input_array[i][j] != "*":
                    continue

                adjacent = look_in_all_directions(i, j, input_array)
                number = ""
                numbers = set() 
                if len(adjacent) >= 2:
                    for adjacent_i, adjacent_j in adjacent:
                        while adjacent_j >= 0 and input_array[adjacent_i][adjacent_j] in "0123456789":
                            adjacent_j -= 1

                        while (adjacent_j + 1) < len(input_array[adjacent_i]) and input_array[adjacent_i][adjacent_j + 1] in "0123456789":
                            number += input_array[adjacent_i][adjacent_j + 1]
                            adjacent_j += 1

                        numbers.add(int(number))
                        number = ""

                    total += prod([x for x in numbers])   
    return total
                
def look_in_all_directions(i, j, input_array):
    rows = len(input_array)
    columns = len(input_array[0])
    adjacent = []
    # Left
    if (j - 1) >= 0 and input_array[i][j - 1] in "0123456789":
        adjacent.append((i, j - 1))
    # Right
    if (j + 1) < columns and input_array[i][j + 1] in "0123456789":
        adjacent.append((i, j + 1))
    # Up
    if (i - 1) >= 0 and input_array[i - 1][j] in "0123456789":
        adjacent.append((i - 1, j))
    # Down
    if (i + 1) < rows and input_array[i + 1][j] in "0123456789":
        adjacent.append((i + 1, j))

    # Corner Up Left
    if (j - 1) >= 0 and (i - 1) >= 0 and input_array[i - 1][j - 1] in "0123456789":
        adjacent.append((i - 1, j - 1))
    
    # Corner Up Right
    if (j + 1) < columns and (i - 1) >= 0 and input_array[i - 1][j + 1] in "0123456789":
        adjacent.append((i - 1, j + 1))
    
    # Corner Down Left
    if (j - 1) >= 0 and (i + 1) < rows and input_array[i + 1][j - 1] in "0123456789":
        adjacent.append((i + 1, j - 1))

    # Corner Down Right
    if (j + 1) < columns and (i + 1) < rows and input_array[i + 1][j + 1] in "0123456789":
        adjacent.append((i + 1, j + 1))
                
    # Default
    return adjacent



if __name__ == "__main__":
    print(solution())