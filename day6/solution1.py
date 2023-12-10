import re


def solution():
    total = 1

    with open("input.txt", 'r') as input:
        whole_file = input.read()
        times = [x for x in re.findall(r'Time:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split(" ") if x != ""]
        record_distances = [x for x in re.findall(r'Distance:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split(" ") if x != ""]

        for i in range(len(times)):
            time = times[i]
            record_to_beat = record_distances[i]

            pressed = 1
            count = 0
            while pressed <= int(time):
                distance = pressed * (int(time) - pressed)
                
                if distance > int(record_to_beat):
                    count += 1
                
                pressed += 1

            total *= count

        return total

if __name__ == "__main__":
    print(solution())