class Tarea:
    def __init__(self ,nombre ,completada=False):
        self.nombre= nombre
        self.completada= completada
    def completada(self):   
        self.completada= True
    def __str__(self):
        estado = "Completada " if self.completada else "No Completada"
        return f"{self.nombre} - {estado}"   
