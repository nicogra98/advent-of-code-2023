import re


def solution():
    total = 0

    with open("input.txt", 'r') as input:
        cards = input.readlines()

        for card in cards:
            winning, our_numbers = card.strip().split(": ")[1].split(" | ")
            winning_list = re.findall(r'\d+', winning)
            our_numbers_list = re.findall(r'\d+', our_numbers)

            common_elemets = set(winning_list).intersection(set(our_numbers_list))

            if len(common_elemets):
                total += 2 ** (len(common_elemets) - 1)
    
    return total

if __name__ == "__main__":
    print(solution())