import time

with open("secreto.txt","rb") as file:
    cont_i = file.read()

    # for i in range(0,256):
    #     des = []
    #     for n in cont_i:
    #         des.append(n^i)
    #     for d in des:
    #         print(chr(d), end="")
    #     print("\n" + str(i))
    #     time.sleep(2)

    des = []
    for n in cont_i:
        des.append(n^137)
    with open("decifrado.pdf", "wb") as pdf:
        for d in des:    
            pdf.write(bytes([d]))
