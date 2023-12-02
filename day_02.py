import file_helper as fh

def get_games(line_arg):
    """return dict of game dicts """
    game_number = int(line_arg.strip().split(':')[0].strip().split(' ')[-1])
    sets = line_arg.strip().split(':')[1].split(';')

    return_sets = []
    for set in sets:
        cubes = set.strip().split(',')
        return_cubes = {'red':0,
                        'green':0,
                        'blue':0}
        for items in cubes: 
            bag = items.strip().split(' ')
            color = bag[1]
            value = int(bag[0])
            return_cubes[color] += value
        return_sets.append(return_cubes)
    
    return game_number, return_sets
def part_1(data_arg):
    """part 1 
    The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?"""
    game_sum = 0
    for line in data_arg:
        game_number, sets = get_games(line)
        game_possible = True
        for set in sets:
            if set['red'] > 12 or set['green'] > 13 or set['blue'] > 14:
                game_possible = False
                break
        
        if game_possible:
            game_sum+=game_number

    return game_sum

def part_2(data_arg):
    """part 2"""
    game_sum = 0
    for line in data_arg:
        game_number, sets = get_games(line)
        min_red =sets[0]['red'] 
        min_green=sets[0]['green']
        min_blue=sets[0]['blue']
        for set in sets:
            if set['red'] > min_red:
                min_red = set['red']
            if set['green'] > min_green:
                min_green = set['green']
            if set['blue'] > min_blue:
                min_blue = set['blue']
        game_sum += min_red * min_green * min_blue

    return game_sum



data_1 = fh.get_data('day_02.txt')
data_2 = fh.get_data('day_02.txt')
print(part_1(data_1))
print(part_2(data_2))