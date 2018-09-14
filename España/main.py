letras = 171024
titulo = 12825
pagina = 14359

sigo = True

i = 1
while sigo:
    letPorPag = pagina - titulo - len(str(i)) * 2 - 1
    if letras <= letPorPag * i:
        sigo = False
        print("Con {} paginas alcanza".format(i))
    else:
        print("Con {} paginas  no alcanza".format(i))
        i+=1
