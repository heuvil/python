def run():
    year = int(input("ano: "))
    resto_4 = year % 4
    resto_100 = year % 100
    resto_400 = year % 400
    # print(resto_4)
    # print(resto_100)
    # print(resto_400)
    if resto_4 == 0:
        if resto_100 == 0:
            if resto_400 == 0:
                print("ano bissexto")
            else:
                print("ano nao bissexto")
        else:
            print("ano bissexto")
    else:
        print("não bissexto")
