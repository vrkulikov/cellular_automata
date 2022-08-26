from int2bin import int2bin
from wolf2zheg import wolf2zheg
from zhegalkin import zhegalkin

if __name__=='__main__':
    linear_rules = []
    for i in range(255):
        poly = wolf2zheg(i)
        cntr = 0
        for j in range(8):
            for k in range(8):
                x = int2bin(j,3)
                y = int2bin(k,3)
                xy = int2bin(j^k,3)
                fx = zhegalkin(poly, x)
                fy = zhegalkin(poly, y)
                fxy = zhegalkin(poly,xy)
                if fxy == fx^fy:
                    cntr += 1
        if cntr == 64:
            linear_rules.append(poly)

    print(linear_rules)
