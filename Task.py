from itertools import product


def inverter(X, Y, Z):
    G = not ((X and Y) or (Y and Z) or (X and Z))
    F = not ((X and G) or (Y and G) or (Z and G) or (X and Y and Z))
    notX = G and (Y or Z or F) or (Y and Z and F)
    notY = G and (X or Z or F) or (X and Z and F)
    notZ = G and (X or Y or F) or (X and Y and F)
    return (notX, notY, notZ)


for combo in product([False, True], repeat=3):
    print(*combo, '=>', *inverter(*combo))

