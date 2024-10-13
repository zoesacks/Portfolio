from django.db import models
from configuracion.utils import *

# ---------------------------------------------------------------------------------------------------
# Modelo para datos personales
# ---------------------------------------------------------------------------------------------------
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido =models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()
    sobre_mi = models.TextField(blank=True, null=True)


    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'Personas' 

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(Persona, self).save(*args, **kwargs)


    # ----------- Metodos de la instancia --------------

    def calcular_edad(self):
        edad = fecha_actual.year - self.fecha_de_nacimiento.year
        return edad
    
    def obtener_contacto(self):
        contactos = self.contacto_set.all()
        return contactos
    
    def obtener_experiencias(self):
        experiencias = self.experiencias_set.all()
        return experiencias
    

# ---------------------------------------------------------------------------------------------------
# Modelo para contacto
# ---------------------------------------------------------------------------------------------------
class Contacto(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    enlace = models.URLField(blank=True, null=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
 
    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'Contactos' 

    def __str__(self):
        return f'{self.titulo}'
    
    def clean(self): 
        return super().clean()
 
    def save(self, *args, **kwargs):
        super(Contacto, self).save(*args, **kwargs)


# ---------------------------------------------------------------------------------------------------
# Modelo para experiencia
# ---------------------------------------------------------------------------------------------------
class Experiencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    institucion = models.CharField(max_length=255)

    desde = models.DateField()
    hasta = models.DateField(blank=True, null=True)

    categoria = models.CharField(max_length=255, choices=CATEGORIASEXPERIENCIA)


    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'experiencia'
        verbose_name_plural = 'Experiencias' 

    def __str__(self):
        return f'{self.titulo}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(Experiencia, self).save(*args, **kwargs)


# ---------------------------------------------------------------------------------------------------
# Modelo para proyecto
# ---------------------------------------------------------------------------------------------------
class Proyecto(models.Model):
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    enlace_ver = models.URLField(blank=True, null=True)
    enlace_repositorio = models.URLField(blank=True, null=True)


    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'Proyectos' 

    def __str__(self):
        return f'{self.titulo}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(Proyecto, self).save(*args, **kwargs)


# ---------------------------------------------------------------------------------------------------
# Modelo para habilidad
# ---------------------------------------------------------------------------------------------------
class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)


    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'Habilidades' 

    def __str__(self):
        return f'{self.nombre}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(Habilidad, self).save(*args, **kwargs)



# ---------------------------------------------------------------------------------------------------
# Modelo para asociar proyecto y habilidad
# ---------------------------------------------------------------------------------------------------
class ProyectoHabilidad(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)

    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'proyecto y habilidad'
        verbose_name_plural = 'Proyectos y Habilidades' 

    def __str__(self):
        return f'{self.proyecto} - {self.habilidad}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(ProyectoHabilidad, self).save(*args, **kwargs)


# ---------------------------------------------------------------------------------------------------
# Modelo para asociar proyecto e imagen
# ---------------------------------------------------------------------------------------------------
class ProyectoImagen(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    imagen = models.ImageField()

    # ----------- Metodos base del modelo --------------

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'Imagenes' 

    def __str__(self):
        return f'{self.proyecto}'
    
    def clean(self): 
        return super().clean()

    def save(self, *args, **kwargs):
        super(ProyectoImagen, self).save(*args, **kwargs)
