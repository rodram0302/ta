num=int(input("Ingrese un número entero: "));
if num > 0:
    mensaje="Es un número positivo";
elif num == 0:
    mensaje = "Es un número neutro";
else:
    mensaje="Es un número negativo";
print(mensaje);
