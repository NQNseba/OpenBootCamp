class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono


class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito


class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario


# Crear objeto de la clase Cliente
cliente = Cliente(30, "Juan", "123456789", 5000)

# Mostrar propiedades del cliente
print("Cliente:")
print("Edad:", cliente.edad)
print("Nombre:", cliente.nombre)
print("Teléfono:", cliente.telefono)
print("Crédito:", cliente.credito)

# Crear objeto de la clase Trabajador
trabajador = Trabajador(35, "María", "987654321", 3000)

# Mostrar propiedades del trabajador
print("\nTrabajador:")
print("Edad:", trabajador.edad)
print("Nombre:", trabajador.nombre)
print("Teléfono:", trabajador.telefono)
print("Salario:", trabajador.salario)




#en js



class Persona {
  constructor(edad, nombre, telefono) {
    this.edad = edad;
    this.nombre = nombre;
    this.telefono = telefono;
  }
}

class Cliente extends Persona {
  constructor(edad, nombre, telefono, credito) {
    super(edad, nombre, telefono);
    this.credito = credito;
  }
}

class Trabajador extends Persona {
  constructor(edad, nombre, telefono, salario) {
    super(edad, nombre, telefono);
    this.salario = salario;
  }
}

// Crear objeto de la clase Cliente
const cliente = new Cliente(30, "Juan", "123456789", 5000);

// Mostrar propiedades del cliente
console.log("Cliente:");
console.log("Edad:", cliente.edad);
console.log("Nombre:", cliente.nombre);
console.log("Teléfono:", cliente.telefono);
console.log("Crédito:", cliente.credito);

// Crear objeto de la clase Trabajador
const trabajador = new Trabajador(35, "María", "987654321", 3000);

// Mostrar propiedades del trabajador
console.log("\nTrabajador:");
console.log("Edad:", trabajador.edad);
console.log("Nombre:", trabajador.nombre);
console.log("Teléfono:", trabajador.telefono);
console.log("Salario:", trabajador.salario);




#en Java



class Persona {
    private int edad;
    private String nombre;
    private String telefono;

    public Persona(int edad, String nombre, String telefono) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public int getEdad() {
        return edad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTelefono() {
        return telefono;
    }
}

class Cliente extends Persona {
    private int credito;

    public Cliente(int edad, String nombre, String telefono, int credito) {
        super(edad, nombre, telefono);
        this.credito = credito;
    }

    public int getCredito() {
        return credito;
    }
}

class Trabajador extends Persona {
    private int salario;

    public Trabajador(int edad, String nombre, String telefono, int salario) {
        super(edad, nombre, telefono);
        this.salario = salario;
    }

    public int getSalario() {
        return salario;
    }
}

public class Main {
    public static void main(String[] args) {
        // Crear objeto de la clase Cliente
        Cliente cliente = new Cliente(30, "Juan", "123456789", 5000);

        // Mostrar propiedades del cliente
        System.out.println("Cliente:");
        System.out.println("Edad: " + cliente.getEdad());
        System.out.println("Nombre: " + cliente.getNombre());
        System.out.println("Teléfono: " + cliente.getTelefono());
        System.out.println("Crédito: " + cliente.getCredito());

        // Crear objeto de la clase Trabajador
        Trabajador trabajador = new Trabajador(35, "María", "987654321", 3000);

        // Mostrar propiedades del trabajador
        System.out.println("\nTrabajador:");
        System.out.println("Edad: " + trabajador.getEdad());
        System.out.println("Nombre: " + trabajador.getNombre());
        System.out.println("Teléfono: " + trabajador.getTelefono());
        System.out.println("Salario: " + trabajador.getSalario());
    }
}




