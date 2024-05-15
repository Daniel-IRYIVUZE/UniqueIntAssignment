from read_file import read_file
from filter_integers import filter_integers
from quicksort import quicksort

def main(file_name):
    data = read_file(file_name)
    integers = filter_integers(data)
    sorted_integers = quicksort(integers)
    print("Sorted Integers:", sorted_integers)

if __name__ == "__main__":
    file_name = "sample_input_for_students/small_sample_input_01.txt"  # Change this to your file name
    main(file_name)
