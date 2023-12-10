def solution():
    numbers = []
    number = ""
    valid = False

    with open("input.txt", 'r') as input:
        rows = input.read().strip().split("\n")
        input_array = [list(row) for row in rows]
        
        for i in range(len(input_array)):
            for j in range(len(input_array[0])):
                if input_array[i][j] in "01234566789":
                    number += input_array[i][j]
                    valid = look_in_all_directions(i, j, input_array) if not valid else valid
                
                elif number != "":
                        numbers.append((number, valid))
                        number = ""
                        valid = False
            
            if number != "":
                        numbers.append((number, valid))
                        number = ""
                        valid = False


                    
    return sum([int(number) for number, valid in numbers if valid])
                
def look_in_all_directions(i, j, input_array):
    rows = len(input_array)
    columns = len(input_array[0])
    # Left
    if (j - 1) >= 0 and input_array[i][j - 1] not in "0123456789.":
        return True
    # Right
    if (j + 1) < columns and input_array[i][j + 1] not in "0123456789.":
        return True
    # Up
    if (i - 1) >= 0 and input_array[i - 1][j] not in "0123456789.":
        return True
    # Down
    if (i + 1) < rows and input_array[i + 1][j] not in "0123456789.":
        return True

    # Corner Up Left
    if (j - 1) >= 0 and (i - 1) >= 0 and input_array[i - 1][j - 1] not in "0123456789.":
        return True
    
    # Corner Up Right
    if (j + 1) < columns and (i - 1) >= 0 and input_array[i - 1][j + 1] not in "0123456789.":
        return True
    
    # Corner Down Left
    if (j - 1) >= 0 and (i + 1) < rows and input_array[i + 1][j - 1] not in "0123456789.":
        return True

    # Corner Down Right
    if (j + 1) < columns and (i + 1) < rows and input_array[i + 1][j + 1] not in "0123456789.":
        return True
                
    # Default
    return False



if __name__ == "__main__":
    print(solution())