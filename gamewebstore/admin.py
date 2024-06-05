from django.contrib import admin
from .models import Usuario, Juego, Pedido, DetallePedido

class AdmUsuario(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'nomb_usuario', 'sexo', 'correo', 'telefono', 'ciudad', 'direccion']
    list_filter=['ciudad']

class AdmJuego(admin.ModelAdmin):
    list_display=['id', 'nomb_juego', 'genero', 'consola', 'precio', 'stock', 'descripcion', 'foto_juego']
    list_filter=['consola']

class AdmPedido(admin.ModelAdmin):
    list_display=['comprador', 'fecha_pedido', 'estado']
    list_filter=['fecha_pedido']

class AdmDetallePedido(admin.ModelAdmin):
    list_display=['pedido', 'juego', 'cantidad', 'precio_unitario']

# Register your models here.
admin.site.register(Usuario, AdmUsuario)
admin.site.register(Juego, AdmJuego)
admin.site.register(Pedido, AdmPedido)
admin.site.register(DetallePedido, AdmDetallePedido)