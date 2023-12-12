import file_helper as fh

def get_seeds(data_arg):
    """returns array of seeds"""
    for line in data_arg:
        if "seeds:" in line:
            return [int(i) for i in line.split(" ")[1:]]
        
def get_seeds_part2(data_arg):
    """returns array of seeds per part 2 definition"""
    seeds = []
    for line in data_arg:
        if "seeds:" in line:
            vals = line.split(" ")[1:]
            count = 0
            seeds = []
            while(count < len(vals)):
                start = int(vals[count])
                i_range = int(vals[count+1])
                seeds.append({'start': start,
                              'range': i_range})
                count += 2
        return seeds

                

def get_map(data_arg, map_string):
    """returns map"""
    line_found = False
    the_map = []
    for line in data_arg:
        if map_string in line:
            line_found = True
            continue
        if line_found:
            if len(line)==0:
                return the_map
            
            line_numbers = line.split(' ')
            src = int(line_numbers[1])
            dest = int(line_numbers[0])
            range = int(line_numbers[2])
            the_map.append({'src':src,
                            'dest':dest,
                            'range':range})

    return the_map

def get_map_array(data_arg):
    """returns array of maps"""
    seed_to_soil_map = get_map(data_arg, 'seed-to-soil map')
    soil_to_fertilizer_map = get_map(data_arg, 'soil-to-fertilizer map')
    fertilizer_to_water_map = get_map(data_arg, 'fertilizer-to-water map')
    water_to_light_map = get_map(data_arg, 'water-to-light map')
    light_to_temperature_map = get_map(data_arg, 'light-to-temperature map')
    temperature_to_humidity_map = get_map(data_arg, 'temperature-to-humidity map')
    humidity_to_location_map = get_map(data_arg, 'humidity-to-location map')

    return [seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map]

def get_mapped_destination(map_arg, source_arg):
    """returns destination from map with source"""

    for i_map in map_arg:
        if source_arg >= i_map['src'] and source_arg < i_map['src'] + i_map['range']:
            return source_arg - i_map['src'] + i_map['dest']
    return source_arg

def get_mapped_source(map_arg, dest_arg):
    for i_map in map_arg:
        if dest_arg >= i_map['dest'] and dest_arg < i_map['dest'] + i_map['range']:
            return dest_arg - i_map['dest'] + i_map['src']
    return dest_arg

def get_locations(seeds_arg, map_array_arg):
    """returns array of destications based on initial seeds and the array of maps"""
    locations = []
    for seed in seeds_arg:
        source = seed
        for _map in map_array_arg:
            destination = get_mapped_destination(_map, source)
            source = destination
        locations.append(destination)
    return locations

def part_1(data_arg):
    """part 1"""
    seeds = get_seeds(data_arg)
    map_array = get_map_array(data_arg)
    locations = get_locations(seeds, map_array)
    return min(locations)

def get_min_destination_indices(destination_map):
    """provides indices of minimum ranges from destination map"""
    return [i[0] for i in sorted(enumerate([ x['dest'] for x in destination_map ]), key=lambda x:x[1])]

def get_seed_from_location(map_array_arg, location_arg):

    destination = location_arg
    for _map in map_array_arg:
        source = get_mapped_source(_map, destination)
        destination = source
    return source
def has_seed(seeds, seed):
    for i_seed in seeds:
        if seed >= i_seed['start'] and seed < i_seed['start'] + i_seed['range']:
            return True
    
    return False

def part_2(data_arg):
    """part 2"""
    seeds = get_seeds_part2(data_arg)
    map_array = get_map_array(data_arg)
    humidity_to_location_map = map_array[-1]
    location_indices = get_min_destination_indices(humidity_to_location_map)
    map_array.reverse()
    
    for loc_ind in location_indices:
        i_map = humidity_to_location_map[loc_ind]
        dest = i_map['dest']
        i_range = i_map['range']
        print(f'checking locations starting at {dest} in range {i_range}')

        min_ind = 0
        max_ind = dest + i_range
        # for i in range(i_range):
        for i in range(1):
            iloc = dest + i
            seed = get_seed_from_location(map_array, iloc)
            if has_seed(seeds, seed):
                return seed



data_1 = fh.get_data('day_05.txt')
data_2 = fh.get_data('day_05.txt')
print(part_1(data_1))
print(part_2(data_2))