import math

def solution():
    total = 0
    with open("input.txt", 'r') as input:
        for game in input.readlines():
            game = game.strip()
            max_map = {
                "blue": 0,
                "red": 0,
                "green": 0,
            }
            sets = game.split(": ")[1].split("; ")
            
            for set in sets:
                plays = set.split(", ")

                for play in plays:
                    num, color = play.split(" ")
                    max_map[color] = max(max_map[color], int(num))

            total += math.prod(max_map.values())
    return total
                
if __name__ == "__main__":
    print(solution())