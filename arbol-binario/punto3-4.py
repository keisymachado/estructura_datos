import pandas as pd
from typing import Optional

class Hospital:
    def __init__(self, NIT: int, Organizacion: str, Sede: str, Municipio: str) -> None:
        # Almacena los datos básicos de un hospital
        self.NIT = NIT                # Número de identificación tributaria (único)
        self.Organizacion = Organizacion  # Nombre legal de la institución
        self.Sede = Sede              # Nombre específico de la sede/filial
        self.Municipio = Municipio    # Ubicación geográfica

    def __str__(self) -> str:
        # Devuelve una representación legible de los datos del hospital
        return f"NIT: {self.NIT}, Organización: {self.Organizacion}, Sede: {self.Sede}, Municipio: {self.Municipio}"

class Nodo:
    def __init__(self, hospital: Hospital) -> None:
        # Estructura de nodo para el árbol binario
        self.hospital = hospital  # Objeto Hospital almacenado en este nodo
        self.izq = None          # Referencia al nodo hijo izquierdo
        self.der = None          # Referencia al nodo hijo derecho

class ArbolBinario:
    def __init__(self, root=None) -> None:
        # Inicializa un árbol binario vacío
        self.root = root         # Nodo raíz del árbol

    def insertar(self, hospital: Hospital) -> None:
        # Inserta un nuevo hospital en el árbol
        if self.root is None:
            # Si el árbol está vacío, crea el nodo raíz
            self.root = Nodo(hospital)
        else:
            # Si hay nodos, busca la posición correcta
            self._insertar_recursivo(hospital, self.root)

    def _insertar_recursivo(self, hospital: Hospital, nodo: Nodo) -> None:
        # Función recursiva para encontrar posición de inserción
        if hospital.NIT < nodo.hospital.NIT:
            # Si el NIT es menor, va al subárbol izquierdo
            if nodo.izq is None:
                # Si no hay hijo izquierdo, inserta aquí
                nodo.izq = Nodo(hospital)
            else:
                # Si hay hijo izquierdo, sigue buscando
                self._insertar_recursivo(hospital, nodo.izq)
        else:
            # Si el NIT es mayor o igual, va al subárbol derecho
            if nodo.der is None:
                # Si no hay hijo derecho, inserta aquí
                nodo.der = Nodo(hospital)
            else:
                # Si hay hijo derecho, sigue buscando
                self._insertar_recursivo(hospital, nodo.der)

    def buscar(self, NIT: int) -> Optional[Hospital]:
        # Busca un hospital por su NIT
        return self._buscar_recursivo(NIT, self.root)

    def _buscar_recursivo(self, NIT: int, nodo: Optional[Nodo]) -> Optional[Hospital]:
        # Búsqueda recursiva por NIT
        if nodo is None:
            # Caso base: nodo vacío (no encontrado)
            return None
        if NIT == nodo.hospital.NIT:
            # Encontró coincidencia exacta
            return nodo.hospital
        elif NIT < nodo.hospital.NIT:
            # Busca en el subárbol izquierdo si el NIT es menor
            return self._buscar_recursivo(NIT, nodo.izq)
        else:
            # Busca en el subárbol derecho si el NIT es mayor
            return self._buscar_recursivo(NIT, nodo.der)

# Procesamiento del archivo CSV
hospitales = pd.read_csv('arbol-binario/tarea3.csv')

# Normalización de nombres de columnas
hospitales.rename(columns={
    'Número NIT': 'NIT',
    'Razón Social Organización': 'Organizacion',
    'Nombre Sede': 'Sede',
    'Nombre Municipio': 'Municipio'
}, inplace=True)

# Limpieza y conversión del campo NIT
hospitales['NIT'] = hospitales['NIT'].str.replace(',', '').astype(int)

# Construcción del árbol binario
arbol = ArbolBinario()
for _, fila in hospitales.iterrows():
    # Crea objeto Hospital por cada registro
    hospital = Hospital(
        NIT=fila['NIT'],
        Organizacion=fila['Organizacion'],
        Sede=fila['Sede'],
        Municipio=fila['Municipio']
    )
    # Inserta el hospital en el árbol
    arbol.insertar(hospital)

# Interfaz de usuario principal
while True:
    print("Options:")
    print("1. Search hospital by NIT")
    print("2. Exit")

    opcion = input("Select an option: ")

    if opcion == "1":
        # Manejo de búsqueda por NIT
        nit = input("Enter hospital NIT: ")
        try:
            nit_numero = int(nit)
            hospital = arbol.buscar(nit_numero)
            if hospital:
                print("Hospital found:")
                print(hospital)
            else:
                print("No hospital found with that NIT")
        except ValueError:
            print("Please enter a valid number")
    elif opcion == "2":
        # Salida del programa
        print("Exiting program...")
        break
    else:
        # Manejo de opción inválida
        print("Invalid option")