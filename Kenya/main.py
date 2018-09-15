medallas = ["abcdefgggghijlmmmnopppqqqqrrr","abcdefggghijlmmnopppqqqqrrr","abcdefggggghijlmmmnopppqqqqrrr","abcdefggggghijlmmmnopppqqqqrrr","abcdefggggghijlmmmnopppqqqqrrr"]
alfab = "abcdefghijklmnopqrstuvwxyz"


def enTodas(c):
    esta = True
    for m in medallas:
        if c not in m:
            esta = False
    return esta

def seRepite(c):
    repite = True
    for m in medallas:
        if m.count(c) <= 2:
            repite = False
    return repite

especiales = []
for c in alfab:
    if enTodas(c) and seRepite(c):
        especiales.append(c)

print(especiales)
print(len(especiales))
print(len(especiales)**2)
