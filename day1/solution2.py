
def solution():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers_map = {
        "zero": "zero0zero",
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine"
    }
    
    total = 0

    with open("input.txt", 'r') as input:
        for line in input.readlines():
            for k, v in numbers_map.items():
                line = line.replace(k, v)
            
                
            all_numbers = [char for char in line if char in numbers]
            first_number =  all_numbers[0]
            last_number = all_numbers[-1]
            total += int(first_number + last_number)

    return total


if __name__ == "__main__":
    print(solution())