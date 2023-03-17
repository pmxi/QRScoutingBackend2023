def parse_qr_string(qr_string: str) -> list:
    """Parse a QR string into a list of values"""
    data_l = qr_string.split('\t')
    bool_indices = [4, 5, 7, 14, 15, 16, 25, 30, 31, 32]
    for i in bool_indices:
        if data_l[i] == 'true':
            data_l[i] = 1
        else:
            data_l[i] = 0
    integer_indices = [1, 3, 8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 24, 27]
    for i in integer_indices:
        try:
            data_l[i] = int(data_l[i])
        except ValueError:
            raise ValueError(f'"{data_l[i]}" at index {i} is not an integer')
    return data_l
