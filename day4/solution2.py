import re


def solution():
    total = 0

    with open("input.txt", 'r') as input:
        cards = input.readlines()
        counts = [1 for card in cards]

        for i, card in enumerate(cards):
            winning, our_numbers = card.strip().split(": ")[1].split(" | ")
            winning_list = re.findall(r'\d+', winning)
            our_numbers_list = re.findall(r'\d+', our_numbers)

            common_elemets = set(winning_list).intersection(set(our_numbers_list))

            for j in range(1, len(common_elemets) + 1):
                counts[i + j] += 1 * counts[i]

    return sum(counts)

if __name__ == "__main__":
    print(solution())