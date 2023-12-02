import file_helper as fh


def part_1(data_arg):
    """part 1"""
    calibration_value_sum = 0
    for line in data_arg:
        calibration_value = 0
        for ind_left in range(len(line)):
            if line[ind_left].isdigit():
                calibration_value = 10*int(line[ind_left])
                break


        for ind_left in range(len(line)):
            ind_right = -1 * (ind_left+1)
            if line[ind_right].isdigit():
                calibration_value += int(line[ind_right])
                break
        # print(f'calibration value: {calibration_value}')
        calibration_value_sum += calibration_value
    
    return calibration_value_sum


num_str = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

num_dig = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

import re
def part_2(data_arg):
    """part 2"""

    def get_find_indices(string_arg, line_arg):
        """get indices of string_arg in line_arg"""
        if string_arg in line_arg:
            return [m.start() for m in re.finditer(string_arg, line_arg)]
        else:
            return None



    calibration_value_sum = 0
    for line in data_arg:
        calibration_value = 0
        # print(line)
        max_ind = -1
        min_ind = len(line)+1
        min_val = 0
        max_val = 0
        for i, num in enumerate(num_str):
            indices = get_find_indices(num, line)
            if indices is None:
                continue
            if min(indices) < min_ind:
                min_ind = min(indices)
                min_val = i+1
            if max(indices) > max_ind:
                max_ind = max(indices)
                max_val = i+1
        for i, num in enumerate(num_dig):
            indices = get_find_indices(num, line)
            if indices is None:
                continue
            if min(indices) < min_ind:
                min_ind = min(indices)
                min_val = i+1
            if max(indices) > max_ind:
                max_ind = max(indices)
                max_val = i+1


        calibration_value = min_val * 10 + max_val
        # print(f'calibration value: {calibration_value}')
        calibration_value_sum += calibration_value
    
    return calibration_value_sum


data_1 = fh.get_data('day_01.txt')
data_2 = fh.get_data("day_01.2.txt")
print(part_1(data_1))
print(part_2(data_2))