
def solution():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total = 0

    with open("input.txt", 'r') as input:
        for line in input.readlines():  
            all_numbers = [char for char in line if char in numbers]
            first_number =  all_numbers[0]
            last_number = all_numbers[-1]
            total += int(first_number + last_number)

    return total


if __name__ == "__main__":
    print(solution())