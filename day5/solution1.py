import re

seeds = []
seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

def parse_file():
    with open("input.txt", 'r') as input:
        whole_file = input.read()
        global seeds
        seeds = re.findall(r'seeds:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split(" ")

        global seed_to_soil
        seed_to_soil = re.findall(r'seed-to-soil map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global soil_to_fertilizer
        soil_to_fertilizer = re.findall(r'soil-to-fertilizer map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global fertilizer_to_water 
        fertilizer_to_water = re.findall(r'fertilizer-to-water map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global water_to_light
        water_to_light = re.findall(r'water-to-light map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global light_to_temperature
        light_to_temperature = re.findall(r'light-to-temperature map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global temperature_to_humidity
        temperature_to_humidity = re.findall(r'temperature-to-humidity map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")
        
        global humidity_to_location
        humidity_to_location = re.findall(r'humidity-to-location map:\s*(\d+(?:\s+\d+)*)', whole_file)[0].split("\n")

def calculate_location_for_seed(seed):
    soil = calculate_mapping_with_ranges(int(seed), seed_to_soil)
    fertilizer = calculate_mapping_with_ranges(int(soil), soil_to_fertilizer)
    water = calculate_mapping_with_ranges(int(fertilizer), fertilizer_to_water)
    light = calculate_mapping_with_ranges(int(water), water_to_light)
    temperature = calculate_mapping_with_ranges(int(light), light_to_temperature)
    humidity = calculate_mapping_with_ranges(int(temperature), temperature_to_humidity)
    location = calculate_mapping_with_ranges(int(humidity), humidity_to_location)
    return location

def calculate_mapping_with_ranges(key, ranges):
    location = int(key)
    for range in ranges:
        destination_range_start, source_range_start, range_length = range.split(" ")
        source_range_end = int(source_range_start) + int(range_length)

        if int(key) >= int(source_range_start) and int(key) <= source_range_end:
            # We are in range then calculate the location
            move_positions = abs(int(source_range_start) - int(key))
            location = int(destination_range_start) + move_positions
            break

    return location 

def solution():
    location = float('inf')
    parse_file()
    for seed in seeds:
        print(f"Calculating Seed: {seed}...")
        seed = int(seed)
        location = min(calculate_location_for_seed(seed), location)

    return location

if __name__ == "__main__":
    print(solution())