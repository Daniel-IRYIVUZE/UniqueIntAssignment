def is_integer_within_range(string):
    try:
        num = int(string)
        return -1023 <= num <= 1023
    except ValueError:
        return False

def filter_integers(data):
    integers = set()  # set() to store unique integers
    for item in data:
        if is_integer_within_range(item):
            integers.add(int(item))
    return list(integers)
