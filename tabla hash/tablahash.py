class Persona:
    def __init__(self, id nombre, apellido, telefono):
        self.id = id  
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    def __str__(self):
        return f"DNI: {self.id}, Nombre: {self.nombre} {self.apellido}, Tel: {self.telefono}"


class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)] 
    def calcular_hash(self, dni):
        dni_str = str(dni)
        suma = sum(ord(c) for c in dni_str)
        return suma % self.tamaño  # Usamos módulo para asegurar que esté en el rango
    
    def insertar(self, persona):
        """
        Inserta una persona en la tabla hash
        :param persona: Objeto Persona a insertar
        """
        indice = self.calcular_hash(persona.dni)
        # Verificamos si el DNI ya existe para actualizar
        for i, (dni_existente, _) in enumerate(self.tabla[indice]):
            if dni_existente == persona.dni:
                self.tabla[indice][i] = (persona.dni, persona)
                return
        # Si no existe, lo agregamos
        self.tabla[indice].append((persona.dni, persona))
    
    def buscar(self, dni):
        """
        Busca una persona por su DNI
        :param dni: DNI a buscar
        :return: Objeto Persona si se encuentra, None si no
        """
        indice = self.calcular_hash(dni)
        for dni_existente, persona in self.tabla[indice]:
            if dni_existente == dni:
                return persona
        return None
    
    def eliminar(self, dni):
        """
        Elimina una persona de la tabla hash por su DNI
        :param dni: DNI de la persona a eliminar
        :return: True si se eliminó, False si no se encontró
        """
        indice = self.calcular_hash(dni)
        for i, (dni_existente, _) in enumerate(self.tabla[indice]):
            if dni_existente == dni:
                del self.tabla[indice][i]
                return True
        return False
    
    def listar(self):
        """
        Lista todas las personas en la tabla hash
        :return: Lista de todas las personas
        """
        lista_personas = []
        for cubeta in self.tabla:
            for _, persona in cubeta:
                lista_personas.append(persona)
        return lista_personas
    
    def mostrar_tabla(self):
        """
        Muestra la estructura completa de la tabla hash
        (Para fines de visualización/debugging)
        """
        for i, cubeta in enumerate(self.tabla):
            print(f"Cubeta {i}:")
            for dni, persona in cubeta:
                print(f"  {persona}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear tabla hash con tamaño 7
    tabla = TablaHash(tamaño=7)
    
    # Crear algunas personas
    p1 = Persona("12345678", "Juan", "Pérez", "555-1234")
    p2 = Persona("87654321", "María", "Gómez", "555-5678")
    p3 = Persona("11223344", "Carlos", "López", "555-9012")
    p4 = Persona("55667788", "Ana", "Martínez", "555-3456")
    
    # Insertar personas en la tabla hash
    tabla.insertar(p1)
    tabla.insertar(p2)
    tabla.insertar(p3)
    tabla.insertar(p4)
    
    # Mostrar estructura de la tabla
    print("--- Estructura de la Tabla Hash ---")
    tabla.mostrar_tabla()
    
    # Buscar una persona
    print("\n--- Buscar Persona con DNI 87654321 ---")
    persona_encontrada = tabla.buscar("87654321")
    print(persona_encontrada if persona_encontrada else "No encontrado")
    
    # Intentar buscar persona no existente
    print("\n--- Buscar Persona con DNI 99999999 ---")
    persona_no_existente = tabla.buscar("99999999")
    print(persona_no_existente if persona_no_existente else "No encontrado")
    
    # Eliminar una persona
    print("\n--- Eliminar Persona con DNI 11223344 ---")
    if tabla.eliminar("11223344"):
        print("Persona eliminada correctamente")
    else:
        print("No se encontró la persona para eliminar")
    
    # Listar todas las personas después de eliminar
    print("\n--- Listado Completo de Personas ---")
    for persona in tabla.listar():
        print(persona)