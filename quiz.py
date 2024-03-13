# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = float(input("Ingrese el valor de a : "))
b = float(input("Ingrese el valor de b : "))
c = float(input("Ingrese el valor de c : "))

# processing
if a + b > c:
    print("los numeros si forman un triangulo")
elif a + c > b:
    print("los numeros si forman un triangulo")
elif b + c > a:
    print("los numeros si forman un triangulo")
else:
    print("los numeros no forman un triangulo")

# output