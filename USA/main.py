usuarios = [
    "edbbaacdcaacacbababaabadeeeaaddecaaeceeecbdcdaeacaccccaddeaaddecdcdcdccadcacceeecdcbceecebde",
    "dadbccabcdeccbcdbedaaabbdccdddcbdbebdeca",
    "aeaeddabaacbdcecacccbbacededbecbaccdccccebacdbbaedecbaeadaebedeccbaedcdcdabdcedbddabaeeaadcbdd",
    "abbdaedeeeedeaeeabcabbadbebedcedaadabbbddbbebdabecdcbdcc",
    "cddddabbaeaccaabedebbaaeabccecddcdbaaecbeeadeaeadabeddadaccbcdeebcacceaddabccdccaaddddd",
    "bbeeabcadeecbcadae",
    "dcbaceaadbdeceaaccaaeecadeedabeaecadbbebeecbdcddaadbbdbeecaaebcadddbb",
    "adcdeaccccaaeabaaeaaabeaecdbadbabdecadeeacebcdcceceebeecdeaeebbbccaeacedeaeddbd",
    "ed",
    "ebeecaddbbceecebdeadedecddddecddecebeabbbecabdbeddeceabc"
    ]

def semejanzas(s,x):
    coincidencias = 0
    for i in range(len(x)+1):
        sub = x[:i]
        if s.startswith(sub):
            coincidencias = len(sub)
    
    return coincidencias


def dividrSufijos(s):
    inicial = s
    sem = []
    for i in range(len(inicial)):
        sub = inicial[i:]
        sem.append(semejanzas(inicial,sub))
    return sum(sem)


sem_usuarios = []
for u in usuarios:
    print(u)
    sem_usuarios.append(dividrSufijos(u))

for s in sem_usuarios:
    print(s, end=" ")