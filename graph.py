import pandas
import sys
import subprocess as sp

'''
Gives back dimensions of current terminal window
'''
def generate_grid_dimensions():
    columns = sp.check_output(["tput", "columns"])
    rows = sp.check_output(["tput", "lines"])
    rows = int(rows)
    columns = int(columns)
    return (rows,columns)

'''
prints a blank grid with "row" rows and "columns" columns
'''
def print_grid(row, columns, max_size=True):
    counter = 0
    cols = ""

    while(counter < rows-1):
        print("|")
        counter += 1

    counter = 0
    while(counter < columns):
        cols += "_"
        counter += 1

    cols = cols[1:]
    print("|" + cols)

rows,columns = generate_grid_dimensions()
print_grid(rows, columns)
