import time 
procesando = "procesando.."
print("este proyecto es mi propia recopilacion con lo que llevo todo aprendido")
si = "si"
while "si" == si:
    time.sleep(0.5)
    print("este proyecto te dara unas opciones elige una de las que esten disponibles por el momento")
    time.sleep(0.5)
    print("-1.calculadora \n-2.tablas\n-3.numero mayor o menor\n-4.bug")
    opcion = input("digite su eleccion: ")
    if opcion == "calculadora":
        print("¿que tipo de claculadora desea elegir?")
        print("1.suma \n2.resta\n3.multiplicacion\n4.divicion\n5.potenciacion")
        opcion_calculadora = input("digite su opcion: ")
        print("en proceso...")
        n1_calculadora = int(input("digite su numero: "))
        n2_calculadora = int(input("digite su numero: "))
        print("este es su resultado de", opcion_calculadora, ":", end="")
        if opcion_calculadora == "suma":
            re_suma = n1_calculadora + n1_calculadora
            print(re_suma)
        if opcion_calculadora == "resta":
            re_resta = n1_calculadora - n2_calculadora
            print(re_resta)
        if opcion_calculadora == "multiplicacion":
            re_multiplicacion = n1_calculadora * n2_calculadora
            print(re_multiplicacion)
        if opcion_calculadora == "divicion":
            re_divicion = n1_calculadora / n2_calculadora
            print(re_divicion)
        if opcion_calculadora == "potenciacion":
            re_potenciacion = n1_calculadora ** n2_calculadora
            print(re_potenciacion)

    if  opcion == "tablas":
        print("esta parte del programa es una funcion para mirar clase de tablas ejemplo la tabla de multiplicacion entre otras tablas")
        print("tabla de multiplicacion\ntabla de suma\ntabla de resta\ntabla de divicion\ntabla de potenciacion")
        opcion_tabla = input("digite su opcion: ")
        n1_tabla = 1
        n2_tabla = int(input("digite el numero con el que quiere tratar:"))
      
        if opcion_tabla == "tabla de multiplicacion":
            for n1_tabla in range(n2_tabla):
                re_tabla_multiplicacion = n1_tabla * n2_tabla
                print(n1_tabla, "x", n2_tabla, "=", re_tabla_multiplicacion)
        if opcion_tabla == "tabla de divicion":
            for n1_tabla in range(n2_tabla):
                re_tabla_divicion = n1_tabla / n2_tabla
                print(n1_tabla, "/", n2_tabla, "= ", re_tabla_divicion)
        if opcion_tabla == "tabla de resta":
            for n1_tabla in range(n2_tabla):
                re_tabla_resta = n1_tabla - n2_tabla
                print(n1_tabla, "-", n2_tabla, "= ", re_tabla_resta)
        if opcion_tabla == "tabla de suma":
            for n1_tabla in range(n2_tabla):
                re_tabla_suma = n1_tabla + n2_tabla
                print(n1_tabla, "+", n2_tabla, "= ", re_tabla_suma)
        if opcion_tabla == "tabla de potenciacion":
            for n1_tabla in range(n2_tabla):
                re_tabla_potenciacion = n1_tabla ** n2_tabla
                print(n1_tabla, "**", n2_tabla, "= ", re_tabla_potenciacion)
    if opcion == "numero mayor o menor":
        print("esta parte del programa te dira cual es el numero mayor o menor dependiendo de tu opcion \n-1.mayor\n-2.menor")
        time.sleep(5)
        print(procesando)
        opcion_mayor_menor = input("digite aca su opcion: ")
        n1_mayor_o_menor = int(input("digite un numero: "))
        n2_mayor_o_menor = int(input("digite un numero: "))
        n3_mayor_o_menor = int(input("digite un numero: "))
        print(procesando)
        time.sleep(2)
        print("este es su numero", opcion_mayor_menor, ":", end="")
        if opcion_mayor_menor == "mayor":
            re_mayor = max(n1_mayor_o_menor, n2_mayor_o_menor, n3_mayor_o_menor)
            print(re_mayor)
        if opcion_mayor_menor == "menor":
            re_menor = min(n1_mayor_o_menor, n2_mayor_o_menor, n3_mayor_o_menor)
            print(re_menor)
        print(procesando)
        time.sleep(5)
        numeros_elegidos_de_cual_de_los_tres_es_mayor_o_menor = [n1_mayor_o_menor, n2_mayor_o_menor, n3_mayor_o_menor]
        print(len(numeros_elegidos_de_cual_de_los_tres_es_mayor_o_menor))
        print("numeros elegidos: ", numeros_elegidos_de_cual_de_los_tres_es_mayor_o_menor)
    if opcion == "bug":
        print("esta funcion te permitira colapsar sitios qeb que se puedan ejecutar por ide online de python o subir los recursos de alguna pc")
        print(procesando)
        time.sleep(0.5)
        veces = int(input("digite las veces que se desea repetir: "))
        for veces in range(veces):
            bug_pc = 9**9**9
            print(bug_pc)
            print(procesando)
    
    print("deseas otra vez utilizar mi programa", end="")
    si = input("(si/no)")
else:
    print("gracias por utilizar el programa")
