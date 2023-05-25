def sumar_tres_numeros(num1, num2, num3):
    suma = num1 + num2 + num3
    return suma

def main():
    resultado = sumar_tres_numeros(2, 4, 6)
    print("El resultado de la suma es:", resultado)

# Llamar a la función main
main()

class Coche:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas

    def agregar_puerta(self):
        self.num_puertas += 1

    def obtener_num_puertas(self):
        return self.num_puertas

# Crear un objeto miCoche de la clase Coche
miCoche = Coche(3)
miCoche.agregar_puerta()

# Mostrar el número de puertas del objeto miCoche
print("El coche tiene", miCoche.obtener_num_puertas(), "puertas.")
