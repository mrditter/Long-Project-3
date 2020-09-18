def unzip(compressed):
    "'Unzips' the compressed stream"
    final_string = ""
    for i in compressed :
        assert (type(i) == str) or (type(i) == tuple)
        if type(i) == str :
            assert len(i) == 1
        if type(i) == tuple:
            assert type(i[0]) == int
            assert type(i[1]) == int
            assert type(i[0]) > 0
        if type(i) == str :
            final_string = final_string + i
            continue
        elif type(i) == tuple :
            current_index, num_times = 0, 1
            while id(compressed[current_index]) != id(i):
                current_index += 1
            end_index = current_index
            current_index = current_index - i[0]
            assert current_index >= 0
            while num_times <= i[1] :
                final_string = final_string + final_string[current_index]
                if current_index + 1 != end_index :
                    current_index += 1
                num_times += 1
    return final_string
    