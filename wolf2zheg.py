from int2bin import int2bin

def wolf2zheg(wolfram_code: int) -> list[int]:
    """
    Converts integer `wolfram_code` from 0 to 255 to array of length 8 of coeffitients of Zhegalkin`s polynome
    """
    zhegalkin_polynome = [0]*8
    wolfram_binary = int2bin(wolfram_code,8)
    for i in range(8):
        zhegalkin_polynome[i] = wolfram_binary[0]
        for j in range(1,8):
            wolfram_binary[j-1] = (wolfram_binary[j-1]+wolfram_binary[j]) % 2
    return zhegalkin_polynome

