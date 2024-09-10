
import os,time

os.system("cls")


armas=[]
mapas=[]
skin=[]


while True:
    print("|WARZONE|")
    print("1. weapons")
    print("2. map")
    print("3. skin") 
    print("4. inventario")
    print("5. exit")
    while True:
        try:
            opc = int(input("elija una opcion: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("error como no sabi apretar un numero wn tonto")
        except:
            print("error eri weta")
    if opc==1:
        os.system("cls")
        print("agreagar armamento")
        principal=input("ingrese arma: ")
        secundaria=input("ingrese arma secundaria: ")
        armas.append(principal)
        armas.append(secundaria)
    elif opc==2:
        os.system("cls")
        print("inserte mapa")
        maps=input("nombre de mapa: ")
        mapas.append(maps)
    elif opc==3:
        os.system("cls")
        print("eliga su skin")
        skn=input("nombre de skin: ")
        skin.append(skn)
    elif opc==4:
        os.system("cls")
        print("esta es tu eleccion")  
        print(armas)
        print(mapas)
        print(skin)  
    else:
        print("chao ctm!!")
        break
