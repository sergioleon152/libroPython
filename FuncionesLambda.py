'''def area_triangulo(base, altura):
    return (base*altura)/2


tringulo1 = area_triangulo(5, 7)
tringulo2 = area_triangulo(9, 6)

print(
    f"area del primer triangulo {tringulo1} area del segundo triangulo {tringulo2}")
'''
# ahora con funciones lambda


def area_triangulo(base, altura): return (base*altura)/2


print(area_triangulo(7, 5))
print(area_triangulo(9, 7))
# o podemos guardarlos en aribles
triangulo1 = area_triangulo(2, 5)
triangulo2 = area_triangulo(4, 8)
print(triangulo2, triangulo1)
