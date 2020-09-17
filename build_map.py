def build_map(infile) :
    "Builds a decryption map"
    key = {}
    infile = open(infile, 'r')
    for line in infile :
        if line[0] == '#':
            continue
        line = line.strip()
        if len(line) == 0 :
            continue
        line = line.split()
        key[line[0]] = line[1]
    print(key)
    return key

def is_valid_map(key):
    "Checks the validity of the input file"
    

if __name__ == "__main__" :
    infile = "test1.txt"
    build_map(infile)