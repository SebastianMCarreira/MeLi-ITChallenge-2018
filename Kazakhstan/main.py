with open("string.txt",'r') as file:
    s = file.read()
    minLex = s


longitud = 2976

def esMinLex(a,b):
    if ord(a[0]) < ord(b[0]):
        return True
    elif a[0] == b[0]:
        if len(a) == 1:
            return True
        else:
            return esMinLex(a[1:],b[1:])
    else:
        return False

def girar(a):
    return a[1:] + a[0]

sigo = True
for i in range(1000001):
    s = girar(s)
    if esMinLex(s,minLex):
        minLex = s
        print("\nEs min!")
        print(minLex[:20])
    print("\b\b\b\b\b\b\b",end="")
    print(str(i).rjust(7," "), end="")

print("\nMensaje:")
mitad = len(minLex)//2
print(minLex[mitad:mitad+longitud])
