'''Gen Binary Matrix
When ran as a script this takes two args, the path to the json
and the desired out put path for the matrix csv.

Args
====
* Path to json
* Out path

'''

import pandas as pd 
import json 

def get_dict(path):
    with open(path, "r") as infile: 
        fun_dict = json.load(infile)
    return fun_dict

def get_names (dict):
    return list(dict.keys())

def gen_matrix (names, dict):
    matrix = pd.DataFrame(columns = names)
    for n in fun_names:
        bool_row = [0] * len(fun_names)
        adjacent = dict[n]
        for a in adjacent:
            index = names.index(a)
            bool_row[index] = 1
        matrix.loc[n] = bool_row
    return matrix 

if __name__ == "__main__":
    import sys 
    
    if len(sys.argv) != 3 or sys.argv[1] in ["h","-h","--help","help"]: 
        print(__doc__)
    
    fun_dict = get_dict(sys.argv[1])
    fun_names = get_names(fun_dict)
    matrix = gen_matrix(fun_names, fun_dict)
    
    matrix.to_csv(sys.argv[2])
   



