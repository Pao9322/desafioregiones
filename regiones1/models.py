from django.db import models


# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    telefono_personal = models.CharField(max_length=20)
    correo_electronico = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    @classmethod
    def crear_usuario(cls, nombres, apellidos, rut, direccion, telefono_personal, correo_electronico, tipo_usuario):
        usuario = cls(nombres=nombres, apellidos=apellidos, rut=rut, direccion=direccion, telefono_personal=telefono_personal, correo_electronico=correo_electronico, tipo_usuario=tipo_usuario)
        usuario.save()
        return usuario

    @classmethod
    def listar_usuarios(cls):
        return cls.objects.all()

    def actualizar_usuario(self, nombres, apellidos, rut, direccion, telefono_personal, correo_electronico, tipo_usuario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.rut = rut
        self.direccion = direccion
        self.telefono_personal = telefono_personal
        self.correo_electronico = correo_electronico
        self.tipo_usuario = tipo_usuario
        self.save()

    def borrar_usuario(self):
        self.delete()   

    
class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLE_CHOICES)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    @classmethod
    def crear_inmueble(cls, nombre, descripcion, m2_construidos, m2_terreno, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_mensual):
        inmueble = cls(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_terreno=m2_terreno, estacionamientos=estacionamientos, habitaciones=habitaciones, banos=banos, direccion=direccion, comuna=comuna, tipo_inmueble=tipo_inmueble, precio_mensual=precio_mensual)
        inmueble.save()
        return inmueble

    @classmethod
    def listar_inmuebles(cls, comuna):
        return cls.objects.filter(comuna=comuna)

    def actualizar_inmueble(self, nombre, descripcion, m2_construidos, m2_terreno, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_mensual, usuario):
        self.nombre = nombre
        self.descripcion = descripcion
        self.m2_construidos = m2_construidos
        self.m2_terreno = m2_terreno
        self.estacionamientos = estacionamientos
        self.habitaciones = habitaciones
        self.banos = banos
        self.direccion = direccion
        self.comuna = comuna
        self.tipo_inmueble = tipo_inmueble
        self.precio_mensual = precio_mensual
        self.usuario = usuario
        self.save()

    def borrar_inmueble(self):
        self.delete()

