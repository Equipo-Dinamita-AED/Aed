from time import sleep
from colorama import Cursor, init, Fore
init()

print(Fore.GREEN + "Programa para Generación de Estadísticas de COVID-19")
print("=" * 80)
#Validación de mail...

mail = str(input(Fore.LIGHTBLUE_EX + "Ingrese su mail(en formato 'nombre@dominio'): "))
intentos = 0

if mail[0] == "." or mail[-1] == ".":
    while intentos < 2:
       print("Correo INVÁLIDO\nIngrese el correo nuevamente y respetanto el formato")
       mail = input("Ingrese su mail(en formato 'nombre@dominio'): ")
       intentos += 1
       if intentos == 2:
            print(Fore.RED +"Llegó al límite de intentos permitidos\n\tFinalizando Programa...")
            exit()
else:
    print(Fore.GREEN + "Correo VÁLIDO\nContinúe...")
print("\n")

#Generacion de datos aleatorios...
pacientes = int(input(Fore.LIGHTCYAN_EX + "Cantidad de casos sospechosos es: "))
resultado = (1, 2)
region = ("Capital", "Gran Córdoba", "Norte", "Sur")
contac_conf = ("Si", "No")
ps = ("Si", "No")
viajo = ("Si", "No")
autoctono = 0
#Banderas...
casos_conf = 0
ps_contador = 0
casos_capital = 0
casos_gc = 0
casos_N = 0
casos_S = 0
casos_ext = 0
casos_cc = 0
mayores = []
suma_mayores = 0
prom_mayores = 0
edades = []
suma_edades = 0

for i in range(pacientes):
    import random
    edad = random.randint(1, 100)
    r_test = random.choice(resultado)
    if r_test == 1:
        r_test = "Positivo"
        casos_conf += 1
        edades.append(edad)
    else:
        r_test = "Negativo"

    if edad >= 60 and r_test == "Negativo":
        mayores.append(edad)
    x = random.choice(region)
    if r_test == "Positivo" and x == "Capital":
        casos_capital += 1
    elif r_test == "Positivo" and x == "Gran Córdoba":
        casos_gc += 1
    elif r_test == "Positivo" and x == "Norte":
        casos_N += 1
    elif r_test == "Positivo" and x == "Sur":
        casos_S += 1
    ce = random.choice(contac_conf)
    if ce == "Si" and r_test == "Positivo":
        casos_cc += 1
    p = random.choice(ps)
    if edad < 23 or edad > 70:
        p = "No"
    else:
        p = "Si"
        if p == "Si":
            ps_contador += 1
    v = random.choice(viajo)
    if r_test == "Positivo" and ce == "No" and p == "No" and v == "No":
        autoctono = "Si"
    else:
        autoctono = "No"
        if v == "Si" and r_test == "Positivo":
            casos_ext += 1


    print("Resultado del test:", r_test)
    print("Edad:", edad)
    print("Región donde reside: ", x)
    print("Tuvo contacto con casos confirmados: ", ce)
    print("¿Es personal de salud? ", p)
    print("¿Viajó al exterior? ", v)
    print("¿Es caso autóctono? ", autoctono)
    print("=" * 30)

for e in mayores:
    if mayores != -1 :
        suma_mayores += e
        prom_mayores = suma_mayores / len(mayores)

for z in edades:
    suma_edades += z

print("\n")
#Informacion sobre los casos...

print(Fore.BLUE + "Casos confirmados: ", casos_conf)
porc_conf = casos_conf * pacientes / 100
print(Fore.BLUE + "Porcentaje de casos confirmados es: ",porc_conf, "%")
print("." * 30)

print("El promedio de edades entre los pacientes de riesgo es: ", prom_mayores)
print("." * 30)

porc_ps = ps_contador * pacientes / 100
print(Fore.CYAN + "Cantidad de personal de salud: ", ps_contador)
print(Fore.CYAN + "Porcentaje de personal de salud sobre total de casos: ", porc_ps)
print("." * 30)

prom_edades = suma_edades / casos_conf
print("El promedio de edades entre pacientes es: ", prom_edades)
print("." * 30)

print(Fore.LIGHTGREEN_EX + "Cantidad de casos en Capital: ", casos_capital)
print(Fore.LIGHTGREEN_EX + "Cantidad de casos en Gran Córdoba: ", casos_gc)
print(Fore.LIGHTGREEN_EX + "Cantidad de casos en Norte: ", casos_N)
print(Fore.LIGHTGREEN_EX + "Cantidad de casos en Sur: ", casos_S)
print("." * 30)

print(Fore.LIGHTYELLOW_EX + "Casos confirmados por viajes al exterior: ", casos_ext)
print("." * 30)

print(Fore.WHITE + "Casos sospechoso en contacto con casos confirmados: ", casos_cc)
print("." * 30)

if casos_capital == 0:
    print(Fore.MAGENTA + "Región Capital sin casos confirmados")
    print("." * 30)
elif casos_gc == 0:
    print(Fore.MAGENTA + "Región Gran Córdoba sin casos confirmados")
    print("." * 30)
elif casos_N == 0:
    print(Fore.MAGENTA + "Región Norte sin casos confirmados")
    print("." * 30)
elif casos_S == 0:
    print(Fore.MAGENTA + "Región Sur sin casos confirmados")
    print("." * 30)
