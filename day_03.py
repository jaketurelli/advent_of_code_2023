import file_helper as fh

def determine_number(row_col_point, data_arg):
    """determines number at row_col_point in data_arg"""
    row = row_col_point[0]
    col = row_col_point[1]
    line = data_arg[row]
    min = col
    max = col
    abs_max = len(line)-1
    while(True):
        if min == 0:
            break
        if line[min-1].isdigit():
            min -= 1
        else:
            break
    while(True):
        if max == abs_max:
            break
        if line[max+1].isdigit():
            max+=1
        else:
            break
    return int(line[min:max+1])

def find_part_numbers(row,col,data_arg):
    """find all part numbers adjacent to row,col location in data_arg"""
    part_numbers = []
    points_of_interest_lat = [
                            [row,col+1],
                            [row,col-1]]

    points_of_interest_below = [
                          [row+1,col],
                          [row+1,col+1],
                          [row+1,col-1]]
    
    points_of_interest_above = [
                          [row-1,col],
                          [row-1,col+1],
                          [row-1,col-1]]
    for point in points_of_interest_lat:
        if(data_arg[point[0]][point[1]].isdigit()):
            part_numbers.append(determine_number(point,data_arg))
    
    part_numbers_above = []
    for point in points_of_interest_above:
        if(data_arg[point[0]][point[1]].isdigit()):
            part_numbers_above.append(determine_number(point,data_arg))
    if data_arg[row-1][col].isdigit():
        part_numbers = part_numbers + list(set(part_numbers_above))
    else:
        part_numbers = part_numbers + part_numbers_above

    part_numbers_below = []
    for point in points_of_interest_below:
        if(data_arg[point[0]][point[1]].isdigit()):
            part_numbers_below.append(determine_number(point,data_arg))
    if data_arg[row+1][col].isdigit():
        part_numbers = part_numbers + list(set(part_numbers_below))
    else:
        part_numbers = part_numbers + part_numbers_below
       
    return part_numbers

def part_1(data_arg):
    """part 1"""
    part_numbers = []
    for row, line in enumerate(data_arg):
        for col, item in enumerate(line):
            if item == '.' or item.isdigit():
                continue
            new_part_numbers = find_part_numbers(row, col, data_arg)
            part_numbers = part_numbers + new_part_numbers
    
    return sum(part_numbers)



def part_2(data_arg):
    """part 2"""
    gear_ratios = 0
    for row, line in enumerate(data_arg):
        for col, item in enumerate(line):
            if item != '*':
                continue
            new_gear_ratios = find_part_numbers(row, col, data_arg)
            if len(new_gear_ratios) == 2:
                gear_ratios += new_gear_ratios[0]*new_gear_ratios[1]
    
    return gear_ratios



data_1 = fh.get_data('day_03.txt')
data_2 = fh.get_data('day_03.txt')
print(part_1(data_1))
print(part_2(data_2))