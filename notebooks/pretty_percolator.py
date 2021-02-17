import numpy as np

def pretty_percolator(your_arr):

    assert your_arr.shape[0]==your_arr.shape[1], "Your array must be square"

    your_arr = np.array2string(your_arr, separator = " ", max_line_width = your_arr.shape[0]*10)
    your_arr = " " + your_arr[1:-1] + " "
    your_arr = your_arr.replace("'", "").replace("]", "|").replace("[", "|")

    print(your_arr)
