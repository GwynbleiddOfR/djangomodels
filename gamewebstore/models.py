from django.db import models
from .enumeraciones import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    nomb_usuario=models.CharField(max_length=13, null=False, verbose_name="Nombre de usuario")
    sexo=models.CharField(max_length=1,choices=TIPO_SEXO)
    correo = models.EmailField(unique=True, null=False)
    telefono=models.CharField(max_length=8, null=False)
    ciudad=models.CharField(max_length=20, choices=NOMB_CIUDAD)
    direccion=models.CharField(max_length=75, null=False)
    contraseña = models.CharField(max_length=50, null=False, default='')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nomb_juego=models.CharField(max_length=100, null=False, verbose_name="Nombre")
    genero=models.CharField(max_length=50, null=False)
    consola=models.CharField(max_length=3, choices=TIPO_CONSOLA)
    precio=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999999)])
    stock=models.PositiveIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(99)])
    descripcion=models.TextField()
    foto_juego=models.ImageField(upload_to='juegos',null=False, verbose_name="Imagen")
    vendedor = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.nomb_juego

class Pedido(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'Pedido {self.id} - {self.comprador.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    juego = models.ForeignKey(Juego, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.juego.nombre}'

class SuspenderUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    numero_de_dias = models.PositiveIntegerField()
    motivo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fsuspender_u=models.ImageField(upload_to='susp_user',null=False, verbose_name="Imagen")

    def __str__(self):
        return f"Suspensión de {self.usuario} por {self.numero_de_dias} días"

class EliminarUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=100)
    descripcion = models.TextField()
    feliminar_u=models.ImageField(upload_to='del_user',null=False, verbose_name="Imagen")