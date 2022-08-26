def zhegalkin(coefs:list[int], variables: list[int]) -> int:
    """
    Calculate Zhegalkin polynome with coeffitients `coefs` on `variables`
    """
    if len(coefs) !=8:
        raise ValueError('Len of coeffitients must be equal 8')
    if len(variables) !=3:
        raise ValueError('Len of variables must be equal 3')
    return (coefs[0] + coefs[1]*variables[0] + coefs[2]*variables[1] + coefs[3]*variables[0]*variables[1] + 
        coefs[4]*variables[2] + coefs[5]*variables[0]*variables[2] + coefs[6]*variables[1]*variables[2] + 
        coefs[7]*variables[0]*variables[1]*variables[2])

