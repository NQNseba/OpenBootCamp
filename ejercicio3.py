#en JS

public class Persona {
    private int edad;
    private String nombre;
    private String telefono;
    
    // Constructor
    public Persona() {
    }
    
    // Getter y Setter para la propiedad edad
    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    // Getter y Setter para la propiedad nombre
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    // Getter y Setter para la propiedad telefono
    public String getTelefono() {
        return telefono;
    }
    
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}

public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();
        
        // Utilizar los setters para asignar valores a las propiedades
        persona.setEdad(25);
        persona.setNombre("Juan");
        persona.setTelefono("123456789");
        
        // Utilizar los getters para mostrar las propiedades por consola
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Teléfono: " + persona.getTelefono());
    }
}



# en Python

class Persona:
    def __init__(self):
        self._edad = 0
        self._nombre = ""
        self._telefono = ""
    
    # Getter y Setter para la propiedad edad
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    # Getter y Setter para la propiedad nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    # Getter y Setter para la propiedad telefono
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono


# Crear un objeto persona en el main
persona = Persona()

# Utilizar los setters para asignar valores a las propiedades
persona.edad = 25
persona.nombre = "Juan"
persona.telefono = "123456789"

# Utilizar los getters para mostrar las propiedades por consola
print("Edad:", persona.edad)
print("Nombre:", persona.nombre)
print("Teléfono:", persona.telefono)
