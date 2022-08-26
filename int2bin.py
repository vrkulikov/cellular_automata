def int2bin(code:int, length: int) -> list:
    """
    Convert integer `code` into binary representation of length `length`.
    Returns list of `int` `0` and `1`
    """
    out = [0]*length
    for i in range(length):
        out[i] = code % 2
        code //= 2
    return out
