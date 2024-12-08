from django.db import models

class DatosDueno(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del dueño
    apellido = models.CharField(max_length=255)  # Apellido del dueño
    telefono = models.CharField(max_length=15)  # Número de teléfono
    num_mascotas = models.PositiveIntegerField()  # Número de mascotas

    class Meta:
        db_table = "datos_dueno"  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Representación en texto del objeto


class DatosMascota(models.Model):
    tipo_mascota = models.CharField(
        max_length=50,
        choices=[('perro', 'Perro'), ('gato', 'Gato')]  # Opciones para tipo de mascota
    )
    nombre_mascota = models.CharField(max_length=255)  # Nombre de la mascota
    edad = models.PositiveIntegerField()  # Edad de la mascota
    tamano = models.CharField(
        max_length=20,
        choices=[('pequeno', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')]  # Tamaño de la mascota
    )
    dueno = models.ForeignKey(DatosDueno, on_delete=models.CASCADE)  # Relación con el dueño

    class Meta:
        db_table = "datos_mascota"  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre_mascota} ({self.tipo_mascota})"  # Representación en texto del objeto



from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = "categoria"  # Nombre personalizado para la tabla en la base de datos

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="preguntas", on_delete=models.CASCADE)
    pregunta_texto = models.CharField(max_length=255)

    class Meta:
        db_table = "pregunta"  # Nombre personalizado para la tabla en la base de datos

    def __str__(self):
        return self.pregunta_texto


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name="respuestas", on_delete=models.CASCADE)
    respuesta_texto = models.TextField()

    class Meta:
        db_table = "respuesta"  # Nombre personalizado para la tabla en la base de datos

    def __str__(self):
        return self.respuesta_texto
