from build_map import build_map
from build_map import is_valid_map

def encode(key, string) :
    encode_string = ""
    assert is_valid_map(key) == True
    i, a = 0, 0
    while i < len(string) :
        changed = 0
        for a in key:
            if string[i] == a :
                encode_string = encode_string + key[a]
                changed = 1
                break
        if changed == 0 :
            encode_string = encode_string + string[i]
        i += 1
    return encode_string

def decode(key, string) :
    decode_string = ""
    i, a = 0, 0
    while i < len(string) :
        changed = 0
        for a in key:
            if string[i] == key[a] :
                decode_string = decode_string + a
                changed = 1
                break
        if changed == 0 :
            decode_string = decode_string + string[i]
        i += 1
    return decode_string
