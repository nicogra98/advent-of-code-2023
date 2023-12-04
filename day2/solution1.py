def solution():
    total = 0
    intial_config = {
        "blue": 14,
        "green": 13,
        "red": 12
    }
    with open("input.txt", 'r') as input:
        for id, line in enumerate(input.readlines()):
            game_sets = line.split(":")[1].split(";")
            print(game_sets)
            valid_game = True
            for set in game_sets:
                set = set.strip()
                plays = set.split(",")
                
                for play in plays:
                    play = play.strip()
                    if int(play.split(" ")[0]) > intial_config[play.split(" ")[1]]:
                       valid_game = False
                       break

                if not valid_game:
                    break
            
            if valid_game:
                total += id + 1

    return total
                




if __name__ == "__main__":
    print(solution())