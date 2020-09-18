def unzip(compressed):
    "'Unzips' the compressed stream"
    final_string = ""
    current_index = 0
    string_index = 0
    for i in compressed :
        assert (type(i) == str) or (type(i) == tuple)
        if type(i) == str :
            assert len(i) == 1
        if type(i) == tuple:
            assert type(i[0]) == int
            assert type(i[1]) == int
            assert i[0] > 0
        if type(i) == str :
            final_string = final_string + i
            string_index += 1
        elif type(i) == tuple :
            num_times = 0
            mini_index = string_index - i[0]
            assert mini_index >= 0
            while num_times < i[1] :
                final_string = final_string + final_string[mini_index]
                num_times += 1
                mini_index += 1
                string_index += 1
        current_index += 1
    return final_string
