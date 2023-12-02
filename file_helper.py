def get_data(filepath):
    """ returns column array of strings with every line of file"""
    data_array = []
    with open(filepath, 'r') as file:
        for line in file:
            data_array.append(line.replace('\n', ''))
    
    return data_array