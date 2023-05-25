#en javascritp 


#Ejercicio con estructuras de control

# If
let numeroIf = -5;

if (numeroIf > 0) {
  console.log("El número es positivo");
} else if (numeroIf < 0) {
  console.log("El número es negativo");
} else {
  console.log("El número es 0");
}

# While
let numeroWhile = 0;

while (numeroWhile < 3) {
  numeroWhile++;
  console.log(numeroWhile);
}

# Do While
let numeroDoWhile = 0;

do {
  numeroDoWhile++;
  console.log(numeroDoWhile);
} while (numeroDoWhile < 3);

// For
for (let numeroFor = 0; numeroFor <= 3; numeroFor++) {
  console.log(numeroFor);
}

 #Switch
let estacion = "verano";

switch (estacion) {
  case "primavera":
    console.log("Estamos en primavera.");
    break;
  case "verano":
    console.log("Estamos en verano.");
    break;
  case "otoño":
    console.log("Estamos en otoño.");
    break;
  case "invierno":
    console.log("Estamos en invierno.");
    break;
  default:
    console.log("El valor de la variable no corresponde a una estación.");
}

# en Python

# Ejercicio con estructuras de control

# If
numeroIf = -5

if numeroIf > 0:
    print("El número es positivo")
elif numeroIf < 0:
    print("El número es negativo")
else:
    print("El número es 0")

# While
numeroWhile = 0

while numeroWhile < 3:
    numeroWhile += 1
    print(numeroWhile)

# Do While (emulado con un ciclo while)
numeroDoWhile = 0

while True:
    numeroDoWhile += 1
    print(numeroDoWhile)
    if numeroDoWhile >= 3:
        break

# For
for numeroFor in range(4):
    print(numeroFor)

# Switch (emulado con un diccionario)
estacion = "verano"

estaciones = {
    "primavera": "Estamos en primavera.",
    "verano": "Estamos en verano.",
    "otoño": "Estamos en otoño.",
    "invierno": "Estamos en invierno."
}

mensaje = estaciones.get(estacion, "El valor de la variable no corresponde a una estación.")
print(mensaje)


