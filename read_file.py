def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data
