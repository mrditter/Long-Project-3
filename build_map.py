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
        assert len(line) == 2
        assert len(line[0]) == 1 and \
            len(line[1]) == 1
        assert line[0] not in key.keys()
        key[line[0]] = line[1]
    return key

def is_valid_map(key):
    "Checks the validity of the input file"
    for x, y in key.items() :
        if type(x) != str:
            return False
        elif type(y) != str:
            return False
        elif len(x) != 1:
            return False
        elif len(y) != 1:
            return False
        elif x in " \t\n" :
            return False
        elif y in " \t\n" :
            return False
    dup_to = 0
    for x in key.values():
        dup_to = 0
        for y in key.values():
            if x == y:
                dup_to += 1
        if dup_to > 1:
            return False
    if len(key.items()) != len(key.keys()) :
        return False
    return True

if __name__ == "__main__" :
    infile = "test1.txt"
    build_map(infile)