class Estudiante:
    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion: float):
        if 0 <= calificacion <= 5:
            self.calificaciones.append(calificacion)
        else:
            print("La calificación debe estar entre 0 y 5.")

    def calcular_promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def aprobo_curso(self):
        return self.calcular_promedio() >= 3  


estudiante1 = Estudiante("keisy", 5, "estructuctura de datos")
estudiante1.agregar_calificacion(5)
estudiante1.agregar_calificacion(4)
estudiante1.agregar_calificacion(2)
print(f"Promedio de calificaciones: {estudiante1.calcular_promedio()}")
print(f"¿Aprobó el curso? {'Sí' if estudiante1.aprobo_curso() else 'No'}")