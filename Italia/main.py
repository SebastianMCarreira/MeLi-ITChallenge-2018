with open("estudiantes.txt","r") as file:
    est = file.read()
    p = est.count("p")
    c = est.count("c")
    m = est.count("m")
    b = est.count("b")
    z = est.count("z")
    materias = [p,c,m,b,z]
    print(min(materias))