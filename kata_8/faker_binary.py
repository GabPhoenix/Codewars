def fake_bin(number_string):
    binary_string = ''
    for number in number_string:
        if int(number) < 5:
            binary_string += '0'
        else:
            binary_string += '1'
    return binary_string