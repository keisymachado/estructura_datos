class Contacto:
    def __init__(self, id : int, nombre: str, telefono:str):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
    
    def __str__(self):
        return f"{self.id}: {self.nombre} - {self.telefono}"

class Agenda:
    def __init__(self, tamaño=10):
        self.tabla = [[] for _ in range(tamaño)]
    
    def _hash(self, id):
        return hash(str(id)) % len(self.tabla)
    
    def agregar(self, contacto):
        indice = self._hash(contacto.id)
        for k in self.tabla[indice]:
            if k.id == contacto.id:
                print(f" ID {contacto.id} ya existe")
                return False
        
        self.tabla[indice].append(contacto)
        print(f" {contacto.nombre} agregado en posición {indice}")
        return True
    
    def agregar_con_hash(self, clave: str, valor: str):
        if len(self.tabla) < 10:
            hash_clave = hash(clave)
            indice = self._hash(hash_clave)
            self.tabla[indice].append((clave, valor, hash_clave))
            print(f"\nContacto agregado:")
            print(f"   Nombre  : {clave}")
            print(f"   Teléfono: {valor}")
            print(f"   Hash    : {hash_clave}")
            print(f"   Índice  : {indice}")
        else:
            print("No hay espacio en la tabla para agregar más contactos.")
    
    def buscar(self, id):
        indice = self._hash(id)
        for contacto in self.tabla[indice]:
            if isinstance(contacto, Contacto) and contacto.id == id:
                return contacto
        return None
    
    def eliminar(self, id):
        indice = self._hash(id)
        for i, contacto in enumerate(self.tabla[indice]):
            if isinstance(contacto, Contacto) and contacto.id == id:
                del self.tabla[indice][i]
                print(f"Contacto {id} eliminado")
                return True
        print(f"Contacto {id} no encontrado")
        return False
    
    def mostrar(self):
        print("\n AGENDA COMPLETA")
        for i, cubeta in enumerate(self.tabla):
            if cubeta:
                print(f" Cubeta {i}:")
                for contacto in cubeta:
                    print(f"   {contacto}")

if __name__ == "__main__":
    agenda = Agenda(5)
    
 
    agenda.agregar(Contacto("1001", "Ana García", "555-1001"))
    agenda.agregar(Contacto("1002", "Luis Martínez", "555-1002"))
    agenda.agregar(Contacto("1003", "Carlos López", "555-1003"))
    
    agenda.agregar_con_hash("Pedro Pérez", "555-2001")
    agenda.agregar_con_hash("María Rodríguez", "555-2002")
   
    print("\n Buscando contacto 1002:")
    print(agenda.buscar("1002") or "No encontrado")

    agenda.mostrar()
    
    agenda.eliminar("1002")
 
    agenda.mostrar()
