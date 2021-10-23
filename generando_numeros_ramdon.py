import random

int_random = random.randint(0, 20)
int_rango = random.randrange(0, 50, 2)
real_ramdom = random.random()
uniforme_ramdom = random.uniform(1, 10)
cadena_dentro_de_la_cadena = random.choice(
    "se leccinara un caracter de esta cadena aleatoriamente")

print(f"el numero entero aleatorio {int_random} el numero entero en un rango {int_rango} el numero real ramdom {real_ramdom} el numero real en un rango {uniforme_ramdom}, el caracter alaeatorio de lacadena que se le paso {cadena_dentro_de_la_cadena}")
